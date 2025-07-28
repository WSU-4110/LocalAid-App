import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test the /browse route (GET)
def test_browse_page(client):
    response = client.get('/browse')
    assert response.status_code == 200
    assert b'<html' in response.data.lower()

# Test the /post-request route (GET)
def test_get_post_request_page(client):
    response = client.get('/post-request')
    assert response.status_code == 200
    assert b'<html' in response.data.lower()

# Test the /post-request route (POST)
def test_post_post_request_page(client):
    response = client.post('/post-request', data={
        'title': 'Need food',
        'category': 'Food',
        'description': 'Urgent help needed'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'<html' in response.data.lower()
