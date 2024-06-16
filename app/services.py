import os
from googleapiclient.discovery import build
from app.config import Config

SEARCH_ENGINE_ID = open('./app/SEARCH_ENGINE_ID').read().strip()
API_KEY = open('./app/API_KEY').read().strip()

def fetch_shopping_results(query):
    try:
        service = build('customsearch', 'v1', developerKey=API_KEY)
        result = service.cse().list(
            q=query,
            cx=SEARCH_ENGINE_ID,
            googlehost='google.com.br',
            gl='br',
            num=10
        ).execute()

        return result

    except Exception as e:
        print(f"Erro na requisição: {e}")
        return {'error': str(e)}
