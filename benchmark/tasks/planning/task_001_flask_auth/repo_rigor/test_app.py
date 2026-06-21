import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_public_data(client):
    response = client.get('/public/data')
    assert response.status_code == 200
    assert response.json == {"data": "This is public"}

def test_protected_data_without_token(client):
    response = client.get('/protected/data')
    assert response.status_code == 401
    assert "message" in response.json

def test_login(client):
    response = client.post('/login')
    assert response.status_code == 200
    assert "token" in response.json

def test_protected_data_with_token(client):
    # First login
    login_response = client.post('/login')
    token = login_response.json['token']
    
    # Then access protected data
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = client.get('/protected/data', headers=headers)
    assert response.status_code == 200
    assert response.json == {"data": "This should be protected"}
