import requests

def fetch_data(url, params=None, headers=None):
    """
    Fetches data from the given API URL.

    Args:
        url (str): The API endpoint URL.
        params (dict): Query parameters for the API request (optional).
        headers (dict): Headers for the API request (optional).

    Returns:
        dict: The JSON response from the API if successful.
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
