import os
from googleapiclient.discovery import build
from app.config import Config

SEARCH_ENGINE_ID = open('./app/SEARCH_ENGINE_ID').read()
API_KEY = open('./app/API_KEY').read()

def fetch_shopping_results(query):
    api_key = Config.GOOGLE_SEARCH_API_KEY
    cse_id = Config.GOOGLE_CSE_ID

    service = build('customsearch', 'v1', developerKey=API_KEY)
    result = service.cse().list(
        q=query,
        cx=SEARCH_ENGINE_ID,
        googlehost='google.com.br',
        gl='br',
        num=10
    ).execute()

    return result
