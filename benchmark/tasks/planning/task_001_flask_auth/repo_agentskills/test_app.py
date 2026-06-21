import pytest
import json
from app import app, users

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # clear users before each test
        users.clear()
        yield client

def test_public_data(client):
    response = client.get('/public/data')
    assert response.status_code == 200
    assert response.json['data'] == 'This is public'

def test_protected_data_unauthorized(client):
    response = client.get('/protected/data')
    assert response.status_code == 401
    assert 'Token is missing!' in response.json['message']

def test_register_user(client):
    response = client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 201
    assert 'User registered successfully' in response.json['message']
    assert 'testuser' in users

def test_login_user(client):
    client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    response = client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
    assert 'token' in response.json

def test_protected_data_authorized(client):
    client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    login_response = client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
    token = login_response.json['token']
    
    response = client.get('/protected/data', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.json['data'] == 'This should be protected'
    assert response.json['user'] == 'testuser'
