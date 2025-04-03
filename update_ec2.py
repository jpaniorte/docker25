import AWSCli as utils

if __name__ == "__main__":
    data = utils.read_intances_file('intances_status.yaml')
    profile_name = 'docker25'

    for instance in data['instances']:
        print(f"Analizando {instance['name']} ... ")
        instance_id, instance_status = utils.get_instance_status(instance['name'], profile_name)
        
        if instance_status == 'stopping':
            print(f"Esperando a que la instancia {instance['name']} pase a stopped")
            utils.waiter(instance_id, profile_name, 'instance_stopped')
            instance_status = 'stopped'
        if instance_status == 'pending':
            print(f"Esperando a que la instancia {instance['name']} pase a running")
            utils.waiter(instance_id, profile_name, 'instance_running')
            instance_status = 'running'

        if instance_status != instance['status']:
            print(f"Pasando la {instance['name']} al estado {instance['status']} ")
            utils.change_instance_state(instance['status'], instance_id, profile_name)


