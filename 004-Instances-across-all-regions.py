import boto3

client = boto3.client('ec2')

instances = []
for region in client.describe_regions()['Regions']:
   # print(region)
    ec2 = boto3.resource('ec2', region_name=region['RegionName'])
    print ('Listing of ec2 instances in region ', region['RegionName'])
    #print(region['RegionName'])
    result = ec2.instances.all()
    for instance in result:
            print("\t The InstanceID is ----> ",instance.id,"\tThe Instance Capacity is ---->",instance.instance_type)
            #print(instance.instance_type)
            print("\t Current state ----> ",instance.state['Name'])
    #print(result)
#print (instances)
