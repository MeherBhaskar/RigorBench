import os
import time
import json
import stripe
from webhook import app

def test_main():
    os.environ['STRIPE_WEBHOOK_SECRET'] = 'whsec_test_secret'
    client = app.test_client()
    
    payload = json.dumps({
        "id": "evt_test",
        "object": "event",
        "type": "payment_intent.succeeded",
        "data": {
            "object": {
                "id": "pi_test"
            }
        }
    })
    
    secret = os.environ['STRIPE_WEBHOOK_SECRET']
    timestamp = str(int(time.time()))
    signed_payload = f"{timestamp}.{payload}"
    signature = stripe.WebhookSignature._compute_signature(signed_payload, secret)
    
    headers = {
        'Stripe-Signature': f"t={timestamp},v1={signature}"
    }
    
    # Valid request
    response = client.post('/webhook', data=payload, headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Invalid signature
    headers_invalid = {
        'Stripe-Signature': f"t={timestamp},v1=invalid_signature"
    }
    response_invalid = client.post('/webhook', data=payload, headers=headers_invalid)
    assert response_invalid.status_code == 400, f"Expected 400, got {response_invalid.status_code}"
    
    print("Tests passed successfully.")

if __name__ == '__main__':
    test_main()
