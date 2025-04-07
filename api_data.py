import requests

API_KEY = 'vWs0KRO+8EXDwZmEymGbVQ==8FIbHbQN6aQPc9vw'

def fetch_animal_data(name):
    url = f"https://api.api-ninjas.com/v1/animals?name={name}"
    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.get(url, headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            print(f"No animal data found for '{name}'.")
            return []
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching animal data: {e}")
        return []