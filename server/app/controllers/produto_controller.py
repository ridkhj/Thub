from flask import request, jsonify
from bson import ObjectId
from bson.json_util import dumps
from app.models import produto_model
from app.utils.produto_validator import validar_produto

def criar_produto():
    data = request.get_json()
    produto, erros = validar_produto(data)
    
    if erros:
        return jsonify({ "erros": erros }), 400
    
    result = produto_model.inserir_produto(produto)

    return jsonify({"id": str(result.inserted_id)}), 201

def listar_produtos():
    produtos = produto_model.listar_produtos()
    return dumps(produtos), 200

def obter_produto(produto_id):
    try:
        obj_id = ObjectId(produto_id)
        produto = produto_model.buscar_produto_por_id(obj_id)
        if not produto:
            return jsonify({"erro": "Produto não encontrado"}), 404
        return dumps(produto), 200
    except:
        return jsonify({"erro": "ID inválido"}), 400

def atualizar_produto(produto_id):
    try:
        obj_id = ObjectId(produto_id)
        data = request.get_json()
        resultado = produto_model.atualizar_produto(obj_id, data)
        if resultado.matched_count == 0:
            return jsonify({"erro": "Produto não encontrado"}), 404
        return jsonify({"mensagem": "Produto atualizado"}), 200
    except:
        return jsonify({"erro": "ID inválido"}), 400

def deletar_produto(produto_id):
    try:
        obj_id = ObjectId(produto_id)
        resultado = produto_model.deletar_produto(obj_id)
        if resultado.deleted_count == 0:
            return jsonify({"erro": "Produto não encontrado"}), 404
        return jsonify({"mensagem": "Produto deletado"}), 200
    except:
        return jsonify({"erro": "ID inválido"}), 400
