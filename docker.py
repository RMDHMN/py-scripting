import docker

def list_containers():
    client = docker.from_env()
    for container in client.containers.list():
        print(container.name)

list_containers()
