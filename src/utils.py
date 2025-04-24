import json
from os import path

ARQUIVO_PRODUTOS = 'produtos.json'

def carregar_produtos():
    if not path.exists(ARQUIVO_PRODUTOS):
        return []
    with open(ARQUIVO_PRODUTOS, 'r') as f:
        return json.load(f)

def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, 'w') as f:
        json.dump(produtos, f, indent=4)
