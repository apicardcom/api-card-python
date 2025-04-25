# Placeholder for API-Card Python Example: update_card_limit.py
import os
import sys
import requests
import uuid
from dotenv import load_dotenv

# Add parent directory to path to find .env in root folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables from .env file in project root
load_dotenv()

BASE_URL = "https://api-card.com/api/v1"
ENDPOINT = "/cards/{card_id}"

def update_card_limit(card_id, limit_data, api_key=None):
    # Use provided API key or get from environment
    api_key = api_key or os.getenv("API_CARD_API_KEY")
    
    if not api_key:
        raise ValueError("No API key provided. Set API_CARD_API_KEY in .env file or pass as parameter.")
        
    url = f"{BASE_URL}{ENDPOINT.format(card_id=card_id)}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Idempotency-Key": str(uuid.uuid4())
    }

    response = requests.put(url, headers=headers, json=limit_data)
    print("Response content:", response.text)  # Debug print
    response.raise_for_status()
    return response.json()

# For direct testing
if __name__ == "__main__":
    try:
        card_id = "example_card_id"  # Replace with real card ID

        limit_data = {
            "Type": "limit",
            "Limit": 100.00  # Must be a float value
        }

        print(f"Updating limit for card {card_id} to {limit_data['Limit']}...")
        result = update_card_limit(card_id, limit_data)
        print("Card limit updated successfully:")
        print(result)

    except Exception as e:
        print(f"Error: {e}")
