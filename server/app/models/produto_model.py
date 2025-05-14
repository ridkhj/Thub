from app.db import mongo

def inserir_produto(data):
    return mongo.db.produtos.insert_one(data)

def listar_produtos():
    return list(mongo.db.produtos.find())

def buscar_produto_por_id(produto_id):
    return mongo.db.produtos.find_one({"_id": produto_id})

def atualizar_produto(produto_id, data):
    return mongo.db.produtos.update_one({"_id": produto_id}, {"$set": data})

def deletar_produto(produto_id):
    return mongo.db.produtos.delete_one({"_id": produto_id})
