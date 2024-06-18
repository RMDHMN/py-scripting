import paramiko

def ssh_command():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('hostname', username='user', password='pass')
    stdin, stdout, stderr = ssh.exec_command('ls')
    print(stdout.read().decode())

ssh_command()
