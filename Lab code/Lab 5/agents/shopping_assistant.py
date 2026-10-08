"""
Shopping Assistant Agent — Tasks 2–5
Follow the instructions in lab.ipynb (and the lab guide) to complete this file.

You are building the SAME shopping assistant as the original lab, but instead of
clicking "Create agent" in the Bedrock console, you define it in code with the
Strands Agents SDK and deploy it to Amazon Bedrock AgentCore Runtime.

The agent uses:
  - a Knowledge Base retrieval tool  (search_products)   -> Task 3
  - a price lookup tool               (price_lookup)      -> Task 4
  - a calculator tool                 (calculator)        -> Task 4
  - a Bedrock Guardrail on the model  (BedrockModel)      -> Task 5
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


# ── Task 3: Knowledge Base retrieval tool ───────────────────────────────────
# TODO Task 3: Add the complete search_products @tool function here.
# See the lab instructions for the code block to paste. It calls
# bedrock_agent_runtime.retrieve() against KNOWLEDGE_BASE_ID.


# ── Task 4: Action group tools (price lookup + calculator) ──────────────────
# TODO Task 4, Step 1: Add the complete price_lookup @tool function here.
# It invokes the ShoppingAssistantFunction Lambda with function="PriceLookup".

# TODO Task 4, Step 2: Add the complete calculator @tool function here.
# It invokes the ShoppingAssistantFunction Lambda with function="MultiFunctionCalculatorTool".


# ── Task 5: Guardrail-protected model ───────────────────────────────────────
# TODO Task 5: Replace this plain model with a guardrail-protected BedrockModel.
# Add guardrail_id=GUARDRAIL_ID, guardrail_version=GUARDRAIL_VERSION.
nova_lite = BedrockModel(
    model_id="us.amazon.nova-2-lite-v1:0",
    boto_session=session,
)

# ── System prompt ────────────────────────────────────────────────────────────
# TODO Task 2: Replace the placeholder with the shopping assistant system prompt
# from the instructions.
SYSTEM_PROMPT = "<YOUR SYSTEM PROMPT HERE>"

# ── Agent ─────────────────────────────────────────────────────────────────────
# TODO Task 2: Create the agent using nova_lite, SYSTEM_PROMPT, and the three tools.
# agent = Agent(model=nova_lite, system_prompt=SYSTEM_PROMPT,
#               tools=[search_products, price_lookup, calculator])


# ── AgentCore entrypoint (do not modify) ──────────────────────────────────────
app = BedrockAgentCoreApp()

@app.entrypoint
def agent_invocation(payload, context):
    query = payload.get("prompt", "No question provided.")
    result = agent(query)
    return {"result": str(result)}

if __name__ == "__main__":
    app.run()
