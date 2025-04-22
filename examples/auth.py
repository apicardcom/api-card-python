# Placeholder for API-Card Python Example: auth.py
import requests

BASE_URL = "https://api-card.com/api/v1"
ENDPOINT = "/test-auth"

def authenticate(api_key):
    url = f"{BASE_URL}{ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises HTTPError if not 2xx
    return response.json()
