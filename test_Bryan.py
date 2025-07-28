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

def valid_payload():
    return {
        "name": "John Doe",
        "description": "Need food assistance",
        "location": "123 Main St",
        "contact": "555-1234"
    }


def test_request_help_success(client):
    response = client.post("/request_help", json=valid_payload())
    assert response.status_code == 201
    assert response.get_json() == {"message": "Help request submitted successfully"}
    assert HelpRequest.query.count() == 1

def test_request_help_missing_name(client):
    data = valid_payload()
    del data["name"]
    response = client.post("/request_help", json=data)
    assert response.status_code == 400 or response.status_code == 500
    assert HelpRequest.query.count() == 0

def test_request_help_missing_description(client):
    data = valid_payload()
    del data["description"]
    response = client.post("/request_help", json=data)
    assert response.status_code == 400 or response.status_code == 500
    assert HelpRequest.query.count() == 0

def test_request_help_missing_location(client):
    data = valid_payload()
    del data["location"]
    response = client.post("/request_help", json=data)
    assert response.status_code == 400 or response.status_code == 500
    assert HelpRequest.query.count() == 0

def test_request_help_missing_contact(client):
    data = valid_payload()
    del data["contact"]
    response = client.post("/request_help", json=data)
    assert response.status_code == 400 or response.status_code == 500
    assert HelpRequest.query.count() == 0

def test_request_help_empty_payload(client):
    response = client.post("/request_help", json={})
    assert response.status_code == 400 or response.status_code == 500
    assert HelpRequest.query.count() == 0