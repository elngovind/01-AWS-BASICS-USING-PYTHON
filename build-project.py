import boto3
import click

client = boto3.client('ec2')
regions = client.describe_regions()

@click.command()
@click.option('--project',default=None,
              help )
def list_instances_across_all_regions():
    "Listing of instances across all regions"
    for r in client.describe_regions()['Regions']:
        ec2 = boto3.resource('ec2',region_name=r['RegionName'])
        print("List of instances in ", r['RegionName'])
        instances = ec2.instances.all()
        for i in instances:
            print(i.id)

if __name__ == '__main__':
    list_instances_across_all_regions()
