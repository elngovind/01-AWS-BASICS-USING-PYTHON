import boto3

client = boto3.client('ec2')

instances = []
for region in client.describe_regions()['Regions']:
    ec2 = boto3.resource('ec2', region_name=region['RegionName'])
    print ('Listing of ec2 instances in region ', region['RegionName'])
    result = ec2.instances.all()
    for instance in result:
            print(instance.id,instance.instance_type)
