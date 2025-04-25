from src.app import *
import pytest
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Página inicial

def test_home():
   with app.app_context():
        rendered = render_template("home.html", name="Tester")
        assert "Tester" in rendered 

# Página da loja

def test_loja():
     assert loja() == render_template('index.html')

# ✅ Nova feature: Lista de camisas em JSON
def test_listar_camisas():
    test_camisas = [
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
    assert listar_camisas() == jsonify(test_camisas)
