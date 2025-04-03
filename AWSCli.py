import yaml
import boto3
from botocore.exceptions import ClientError

def get_instance_status(name: str, profile_name: str = None):
    try:
        session = boto3.Session(profile_name=profile_name)
        ec2 = session.client('ec2')

        response = ec2.describe_instances(
            Filters=[{'Name': 'tag:Name', 'Values': [name]}]
        )

        if response['Reservations']:
            instance = response['Reservations'][0]['Instances'][0]
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            return instance_id, state
        else:
            return "Not found", "Unknown"
    
    except ClientError as e:
        return f"Error al intentar obtener el estado de la instancia: {e}", "Unknown"

def create_ec2_instance(user_pub_key: str,
                        instance_name: str,
                        ami_id: str,
                        instance_type: str,
                        key_name: str,
                        profile_name: str = None, 
                        security_group_id: str = None, 
                        subnet_id: str = None):
    try:
        session = boto3.Session(profile_name=profile_name)
        ec2 = session.client('ec2')

        user_data_script = f"""#!/bin/bash
        echo "{user_pub_key}" >> /home/ubuntu/.ssh/authorized_keys
        chown ubuntu:ubuntu /home/ubuntu/.ssh/authorized_keys
        chmod 600 /home/ubuntu/.ssh/authorized_keys
        """

        response = ec2.run_instances(
            ImageId=ami_id,  
            InstanceType=instance_type,  # Tipo de instancia (t2.micro para Free Tier)
            MinCount=1,
            MaxCount=1,
            KeyName=key_name,  # Nombre de la clave SSH
            SecurityGroupIds=[security_group_id],  # ID de tu grupo de seguridad
            SubnetId=subnet_id,  # ID de la subred
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': instance_name}
                ]
            }],
            UserData=user_data_script 
        )

        instance_id = response['Instances'][0]['InstanceId']
        print(f"Instancia EC2 {instance_id} creada con éxito.")
        return instance_id

    except ClientError as e:
        print(f"Error al crear la instancia: {e}")
        return None

def read_intances_file(filename: str):
    with open(filename, 'r') as file:
        return yaml.safe_load(file)

def waiter(instance_id, profile_name, event):

        session = boto3.Session(profile_name=profile_name)
        ec2 = session.client('ec2')

        waiter = ec2.get_waiter(event)
        waiter.wait(InstanceIds=[instance_id])

        print(f"La instancia {instance_id} ha sido detenida.")

def change_instance_state(state: str, instance_id: str, profile_name: str = None):
    try:
        session = boto3.Session(profile_name=profile_name)
        ec2 = session.client('ec2')

        if state == 'running':
            response = ec2.start_instances(InstanceIds=[instance_id])
            return f"Instancia {instance_id} iniciada. Estado: {response['StartingInstances'][0]['CurrentState']['Name']}"
        
        elif state == 'stopped':
            response = ec2.stop_instances(InstanceIds=[instance_id])
            return f"Instancia {instance_id} detenida. Estado: {response['StoppingInstances'][0]['CurrentState']['Name']}"
        
        else:
            return "El estado proporcionado debe ser 'running' o 'stopped'."
    
    except ClientError as e:
        return f"Error al intentar cambiar el estado de la instancia: {e}"
