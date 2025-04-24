import pytest
# Página inicial
from src.app import *

@pytest.fixture
def app_context():
    with app.app_context():
        yield
def test_home(app_context):
    assert home() ==  render_template('home.html')

# Página da loja

def test_loja(app_context):
     assert loja() == render_template('index.html')

# ✅ Nova feature: Lista de camisas em JSON
def test_listar_camisas(app_context):
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
