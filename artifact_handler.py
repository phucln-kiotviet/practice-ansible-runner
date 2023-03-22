import ansible_runner


def my_artifacts_handler(artifacts_dir):
    print(artifacts_dir)


r = ansible_runner.run(private_data_dir='../phucln-ansible', playbook='../phucln-ansible/playbook/install-user.yml',
                       artifacts_handler=my_artifacts_handler)
