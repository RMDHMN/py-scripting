from kubernetes import client, config
from kubernetes.client import Configuration, ApiClient

def get_pod_metrics():
    # Charger la configuration à partir du fichier kubeconfig
    config.load_kube_config()
    
    # Configurer l'API des métriques
    configuration = Configuration()
    configuration.host = "https://<kubernetes-api-url>"
    configuration.verify_ssl = False  # Si nécessaire, désactiver la vérification SSL

    api_client = ApiClient(configuration)
    metrics_api = client.CustomObjectsApi(api_client)
    
    # Obtenir les métriques des pods
    metrics = metrics_api.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "pods")
    
    for item in metrics['items']:
        pod_name = item['metadata']['name']
        namespace = item['metadata']['namespace']
        usage = item['containers'][0]['usage']
        print(f"Namespace: {namespace}, Pod: {pod_name}, CPU: {usage['cpu']}, Memory: {usage['memory']}")

if __name__ == "__main__":
    get_pod_metrics()
