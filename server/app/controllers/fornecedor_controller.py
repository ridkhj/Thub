from flask import request, jsonify
from bson import ObjectId
from bson.json_util import dumps
from app.models import fornecedor_model

def criar_fornecedor():
    data = request.get_json()
    result = fornecedor_model.inserir_fornecedor(data)
    return jsonify({"id": str(result.inserted_id)}), 201

def listar_fornecedores():
    fornecedores = fornecedor_model.listar_fornecedores()
    return dumps(fornecedores), 200

def obter_fornecedor(fornecedor_id):
    try:
        obj_id = ObjectId(fornecedor_id)
        fornecedor = fornecedor_model.buscar_fornecedor_por_id(obj_id)
        if not fornecedor:
            return jsonify({"erro": "fornecedor não encontrado"}), 404
        return dumps(fornecedor), 200
    except:
        return jsonify({"erro": "ID inválido"}), 400

def atualizar_fornecedor(fornecedor_id):
    try:
        obj_id = ObjectId(fornecedor_id)
        data = request.get_json()
        resultado = fornecedor_model.atualizar_fornecedor(obj_id, data)
        if resultado.matched_count == 0:
            return jsonify({"erro": "fornecedor não encontrado"}), 404
        return jsonify({"mensagem": "fornecedor atualizado"}), 200
    except:
        return jsonify({"erro": "ID inválido"}), 400

def deletar_fornecedor(fornecedor_id):
    try:
        obj_id = ObjectId(fornecedor_id)
        resultado = fornecedor_model.deletar_fornecedor(obj_id)
        if resultado.deleted_count == 0:
            return jsonify({"erro": "fornecedor não encontrado"}), 404
        return jsonify({"mensagem": "fornecedor deletado"}), 200
    except:
        return jsonify({"erro": "ID inválido"}), 400
