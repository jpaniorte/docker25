import AWSCli as utils

if __name__ == "__main__":
    data = utils.read_intances_file('instances_private_data.yaml')

    profile_name = data['profile_name']
    ami_id = data['ami_id']
    key_name = data['key_name']
    security_group_id = data['security_group_id']
    subnet_id = data['subnet_id']
    instance_type = data['instance_type']

    for instance in data['instances']:
        print(f"Analizando {instance['name']} ... ")
        instance_id, instance_status = utils.get_instance_status(instance['name'], profile_name)
        
        if instance_id == 'Not found':
            instance_id = utils.create_ec2_instance(
                instance['pub_key'],
                instance['name'],
                ami_id,
                instance_type,
                key_name,
                profile_name,
                security_group_id,
                subnet_id
            )
        


