from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/public/data')
def public_data():
    return jsonify({"data": "This is public"})

@app.route('/protected/data')
def protected_data():
    # TODO: This should only be accessible to authenticated users
    return jsonify({"data": "This should be protected"})

if __name__ == '__main__':
    app.run(debug=True)
