from flask import Flask
from src.api.endpoints import setup_routes
import src.config as config

# Initialize the Flask app
app = Flask(__name__)

# Set up routes
setup_routes(app)

# Main entry point
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
