from app.db import mongo

def inserir_fornecedor(data):
    return mongo.db.produtos.insert_one(data)

def listar_fornecedor():
    return list(mongo.db.produtos.find())

def buscar_fornecedor_por_id(fornecedor_id):
    return mongo.db.produtos.find_one({"_id": fornecedor_id})

def atualizar_fornecedor(fornecedor_id, data):
    return mongo.db.produtos.update_one({"_id": fornecedor_id}, {"$set": data})

def deletar_fornecedor(fornecedor_id):
    return mongo.db.produtos.delete_one({"_id": fornecedor_id})
