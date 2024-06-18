import docker
from kubernetes import client, config

def deploy_container():
    client = docker.from_env()
    container = client.containers.run('nginx', detach=True, ports={'80/tcp': 8080})
    print(f'Deployed container {container.name}')

def list_k8s_pods():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False)
    for pod in pods.items:
        print(f"{pod.metadata.namespace} - {pod.metadata.name}")

if __name__ == '__main__':
    deploy_container()
    list_k8s_pods()
