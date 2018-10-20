import boto3
def list_instances_us_east_1():
    session = boto3.Session(profile_name = 'us-east-1')
    ec2 = session.resource('ec2')
    for i in ec2.instances.all():
        print(i)

if __name__ == '__main__':
    print ("Instances of North Virginia are ")
    list_instances_us_east_1()
    #print ("Instances of Ohio are ")
    #list_instances_us_east_2()
#CLI to access ec2 profile