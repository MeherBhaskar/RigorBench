import pytest
from unittest.mock import patch
import stripe
from webhook import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_missing_signature(client):
    response = client.post('/webhook', data=b'{}')
    assert response.status_code == 400
    assert b'Missing signature' in response.data

@patch('stripe.Webhook.construct_event')
def test_invalid_payload(mock_construct_event, client):
    mock_construct_event.side_effect = ValueError('Invalid payload')
    response = client.post('/webhook', headers={'Stripe-Signature': 'invalid'}, data=b'{}')
    assert response.status_code == 400
    assert b'Invalid payload' in response.data

@patch('stripe.Webhook.construct_event')
def test_invalid_signature(mock_construct_event, client):
    mock_construct_event.side_effect = stripe.error.SignatureVerificationError('Invalid signature', 'sig', 'payload')
    response = client.post('/webhook', headers={'Stripe-Signature': 'invalid'}, data=b'{}')
    assert response.status_code == 400
    assert b'Invalid signature' in response.data

@patch('stripe.Webhook.construct_event')
def test_payment_intent_succeeded(mock_construct_event, client):
    mock_construct_event.return_value = {
        'type': 'payment_intent.succeeded',
        'data': {
            'object': {
                'amount': 1000
            }
        }
    }
    response = client.post('/webhook', headers={'Stripe-Signature': 'valid'}, data=b'{"type": "payment_intent.succeeded"}')
    assert response.status_code == 200
    assert b'OK' in response.data

@patch('stripe.Webhook.construct_event')
def test_other_event_type(mock_construct_event, client):
    mock_construct_event.return_value = {
        'type': 'payment_method.attached',
        'data': {
            'object': {}
        }
    }
    response = client.post('/webhook', headers={'Stripe-Signature': 'valid'}, data=b'{"type": "payment_method.attached"}')
    assert response.status_code == 200
    assert b'OK' in response.data
