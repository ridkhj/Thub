from flask import Blueprint
from app.controllers import fornecedor_controller

fornecedor_bp = Blueprint('fornecedores', __name__, url_prefix='/fornecedores')

fornecedor_bp.post('')(fornecedor_controller.criar_fornecedor)
fornecedor_bp.get('')(fornecedor_controller.listar_fornecedores)
fornecedor_bp.get('/<fornecedor_id>')(fornecedor_controller.obter_fornecedor)
fornecedor_bp.put('/<fornecedor_id>')(fornecedor_controller.atualizar_fornecedor)
fornecedor_bp.delete('/<fornecedor_id>')(fornecedor_controller.deletar_fornecedor)
