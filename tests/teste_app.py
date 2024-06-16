import requests
from bs4 import BeautifulSoup

def buscar_precos_produto(produto, localidade):
    print(1)
    query = f"{produto} em {localidade}"
    url = f"https://www.google.com/search?q={query}"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        resultados = soup.find_all('div', class_='BNeawe iBp4i AP7Wnd')
        
        for resultado in resultados:
            if 'R$' in resultado.text:
                print(resultado.text)
    else:
        print(f"Erro ao fazer requisição: {response.status_code}")

produto = "Baterias de carro"
localidade = "Recife"
buscar_precos_produto(produto, localidade)
