from flask import Flask
from app.config import Config
from app.routes import produtos

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(produtos.produto_bp)

    return app
