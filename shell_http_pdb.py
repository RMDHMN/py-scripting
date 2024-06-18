import subprocess
import requests
import pdb

def get_kubernetes_pods():
    # Utiliser subprocess pour exécuter une commande kubectl
    result = subprocess.run(['kubectl', 'get', 'pods', '-o', 'json'], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Erreur: {result.stderr}")
        return None

    return result.stdout

def send_pod_data_to_api(pod_data):
    url = 'https://httpbin.org/post'
    response = requests.post(url, json={"pods": pod_data})
    
    if response.status_code == 200:
        print("Données envoyées avec succès")
    else:
        print(f"Erreur: {response.status_code}")

if __name__ == "__main__":
    pdb.set_trace()  # Point d'arrêt pour le débogage
    
    pod_data = get_kubernetes_pods()
    if pod_data:
        send_pod_data_to_api(pod_data)
