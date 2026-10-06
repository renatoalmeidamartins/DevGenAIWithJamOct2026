# import AWS SDK for Python and json encoder
import boto3, json
# Instantiate a bedrock runtime client
bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

body = json.dumps({
	"anthropic_version": "bedrock-2023-05-31",
	"max_tokens": 5000,
	"messages": [
		{
			"role": "user",
			#"content": "Hello, how is everything?"
			"content": "Create a script to resize images"
			}
	]
})


# Invoke Claude 4.5 Sonnet model using the same payload
response = bedrock_runtime.invoke_model_with_response_stream(
body=body,
    modelId="global.anthropic.claude-sonnet-4-5-20250929-v1:0",
    accept="application/json",
    contentType="application/json"
)

# Read chunks from the stream as they arrive and print them
print("Streaming invoke response:")
stream = response.get("body")
for event in stream:
	chunk = event.get("chunk")
	if chunk:
		chunk_obj = json.loads(chunk.get("bytes").decode())
		if chunk_obj["type"] == "content_block_delta":
			print(chunk_obj["delta"]["text"], end="", flush=True)
