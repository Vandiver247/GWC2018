import boto3

client = boto3.client('cloud9')

response = client.list_environments()

reponse = client.list_environments(
    nextToken=response['nextToken']
)

print len(response['environmentIds'])

# response = client.create_environment_membership(
#         environmentId='41ac563ec1af481e8b7dae28920b0352',
#         userArn='arn:aws:iam::150404946404:root',
#         permissions='read-write'
#     )
    
# print response

for environment in response['environmentIds']:
    response = client.create_environment_membership(
        environmentId=environment,
        userArn='arn:aws:iam::150404946404:user/jvandiver1',
        permissions='read-write'
    )

    print response