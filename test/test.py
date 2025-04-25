import pytest
import sys
import os

# Adiciona o caminho do diretório src ao sys.path para que possamos importar app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app  # Importa o aplicativo Flask

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Testa se a página inicial retorna o status 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_loja(client):
    """Testa se a página da loja retorna o status 200"""
    response = client.get('/loja')
    assert response.status_code == 200

def test_listar_camisas(client):
    """Testa se a API de camisas retorna o JSON esperado"""
    response = client.get('/api/camisas')
    assert response.status_code == 200
    camisas = response.get_json()
    assert isinstance(camisas, list)
    assert len(camisas) == 3
    assert camisas[0]["time"] == "Real Madrid"
    assert camisas[1]["time"] == "Flamengo"
    assert camisas[2]["time"] == "PSG"