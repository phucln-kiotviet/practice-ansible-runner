import sys

import ansible_runner

out, err, rc = ansible_runner.run_command(
    executable_cmd='ansible-playbook',
    cmdline_args=['../phucln-ansible/playbook/install-user.yml', '-i', 'inventory', '-vvv', '-k'],
    input_fd=sys.stdin,
    output_fd=sys.stdout,
    error_fd=sys.stderr,
)

print("rc: {}".format(rc))
print("out: {}".format(out))
print("err: {}".format(err))
