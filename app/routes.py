from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from app.services import fetch_shopping_results

app = Flask(__name__)
CORS(app)

# Configuração para habilitar o modo de depuração
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def get_data():
    try:
        data = request.json
        query = data.get('query')
        if not query:
            raise ValueError('Query não foi fornecida.')

        results = fetch_shopping_results(query)
        if results is None:
            return jsonify({'error': 'Erro ao buscar os dados. Por favor, tente novamente mais tarde.'}), 500

        print(results)
        return jsonify(results)

    except Exception as e:
        print(f"Erro na requisição: {str(e)}")
        return jsonify({'error': 'Erro ao buscar os dados. Por favor, tente novamente mais tarde.'}), 500
