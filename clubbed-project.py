import boto3
import click

client = boto3.client('ec2')
regions = client.describe_regions()

@click.command()


def list_instances_across_all_regions():
    click.echo ("Listing of instances across all regions")
    for r in client.describe_regions()['Regions']:
        ec2 = boto3.resource('ec2',region_name=r['RegionName'])
        print("List of instances in ", r['RegionName'])
        instances = ec2.instances.all()
        for i in instances:
            j =1
            print( "Instances List ")
            print (" ", str(j),i.id,i.tags)
            j+1
if __name__ == '__main__':
    list_instances_across_all_regions()
