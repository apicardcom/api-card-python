# Placeholder for API-Card Python Example: generate_card_address.py
import requests
import uuid

BASE_URL = "https://api-card.com/api/v1"
ENDPOINT = "/cards"

def generate_card_with_address(api_key, card_data):
    url = f"{BASE_URL}{ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Idempotency-Key": str(uuid.uuid4())
    }

    response = requests.post(url, headers=headers, json=card_data)
    response.raise_for_status()
    return response.json()
