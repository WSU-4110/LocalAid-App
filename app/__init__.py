from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import models  # Ensure models are imported for db.create_all
        from .models import User  # Avoid circular import issues

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        db.create_all()

        # Register Blueprints
        from app.routes import main, auth, requests
        app.register_blueprint(main.bp)
        app.register_blueprint(auth.bp)
        app.register_blueprint(requests.bp)

    return app
