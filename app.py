from flask import Flask, jsonify, request
import json

app = Flask(__name__)
ARQUIVO_PRODUTOS = 'produtos.json'

def carregar_produtos():
    with open(ARQUIVO_PRODUTOS, 'r') as f:
        return json.load(f)

def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, 'w') as f:
        json.dump(produtos, f, indent=4)

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = carregar_produtos()
    return jsonify(produtos)

@app.route('/produto/<int:id>', methods=['GET'])
def obter_produto(id):
    produtos = carregar_produtos()
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

@app.route('/produto', methods=['POST'])
def adicionar_produto():
    novo_produto = request.json
    produtos = carregar_produtos()
    novo_produto["id"] = max([p["id"] for p in produtos] + [0]) + 1
    produtos.append(novo_produto)
    salvar_produtos(produtos)
    return jsonify(novo_produto), 201

@app.route('/produto/<int:id>', methods=['DELETE'])
def remover_produto(id):
    produtos = carregar_produtos()
    produtos = [p for p in produtos if p["id"] != id]
    salvar_produtos(produtos)
    return jsonify({"mensagem": "Produto removido com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
