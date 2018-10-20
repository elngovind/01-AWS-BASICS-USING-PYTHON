import boto3
import logging

client = boto3.client('ec2')

instances = []
for region in client.describe_regions()['Regions']:
   # print(region)
    ec2 = boto3.resource('ec2', region_name=region['RegionName'])
    #print("Hey The Output is")
    print ('Listing of ec2 instances in region ', region['RegionName'])
    #print(region['RegionName'])
    result = ec2.instances.all()
    for instance in result:
            print("\t The InstanceID is\t",instance.id,"\nThe Instance Capacity is---->",instance.instance_type)
            #print(instance.instance_type)
            print("\t The Instance state id \t ",instance.state['Name'])
    #print(result)
#print (instances)
