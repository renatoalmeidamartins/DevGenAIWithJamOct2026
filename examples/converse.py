import boto3, json
# Instantiate a bedrock runtime client
bedrock_client = boto3.client("bedrock-runtime")

# Send the message.
response = bedrock_client.converse(
    modelId=
       #"us.anthropic.claude-sonnet-4-5-20250929-v1:0",
       #"amazon.nova-lite-v1:0",
       "arn:aws:bedrock:us-east-1:526015996414:application-inference-profile/70h20m5n6fwr",
    
    messages=[{
            "role": "user",
            "content": [{"text": "How is everything?"}]
        }],
    system=[{"text": "You are an app developer proficient in Python. Only engage in discussion of coding topics."}],
    inferenceConfig={
        "temperature": 0.7  
        ,"maxTokens": 500 
        #,"topP": 0.9
                        }
    #,additionalModelRequestFields={"top_k": 200}
)

print(response)