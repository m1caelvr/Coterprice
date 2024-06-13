import requests
from app.config import Config

def fetch_shopping_results(query):
    api_key = Config.GOOGLE_SEARCH_API_KEY
    cse_id = Config.GOOGLE_CSE_ID
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id,
        'googlehost': 'google.com.br',
        'gl': 'br',
        'tbm': 'shop'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()