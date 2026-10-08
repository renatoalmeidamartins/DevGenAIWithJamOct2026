"""
Shopping Assistant Agent — COMPLETED reference implementation.

Same learning objective as the original console lab: a shopping assistant agent
integrated with a Knowledge Base, an action-group Lambda (price lookup + math),
and a Guardrail. Instead of being created by hand in the Bedrock Agents console
(bedrock:CreateAgent), it is defined here with the Strands Agents SDK and
deployed to Amazon Bedrock AgentCore Runtime.

Mapping from the original console lab:
  KB association (Agent Builder)      -> search_products @tool  (bedrock-agent-runtime:Retrieve)
  Action group (Lambda) via console   -> price_lookup + calculator @tools (lambda:InvokeFunction)
  Guardrail attached in console        -> guardrail_id/guardrail_version on BedrockModel
  Foundation model (Nova 2 Lite)       -> BedrockModel(model_id="us.amazon.nova-2-lite-v1:0")

Deployed as: shopping_assistant_agent (AgentCore Runtime)
"""
import json
import os
import boto3
from strands import Agent, tool
from strands.models import BedrockModel
from bedrock_agentcore.runtime import BedrockAgentCoreApp

# ── Clients ────────────────────────────────────────────────────────────────
session = boto3.Session(region_name="us-east-1")
lambda_client = boto3.client("lambda", region_name="us-east-1")
bedrock_agent_runtime = boto3.client("bedrock-agent-runtime", region_name="us-east-1")

# ── Values injected at deploy time (from the lab stack outputs) ─────────────
KNOWLEDGE_BASE_ID = os.environ.get("KNOWLEDGE_BASE_ID", "")
GUARDRAIL_ID      = os.environ.get("GUARDRAIL_ID", "")
GUARDRAIL_VERSION = os.environ.get("GUARDRAIL_VERSION", "1")
TOOL_LAMBDA_NAME  = os.environ.get("TOOL_LAMBDA_NAME", "ShoppingAssistantFunction")


# ── Tool: Knowledge Base retrieval ──────────────────────────────────────────
@tool
def search_products(query: str) -> str:
    """
    Searches the shopping Knowledge Base for product information such as
    manufacturer, description, and rating.

    Args:
        query: The product question or topic to search for.

    Returns:
        Relevant product content retrieved from the knowledge base.
    """
    response = bedrock_agent_runtime.retrieve(
        knowledgeBaseId=KNOWLEDGE_BASE_ID,
        retrievalQuery={"text": query},
        retrievalConfiguration={
            "vectorSearchConfiguration": {"numberOfResults": 5}
        },
    )
    results = response.get("retrievalResults", [])
    if not results:
        return "No relevant product information found for this query."
    formatted = []
    for i, r in enumerate(results, 1):
        content = r.get("content", {}).get("text", "")
        formatted.append(f"[Result {i}] {content}")
    return "\n\n".join(formatted)


# ── Tool: Price lookup (Lambda action group) ────────────────────────────────
@tool
def price_lookup(product_id: str) -> str:
    """
    Looks up the price of a product. Supply either a product id (e.g. P001)
    or a product name (e.g. "string trimmer").

    Args:
        product_id: The product identifier or product name.

    Returns:
        The product price as a string.
    """
    response = lambda_client.invoke(
        FunctionName=TOOL_LAMBDA_NAME,
        InvocationType="RequestResponse",
        Payload=json.dumps({
            "function": "PriceLookup",
            "parameters": [{"name": "productId", "value": product_id}],
        }),
    )
    body = json.loads(response["Payload"].read())
    return json.loads(body["body"]).get("result", str(body))


# ── Tool: Calculator (Lambda action group) ──────────────────────────────────
@tool
def calculator(oper1: str, oper2: str, operator: str) -> str:
    """
    Performs a simple calculation on two numbers. Use this for any math because
    the assistant is not good at arithmetic on its own.

    Args:
        oper1: The first operand.
        oper2: The second operand.
        operator: One of + - * / (or add, subtract, multiply, divide).

    Returns:
        The result of the calculation as a string.
    """
    response = lambda_client.invoke(
        FunctionName=TOOL_LAMBDA_NAME,
        InvocationType="RequestResponse",
        Payload=json.dumps({
            "function": "MultiFunctionCalculatorTool",
            "parameters": [
                {"name": "oper1", "value": oper1},
                {"name": "oper2", "value": oper2},
                {"name": "operator", "value": operator},
            ],
        }),
    )
    body = json.loads(response["Payload"].read())
    return json.loads(body["body"]).get("result", str(body))


# ── Guardrail-protected model ───────────────────────────────────────────────
# The Guardrail (denies "lawn maintenance advice") is attached directly to the
# model, so every model call is screened — the same effect as attaching the
# Guardrail to the agent in the console.
nova_lite = BedrockModel(
    model_id="us.amazon.nova-2-lite-v1:0",
    boto_session=session,
    guardrail_id=GUARDRAIL_ID,
    guardrail_version=GUARDRAIL_VERSION,
)

# ── System prompt (unchanged wording from the original lab) ─────────────────
SYSTEM_PROMPT = """You are an AI shopping assistant, and you respond to product related questions. Never provide lawn maintenance advice. Do not make assumptions or make up an answer. You are not good at math. So, use the calculator tool provided to answer math questions. You ALWAYS reply politely and concisely, using ONLY the knowledge base (search_products) and the price_lookup and calculator tools available.
"""

# ── Agent ───────────────────────────────────────────────────────────────────
agent = Agent(
    model=nova_lite,
    system_prompt=SYSTEM_PROMPT,
    tools=[search_products, price_lookup, calculator],
)

# ── AgentCore entrypoint ─────────────────────────────────────────────────────
app = BedrockAgentCoreApp()

@app.entrypoint
def agent_invocation(payload, context):
    """AgentCore Runtime handler — receives a shopper question, returns a reply."""
    query = payload.get(
        "prompt",
        "No question provided. Please send a JSON payload with a 'prompt' key."
    )
    result = agent(query)
    return {"result": str(result)}

if __name__ == "__main__":
    app.run()
