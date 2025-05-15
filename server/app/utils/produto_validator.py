from cerberus import Validator

produto_schema = {
    "nome": { "type": "string", "required": True, "empty": False },
    "marca": { "type": "string", "required": True, "empty": False },
    "categoria": { "type": "string", "required": True, "empty": False },
    "quantidade": { "type": "integer", "min": 0, "required": True },
    "preco": { "type": "float", "min": 0, "required": True },
    "fornecedor_id": { "type": "string", "required": True, "empty": False }
}

def validar_produto(data):
    v = Validator(produto_schema, purge_unknown=True)

    if not v.validate(data):
        return None, v.errors
    
    return v.document, None
