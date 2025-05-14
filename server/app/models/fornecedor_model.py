from app.db import mongo

def inserir_fornecedor(data):
    return mongo.db.fornecedores.insert_one(data)

def listar_fornecedores():
    return list(mongo.db.fornecedores.find())

def buscar_fornecedor_por_id(fornecedor_id):
    return mongo.db.fornecedores.find_one({"_id": fornecedor_id})

def atualizar_fornecedor(fornecedor_id, data):
    return mongo.db.fornecedores.update_one({"_id": fornecedor_id}, {"$set": data})

def deletar_fornecedor(fornecedor_id):
    return mongo.db.fornecedores.delete_one({"_id": fornecedor_id})
