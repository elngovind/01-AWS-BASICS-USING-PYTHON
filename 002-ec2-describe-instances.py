import boto3

ec2 = boto3.client('ec2')
instancs = ec2.describe_instances()
print(instancs)
