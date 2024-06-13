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
    return jsonify(results)