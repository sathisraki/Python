#!/
import paramiko
import os
router_ip = "x.x.x.x"
router_username = "ladmin"
router_password = "password"
ssh = paramiko.SSHClient()
# Load SSH host keys.
ssh.load_system_host_keys()
# Add SSH host key automatically if needed.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to router using username/password authentication.
ssh.connect(router_ip,
            username=router_username,
            password=router_password,
            look_for_keys=False )
# Run command.
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("pwd")
output = ssh_stdout.readlines()
print(output)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls")
output = ssh_stdout.readlines()
print(output)
# Close connection.
ssh.close()
