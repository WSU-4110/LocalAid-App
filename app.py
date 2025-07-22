from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from routes.api import api_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register routes
app.register_blueprint(api_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
