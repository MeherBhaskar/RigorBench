import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client

def test_public_data(client):
    response = client.get('/public/data')
    assert response.status_code == 200
    assert response.get_json() == {"data": "This is public"}

def test_protected_data_without_token(client):
    response = client.get('/protected/data')
    assert response.status_code == 401

def test_user_registration(client):
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 201
    assert response.get_json() == {"msg": "User created successfully"}

def test_user_registration_duplicate(client):
    client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 400

def test_login_success(client):
    client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    assert 'access_token' in response.get_json()

def test_login_failure(client):
    response = client.post('/login', json={
        'username': 'wronguser',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401

def test_protected_data_with_token(client):
    client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    login_response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    token = login_response.get_json()['access_token']
    
    response = client.get('/protected/data', headers={
        'Authorization': f'Bearer {token}'
    })
    assert response.status_code == 200
    assert response.get_json()['data'] == "This should be protected"
