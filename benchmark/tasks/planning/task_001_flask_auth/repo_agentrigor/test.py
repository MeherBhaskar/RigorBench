# Test suite for Flask JWT Authentication endpoints
import pytest
from app import app, users

@pytest.fixture
def client():
    app.config['TESTING'] = True
    users.clear()
    with app.test_client() as client:
        yield client

def test_public_endpoint(client):
    rv = client.get('/public/data')
    assert rv.status_code == 200
    assert rv.get_json()['data'] == "This is public"

def test_protected_endpoint_without_token(client):
    rv = client.get('/protected/data')
    assert rv.status_code == 401

def test_register_and_login(client):
    rv = client.post('/register', json={'username': 'testuser', 'password': 'testpass'})
    assert rv.status_code == 201
    
    rv = client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
    assert rv.status_code == 200
    token = rv.get_json().get('token')
    assert token is not None

def test_protected_endpoint_with_token(client):
    client.post('/register', json={'username': 'testuser', 'password': 'testpass'})
    rv = client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
    token = rv.get_json()['token']
    
    rv = client.get('/protected/data', headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 200
    assert rv.get_json()['data'] == "This should be protected"

def test_duplicate_registration(client):
    rv1 = client.post('/register', json={'username': 'dupuser', 'password': 'pass'})
    assert rv1.status_code == 201
    rv2 = client.post('/register', json={'username': 'dupuser', 'password': 'pass'})
    assert rv2.status_code == 400
    assert rv2.get_json()['message'] == 'User already exists'

def test_missing_fields_registration(client):
    rv = client.post('/register', json={'username': 'onlyuser'})
    assert rv.status_code == 400
    assert rv.get_json()['message'] == 'Missing username or password'

def test_invalid_token(client):
    rv = client.get('/protected/data', headers={'Authorization': 'Bearer invalidtokenhere'})
    assert rv.status_code == 401
    assert rv.get_json()['message'] == 'Token is invalid!'
