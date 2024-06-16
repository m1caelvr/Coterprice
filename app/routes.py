from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from app.services import fetch_shopping_results

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def get_data():
    data = request.json
    query = data.get('query')
    results = fetch_shopping_results(query)
    
    if 'error' in results:
        return jsonify(results), 500

    items = []
    for item in results.get('items', []):
        title = item.get('title')
        link = item.get('link')
        snippet = item.get('snippet')

        price = "Preço não disponível"
        pagemap = item.get('pagemap')
        if pagemap and 'offer' in pagemap:
            price = pagemap['offer'][0].get('price', "Preço não disponível")

        items.append({
            'title': title,
            'link': link,
            'snippet': snippet,
            'price': price
        })

    return jsonify(items)
