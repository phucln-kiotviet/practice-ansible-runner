from ansible_runner import Runner, RunnerConfig

# Using tag using RunnerConfig
rc = RunnerConfig(
    private_data_dir="../phucln-ansible",
    playbook="../phucln-ansible/playbook/install-user.yml",
    tags="my_tag",
)
rc.prepare()
r = Runner(config=rc)
r.run()
