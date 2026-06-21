import os
import stripe
from flask import Flask, request

app = Flask(__name__)

endpoint_secret = os.environ.get('STRIPE_ENDPOINT_SECRET', 'whsec_test_secret')
stripe.api_key = os.environ.get('STRIPE_API_KEY', 'sk_test_123')

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    if not sig_header:
        return 'Missing signature', 400

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return 'Invalid signature', 400

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        print(f"Payment for {payment_intent.get('amount')} succeeded")
    else:
        print(f"Unhandled event type {event['type']}")

    return 'OK', 200

if __name__ == '__main__':
    app.run(port=4242)