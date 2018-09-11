import boto3

ec2 = boto3.client('ec2')
regions = ec2.describe_regions()
instances = ec2.describe_instances()
for i in regions:
    instances = ec2.describe_instances()
    print(instances)
