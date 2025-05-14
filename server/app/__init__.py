from flask import Flask
from app.config import Config
from app.routes import produtos
from app.routes import fornecedor 
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(produtos.produto_bp)
    app.register_blueprint(fornecedor.fornecedor_bp)

    return app
