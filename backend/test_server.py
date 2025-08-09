from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "message": "Test server is running!"})

if __name__ == '__main__':
    print("Starting test server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
