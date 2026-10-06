# import AWS SDK for Python
import boto3
# Instantiate a bedrock client
bedrock = boto3.client("bedrock", region_name="us-east-1")
# List foundation models
response = bedrock.list_foundation_models()
print(response)
# CLI equivalent --> aws bedrock list-foundation-models 
# or filtering with --query 'modelSummaries[*].modelName'