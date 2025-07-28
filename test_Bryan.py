import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.api import api_routes
from models import db, HelpRequest

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(api_routes)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_request_help_success(client):

    data = {
        "name": "John Doe",
        "description": "Need food assistance",
        "location": "123 Main St",
        "contact": "555-1234"
    }

    
    response = client.post("/request_help", json=data)

    
    assert response.status_code == 201
    assert response.get_json() == {"message": "Help request submitted successfully"}

    
    help_requests = HelpRequest.query.all()
    assert len(help_requests) == 1
    assert help_requests[0].name == "John Doe"
