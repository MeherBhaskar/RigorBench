import datetime
from functools import wraps
from flask import Flask, jsonify, request, make_response
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key-for-testing'

# User model (in-memory)
users = {}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
            else:
                token = auth_header
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
            
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users.get(data['username'])
            if not current_user:
                raise Exception("User not found")
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401
            
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400
        
    username = data['username']
    password = data['password']
    
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
        
    hashed_password = generate_password_hash(password)
    users[username] = {'username': username, 'password': hashed_password}
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
        
    user = users.get(data['username'])
    
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
        
    if check_password_hash(user['password'], data['password']):
        token = jwt.encode({'username': user['username'], 'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})
        
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

@app.route('/public/data')
def public_data():
    return jsonify({"data": "This is public"})

@app.route('/protected/data')
@token_required
def protected_data(current_user):
    return jsonify({"data": "This should be protected", "user": current_user['username']})

if __name__ == '__main__':
    app.run(debug=True)
