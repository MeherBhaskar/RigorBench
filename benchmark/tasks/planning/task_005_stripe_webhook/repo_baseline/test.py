import json
import time
import stripe
from webhook import app, endpoint_secret

def generate_stripe_signature(payload: bytes, secret: str) -> str:
    timestamp = int(time.time())
    signed_payload = "%d.%s" % (timestamp, payload.decode("utf-8"))
    signature = stripe.WebhookSignature._compute_signature(signed_payload, secret)
    return f"t={timestamp},v1={signature}"

def test_main():
    client = app.test_client()
    
    # Test valid signature and payment_intent.succeeded
    event_data = {
        "id": "evt_test",
        "object": "event",
        "type": "payment_intent.succeeded",
        "data": {
            "object": {
                "id": "pi_test",
                "object": "payment_intent",
                "amount": 1000,
            }
        }
    }
    payload = json.dumps(event_data).encode("utf-8")
    sig_header = generate_stripe_signature(payload, endpoint_secret)
    
    response = client.post(
        "/webhook",
        data=payload,
        headers={"Stripe-Signature": sig_header, "Content-Type": "application/json"}
    )
    
    assert response.status_code == 200
    assert response.data == b"OK"
    
    # Test missing signature
    response_missing = client.post(
        "/webhook",
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    assert response_missing.status_code == 400
    
    # Test invalid signature
    response_invalid = client.post(
        "/webhook",
        data=payload,
        headers={"Stripe-Signature": "t=123,v1=invalid", "Content-Type": "application/json"}
    )
    assert response_invalid.status_code == 400

if __name__ == "__main__":
    test_main()
    print("Tests passed.")
