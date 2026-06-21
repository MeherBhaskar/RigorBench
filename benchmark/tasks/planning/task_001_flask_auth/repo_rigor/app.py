from flask import Flask, jsonify, request
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key-for-testing'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
  
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except Exception:
            return jsonify({'message': 'Token is invalid!'}), 401
            
        return f(*args, **kwargs)
  
    return decorated

@app.route('/login', methods=['POST'])
def login():
    token = jwt.encode({
        'user': 'testuser',
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    
    return jsonify({'token': token})

@app.route('/public/data')
def public_data():
    return jsonify({"data": "This is public"})

@app.route('/protected/data')
@token_required
def protected_data():
    # TODO: This should only be accessible to authenticated users
    return jsonify({"data": "This should be protected"})

if __name__ == '__main__':
    app.run(debug=True)
