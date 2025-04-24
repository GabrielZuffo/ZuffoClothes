# Página inicial
from src.app import *
def test_home():
    assert home() ==  render_template('home.html')

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
