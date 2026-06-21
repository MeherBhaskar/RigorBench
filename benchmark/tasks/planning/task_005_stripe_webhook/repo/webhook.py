from flask import Flask, request
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    # TODO: Verify signature and process payment_intent.succeeded
    return 'OK', 200