from flask import Flask
from src.utils.data_fetcher import fetch_data  # Import the utility function
from src.api.endpoints import setup_routes

# Initialize the Flask app
app = Flask(__name__)

# Example usage of fetch_data in main.py (just for demonstration)
def test_fetch():
    url = "https://api.example.com/data"
    response = fetch_data(url)
    if response:
        print("Fetched data:", response)
    else:
        print("Failed to fetch data.")

# Set up routes
setup_routes(app)

# Main entry point
if __name__ == "__main__":
    test_fetch()  # Call test_fetch before starting the server
    app.run(debug=True, host="0.0.0.0", port=5000)
