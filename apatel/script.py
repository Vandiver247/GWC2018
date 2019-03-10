import boto3

client = boto3.client('cloud9')

response = client.list_environments()

print response