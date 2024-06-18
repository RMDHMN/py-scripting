import requests

def fetch_data():
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print(response.json())

fetch_data()
