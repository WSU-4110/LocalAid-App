import pytest
from flask import Flask
from requests import bp  # Replace 'your_module' with the actual Python filename (without .py)

@pytest.fixture
def app():
    app = Flask(__name__)
    app.secret_key = 'test'  # Needed for flashing messages
    app.register_blueprint(bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# 1. Test GET /browse returns 200
def test_browse_route_status_code(client):
    response = client.get('/browse')
    assert response.status_code == 200

# 2. Test GET /browse returns correct template content (optional)
def test_browse_route_content(client):
    response = client.get('/browse')
    assert b'browse' in response.data.lower()  # crude check (adjust if needed)

# 3. Test GET /post-request returns 200
def test_get_post_request_page(client):
    response = client.get('/post-request')
    assert response.status_code == 200

# 4. Test POST /post-request redirects to /browse
def test_post_request_redirect(client):
    response = client.post('/post-request', data={}, follow_redirects=False)
    assert response.status_code == 302  # Redirect
    assert '/browse' in response.headers['Location']

# 5. Test POST /post-request sets flash message
def test_post_request_flash_message(client):
    with client.session_transaction() as sess:
        sess['_flashes'] = []

    response = client.post('/post-request', data={}, follow_redirects=True)
    assert b'Your request has been posted!' in response.data

# 6. Test POST method logic only triggers on POST, not GET
def test_post_request_does_not_flash_on_get(client):
    response = client.get('/post-request')
    assert b'Your request has been posted!' not in response.data