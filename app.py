import logging
from flask import Flask, jsonify

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def home():
    app.logger.info('Home route accessed')
    return jsonify({"message": "Welcome to the Flask App!"})

if __name__ == '__main__':
    app.logger.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000)
