import boto3

users = ["apatel1","araval1","amkleinle1","ankleinle1","agupta1","awang1","djain1","edouglas1","ekrever1","ireyes1","iqi1","jauslander1","kli1","mtakahashi1","nmadhav1","nbhatia1","pmurali1","rpatnaik1","jvandiver1","rnagarakanti1","srao1","sshekhawat1","sghatak1","slee1","vagarwal1","smurthy1","usharma1","bburkhardt1","mkauffman1","bkowalczyk1","mvyas1","tnamjoshi1"]

client = boto3.client('cloud9')

response = client.list_environments()

for user in users:
    for environment in response['environmentIds']:
        response = client.create_environment_membership(
            environmentId=environment,
            userArn="arn:aws:iam::150404946404:user/" + user,
            permissions='read-write'
        )
    
        print response

response = client.list_environments(
    nextToken=response['nextToken']
)

for user in users:
    for environment in response['environmentIds']:
        response = client.create_environment_membership(
            environmentId=environment,
            userArn="arn:aws:iam::150404946404:user/" + user,
            permissions='read-write'
        )
    
        print response