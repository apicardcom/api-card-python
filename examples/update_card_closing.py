# Placeholder for API-Card Python Example: update_card_closing.py
import requests
import uuid

BASE_URL = "https://api-card.com/api/v1"

def update_card_closing_date(api_key, card_id, data):
    url = f"{BASE_URL}/cards/{card_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Idempotency-Key": str(uuid.uuid4())
    }

    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()
