from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(model= "bedrock_converse:global.amazon.nova-2-lite-v1:0", 
                    tools=[get_weather])

config = {"configurable": {"thread_id": str(uuid7())}}
#prompt = "What's the weather in San Francisco?"
prompt = "How are you?"

result = agent.invoke(
    {"messages": [{"role": "user", "content": prompt}]},
    config=config,
)
#print(result["messages"][-1].content_blocks)
print(result)
