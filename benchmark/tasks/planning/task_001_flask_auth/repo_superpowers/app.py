from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if auth == 'Bearer secret-token':
            return f(*args, **kwargs)
        return jsonify({"message": "Unauthorized"}), 401
    return decorated

@app.route('/public/data')
def public_data():
    return jsonify({"data": "This is public"})

@app.route('/protected/data')
@require_auth
def protected_data():
    # TODO: This should only be accessible to authenticated users
    return jsonify({"data": "This should be protected"})

if __name__ == '__main__':
    app.run(debug=True)
