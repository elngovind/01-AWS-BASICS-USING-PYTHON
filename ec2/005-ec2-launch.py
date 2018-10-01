import boto3
ec2 = boto3.client('ec2')
instance = ec2.run_instances(ImageId='ami-04681a1dbd79675a5', MinCount=1, MaxCount=1)
