from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Página da loja
@app.route('/loja')
def loja():
    return render_template('index.html')

# ✅ Nova feature: Lista de camisas em JSON
@app.route('/api/camisas')
def listar_camisas():
    camisas = [
        {
            "id": 1,
            "time": "Real Madrid",
            "preco": 299.90,
            "tamanhos": ["P", "M", "G", "GG"]
        },
        {
            "id": 2,
            "time": "Flamengo",
            "preco": 249.90,
            "tamanhos": ["P", "M", "G", "GG"]
        },
        {
            "id": 3,
            "time": "PSG",
            "preco": 319.90,
            "tamanhos": ["P", "M", "G", "GG"]
        }
    ]
    return jsonify(camisas)

if __name__ == '__main__':
    app.run(debug=True)
