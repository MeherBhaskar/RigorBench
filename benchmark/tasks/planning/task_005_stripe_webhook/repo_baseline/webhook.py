import os
import stripe
from flask import Flask, request

app = Flask(__name__)

# Usually set in environment variables
stripe.api_key = os.environ.get("STRIPE_API_KEY", "sk_test_dummy")
endpoint_secret = os.environ.get("STRIPE_WEBHOOK_SECRET", "whsec_dummy")

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    if not sig_header:
        return 'Missing Stripe-Signature header', 400

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
        # Process payment_intent.succeeded here
        print(f"Payment intent {payment_intent.id} succeeded.")
    else:
        # Unexpected event type
        print(f"Unhandled event type: {event['type']}")

    return 'OK', 200