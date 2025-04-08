import requests
import os
from dotenv import load_dotenv



load_dotenv()

API_KEY = os.getenv("API_KEY")


def fetch_animal_data(name):
    """
    Fetches the animals data for the animal 'name'.
    Returns: a list of animals, each animal is a dictionary.
    """
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