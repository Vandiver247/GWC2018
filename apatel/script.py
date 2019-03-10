import boto3

client = boto3.client('cloud9')

response = client.list_environments()

print response

for environment in response['environmentIds']:
    response = client.create_environment_membership(
        environmentId=environment,
        userArn='arn:aws:iam::150404946404:root',
        permissions='read-write'
    )

    print response