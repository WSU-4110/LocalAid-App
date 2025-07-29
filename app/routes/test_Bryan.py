import pytest
from flask import Flask
from requests import bp 

@pytest.fixture
def app():
    app = Flask(__name__)
    app.secret_key = 'test'
    app.register_blueprint(bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()


def test_browse_route_status_code(client):
    response = client.get('/browse')
    assert response.status_code == 200


def test_browse_route_content(client):
    response = client.get('/browse')
    assert b'browse' in response.data.lower() 


def test_get_post_request_page(client):
    response = client.get('/post-request')
    assert response.status_code == 200


def test_post_request_redirect(client):
    response = client.post('/post-request', data={}, follow_redirects=False)
    assert response.status_code == 302 
    assert '/browse' in response.headers['Location']


def test_post_request_flash_message(client):
    with client.session_transaction() as sess:
        sess['_flashes'] = []

    response = client.post('/post-request', data={}, follow_redirects=True)
    assert b'Your request has been posted!' in response.data

def test_post_request_does_not_flash_on_get(client):
    response = client.get('/post-request')
    assert b'Your request has been posted!' not in response.data