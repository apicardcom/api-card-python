# Placeholder for API-Card Python Example: list_internal_txns.py
import requests

BASE_URL = "https://api-card.com/api/v1"
ENDPOINT = "/transactions/internal"

def list_internal_transactions(api_key, params=None):
    url = f"{BASE_URL}{ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
