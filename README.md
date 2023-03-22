# ansible-runner

- [python_interface](https://ansible-runner.readthedocs.io/en/stable/python_interface/)


## Helper interfaces

- ansible_runner.interface.run
- ansible_runner.interface.run_async
- ansible_runner.interface.run_command
- ansible_runner.interface.run_command_async
- ansible_runner.interface.get_inventory
- ansible_runner.interface.get_ansible_config
- ansible_runner.interface.get_role_list

## Runner object

- `rc` return code of ansible process
- `status` can be one of:
  - `unstarted`: runner task has been created but hasn't actually started yet.
  - `successful`
  - `failed`


- Some property:
  - ansible_runner.runner.Runner.stdout
  - ansible_runner.runner.Runner.stderr
  - ansible_runner.runner.Runner.events
  - ansible_runner.runner.Runner.stats
  - ansible_runner.runner.Runner.host_events
  - 