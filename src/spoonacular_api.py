"""Spoonacular Api fetch"""
import requests

def fetch_recipes(api_key):
    """Fetches a list of recipes from the Spoonacular API using the provided API key."""
    url = "https://api.spoonacular.com/recipes/random"
    params = {
        "apiKey": api_key,
        "number": 20
    }
    try:
        response = requests.get(url, params=params, timeout=10)  # Add timeout argument
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        return data['recipes']
    except requests.RequestException as e:
        print(f"Error fetching recipes: {e}")
        return []
