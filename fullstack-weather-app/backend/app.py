from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "Backend Running"
    })

@app.route('/weather')
def weather():
    return jsonify({
        "city": "Nagpur",
        "temperature": "32°C",
        "condition": "Sunny"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)