import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_public_data(client):
    response = client.get('/public/data')
    assert response.status_code == 200
    assert response.get_json() == {"data": "This is public"}

def test_protected_data_unauthenticated(client):
    response = client.get('/protected/data')
    assert response.status_code == 401

def test_protected_data_authenticated(client):
    response = client.get('/protected/data', headers={"Authorization": "Bearer secret-token"})
    assert response.status_code == 200
    assert response.get_json() == {"data": "This should be protected"}
