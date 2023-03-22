import ansible_runner


def my_event_handler(data):
    # Do something here
    print(data)


r = ansible_runner.run(private_data_dir='../phucln-ansible', playbook='../phucln-ansible/playbook/install-user.yml',
                       event_handler=my_event_handler)
