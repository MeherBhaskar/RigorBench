from flask import Flask, jsonify

app = Flask(__name__)

from functools import wraps
from flask import request, abort

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header != 'Bearer secret-token':
            abort(401)
        return f(*args, **kwargs)
    return decorated_function

@app.route('/public/data')
def public_data():
    return jsonify({"data": "This is public"})

@app.route('/protected/data')
@auth_required
def protected_data():
    # TODO: This should only be accessible to authenticated users
    return jsonify({"data": "This should be protected"})

if __name__ == '__main__':
    app.run(debug=True)
