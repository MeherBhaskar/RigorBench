import pytest
from app import app, db, User
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_public_endpoint(client):
    response = client.get('/public/data')
    assert response.status_code == 200
    assert response.get_json() == {"data": "This is public"}

def test_register_success(client):
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 201
    assert 'User created successfully' in response.get_json()['message']

def test_register_missing_data(client):
    response = client.post('/register', json={
        'username': 'testuser'
    })
    assert response.status_code == 400

def test_register_duplicate(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 400
    assert 'User already exists' in response.get_json()['message']

def test_login_success(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    assert 'token' in response.get_json()

def test_login_failure(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert 'Invalid credentials' in response.get_json()['message']

def test_protected_endpoint_without_token(client):
    response = client.get('/protected/data')
    assert response.status_code == 401
    assert 'Token is missing!' in response.get_json()['message']

def test_protected_endpoint_with_invalid_token(client):
    response = client.get('/protected/data', headers={'Authorization': 'Bearer invalidtoken'})
    assert response.status_code == 401
    assert 'Token is invalid!' in response.get_json()['message']

def test_protected_endpoint_with_valid_token(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    login_response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    token = login_response.get_json()['token']
    
    response = client.get('/protected/data', headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 200
    assert response.get_json() == {"data": "This should be protected"}
