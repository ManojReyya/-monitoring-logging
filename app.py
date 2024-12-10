import logging
from flask import Flask, jsonify

# Configure logging to write to a file
logging.basicConfig(
    filename='/var/log/app.log',  # Log file location
    level=logging.INFO,           # Set the log level
    format='%(asctime)s %(levelname)s: %(message)s',  # Include timestamp and log level
)

app = Flask(__name__)

@app.route('/')
def home():
    app.logger.info('Home route accessed')
    return jsonify({"message": "Welcome to the Flask App!"})

if __name__ == '__main__':
    app.logger.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000)

