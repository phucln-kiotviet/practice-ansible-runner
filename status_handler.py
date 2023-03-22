import ansible_runner


def my_status_handler(data, runner_config):
    # Do something here
    print(data)


r = ansible_runner.run(private_data_dir='../phucln-ansible', playbook='../phucln-ansible/playbook/install-user.yml',
                       status_handler=my_status_handler)
