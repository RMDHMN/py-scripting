from fabric import Connection

def deploy():
    c = Connection('remote_host')
    c.run('uname -s')
    c.put('myfile.txt', '/tmp/myfile.txt')
    c.run('ls /tmp')

deploy()
