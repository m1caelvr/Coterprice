import requests
from bs4 import BeautifulSoup

def buscar_precos_produto(nome_produto):
    url = f'https://www.google.com/search?q={nome_produto}&tbm=shop'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        resultados = soup.find_all('div', class_='sh-dlr__list-result')

        for resultado in resultados:
            titulo = resultado.find('div', class_='sh-dlr__title').text.strip()
            preco = resultado.find('span', class_='sh-dlr__price').text.strip()
            loja = resultado.find('div', class_='sh-dlr__subtitle').text.strip()

            print(f'Produto: {titulo}')
            print(f'Preço: {preco}')
            print(f'Loja: {loja}')
            print()

    else:
        print(f'Erro ao acessar a página. Código de status: {response.status_code}')

# Exemplo de uso
buscar_precos_produto('bateria de carro')
