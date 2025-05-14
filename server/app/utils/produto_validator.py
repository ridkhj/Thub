from cerberus import Validator

produto_schema = {
    "nome": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "categoria": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "quantidade": {
        "type": "integer",
        "min": 0,
        "required": True
    },
    "preco": {
        "type": "float",
        "min": 0,
        "required": True
    },
    "fornecedor_id": {
        "type": "string",
        "required": True,
        "empty": False
    }
}

fornecedor_schema = {
    'nome': {
        'type': 'string',
        'required': True,
        'empty': False
    },
    'cnpj': {
        'type': 'string',
        'required': True,
        'empty': False
    },
    'email': {
        'type': 'string',
        'required': True,
        'empty': False,
        'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    }  ,
    'telefone': {
        'type': 'string',
        'required': True,
        'empty': False,
        'regex': r'^\(\d{2}\) \d{4,5}-\d{4}$'
    },
}

def validar_produto(data):
    v = Validator(produto_schema, purge_unknown=True)
    if not v.validate(data):
        return None, v.errors
    return v.document, None

def validar_fornecedor(data):
    valide = Validator(fornecedor_schema, purge_unknown=True)
    if not valide.validate(data):
        return None, valide.errors
    return valide.document, None
