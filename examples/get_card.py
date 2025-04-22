# Placeholder for API-Card Python Example: get_card.py
import requests

BASE_URL = "https://api-card.com/api/v1"

def get_card(api_key, card_id):
    url = f"{BASE_URL}/cards/{card_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
