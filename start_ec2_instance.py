import boto3
import time
import os
from dotenv import load_dotenv

SECONDS_TO_WAIT_FOR_INSTANCE_PUBLIC_IP = 10

def init_boto3_client(service_name):
    return boto3.client(
        service_name,
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )

def start_ec2_instance(instance_id):
    ec2 = init_boto3_client('ec2')

    print(f"Starting EC2 instance {instance_id}...")
    ec2.start_instances(InstanceIds=[instance_id])
    
    ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])
    print(f"The instance {instance_id} is running")

def get_instance_public_ip(instance_id):
    ec2 = init_boto3_client('ec2')
    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]

    return instance.get('PublicIpAddress')

def update_hosts_file(ip_address, urls):
    hosts_path = os.getenv('HOSTS_PATH')
    
    # backup hosts file
    with open(hosts_path, 'r') as file:
        lines = file.readlines()

    # Filter out any previous lines related to the URLs
    lines = [line for line in lines if not any(url in line for url in urls)]
    
    # Add new entries with the public IP
    with open(hosts_path, 'w') as file:
        file.writelines(lines)
        for url in urls:
            file.write(f"{ip_address} {url}\n")

    print(f"Hosts file updated with IP {ip_address} for: {', '.join(urls)}")
    print("PROCESS COMPLETE! YOU CAN CLOSE THE CONSOLE NOW.")

def load_urls_from_file(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    urls_file_path = os.path.join(current_dir, file_path)

    with open(urls_file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

# EXECUTION STARTS HERE
load_dotenv()

INSTANCE_ID = os.getenv('INSTANCE_ID')

start_ec2_instance(INSTANCE_ID)

print("Waiting for the instance to obtain its public IP...")
time.sleep(SECONDS_TO_WAIT_FOR_INSTANCE_PUBLIC_IP)

public_ip = get_instance_public_ip(INSTANCE_ID)
print(f"The public IP of the instance is: {public_ip}")

if public_ip:
    urls_to_update = load_urls_from_file('hosts.txt')
    update_hosts_file(public_ip, urls_to_update)
else:
    print("ERROR: Could not obtain the public IP of the instance, check the previous messages for more information.")
