from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import carregar_produtos, salvar_produtos
from flask import render_template


app = Flask(__name__)
CORS(app)  # Permite acesso por frontend externo

@app.route('/')
def home():
    return jsonify({"mensagem": "Bem-vindo à loja de futebol ⚽"}), 200

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = carregar_produtos()
    return jsonify(produtos), 200

@app.route('/produto/<int:id>', methods=['GET'])
def obter_produto(id):
    produtos = carregar_produtos()
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        return jsonify(produto), 200
    return jsonify({"erro": "Produto não encontrado"}), 404

@app.route('/produto', methods=['POST'])
def adicionar_produto():
    dados = request.get_json()

    if not dados or 'nome' not in dados or 'preco' not in dados:
        return jsonify({"erro": "Nome e preço são obrigatórios"}), 400

    try:
        preco = float(dados['preco'])
    except ValueError:
        return jsonify({"erro": "Preço inválido"}), 400

    produtos = carregar_produtos()
    novo_id = max([p["id"] for p in produtos], default=0) + 1
    novo_produto = {
        "id": novo_id,
        "nome": dados["nome"],
        "preco": round(preco, 2)
    }
    produtos.append(novo_produto)
    salvar_produtos(produtos)
    return jsonify(novo_produto), 201

@app.route('/produto/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    dados = request.get_json()
    produtos = carregar_produtos()
    produto = next((p for p in produtos if p['id'] == id), None)

    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    if "nome" in dados:
        produto["nome"] = dados["nome"]
    if "preco" in dados:
        try:
            produto["preco"] = float(dados["preco"])
        except ValueError:
            return jsonify({"erro": "Preço inválido"}), 400

    salvar_produtos(produtos)
    return jsonify(produto), 200

@app.route('/produto/<int:id>', methods=['DELETE'])
def remover_produto(id):
    produtos = carregar_produtos()
    produtos_filtrados = [p for p in produtos if p['id'] != id]

    if len(produtos) == len(produtos_filtrados):
        return jsonify({"erro": "Produto não encontrado"}), 404

    salvar_produtos(produtos_filtrados)
    return jsonify({"mensagem": "Produto removido com sucesso"}), 200
@app.route('/loja')
def loja():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
