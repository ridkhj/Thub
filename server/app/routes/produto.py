from flask import Blueprint
from app.controllers import produto_controller

produto_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

produto_bp.post('')(produto_controller.criar_produto)
produto_bp.get('')(produto_controller.listar_produtos)
produto_bp.get('/<produto_id>')(produto_controller.obter_produto)
produto_bp.put('/<produto_id>')(produto_controller.atualizar_produto)
produto_bp.delete('/<produto_id>')(produto_controller.deletar_produto)
