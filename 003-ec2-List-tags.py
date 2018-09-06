import boto3

client = boto3.client('ec2')

response = client.describe_instances()

for r in response['Reservations']:
    for i in r['Instances']:
        for j in i['Tags']:
            print (j['Key'],j['Value']) # Key value eg. Key = Name, Value = Assignment; in this case keys are Key & Value, while values are Name&Assignment
