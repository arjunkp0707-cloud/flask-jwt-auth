from flask import Flask
from app.config import Config
from app.extension import jwt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)

    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.protected import protected_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(protected_bp)

    # Register JWT handlers
    from .handlers.jwt_handlers import register_jwt_handlers

    register_jwt_handlers(jwt)

    return app
