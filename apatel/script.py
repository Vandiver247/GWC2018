import boto3

users = ["apatel1","araval1","amkleinle1","ankleinle1","agupta1","awang1","djain1","edouglas1","ekrever1","ireyes1","iqi1","jauslander1","kli1","mtakahashi1","nmadhav1","nbhatia1","pmurali1","rpatnaik1","rnagarakanti1","srao1","sshekhawat1","sghatak1","slee1","vagarwal1","smurthy1","usharma1","bburkhardt1","mkauffman1","bkowalczyk1","mvyas1","tnamjoshi1"]

client = boto3.client('cloud9')

response = client.list_environments()

for environment in response['environmentIds']:
    env_data = client.describe_environment_memberships(environmentId=environment)
    if len(env_data['memberships']) >= 8:
        env_data = client.describe_environments(environmentIds=[environment])
        print env_data['environments'][0]['name']







# for user in users:
#     for environment in response['environmentIds']:
#         response2 = client.delete_environment_membership(
#             environmentId=environment,
#             userArn="arn:aws:iam::150404946404:user/" + user,
#             #permissions='read-write'
#         )
    
#         print response2

# response = client.list_environments(
#     nextToken=response['nextToken']
# )

# for user in users:
#     for environment in response['environmentIds']:
#         try:
#             response2 = client.delete_environment_membership(
#                 environmentId=environment,
#                 userArn="arn:aws:iam::150404946404:user/" + user,
#                 #permissions='read-write'
#             )
#         except:
#             print "Exception"
#             continue
    
#         print response2