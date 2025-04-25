# Placeholder for API-Card Python Example: get_card.py
import os
import sys
import requests
from dotenv import load_dotenv

# Add parent directory to path to find .env in root folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables from .env file in project root
load_dotenv()

BASE_URL = "https://api-card.com/api/v1"
ENDPOINT = "/cards/{card_id}"

def get_card(card_id, api_key=None):
    # Use provided API key or get from environment
    api_key = api_key or os.getenv("API_CARD_API_KEY")
    
    if not api_key:
        raise ValueError("No API key provided. Set API_CARD_API_KEY in .env file or pass as parameter.")

    url = f"{BASE_URL}{ENDPOINT.format(card_id=card_id)}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# For direct testing
if __name__ == "__main__":
    try:
        # Replace with an actual card ID for testing
        card_id = "example_card_id"
        result = get_card(card_id)
        print(f"Card details: {result}")
    except Exception as e:
        print(f"Error: {e}")
