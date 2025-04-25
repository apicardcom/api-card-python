# Placeholder for API-Card Python Example: generate_card_address.py
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
ENDPOINT = "/cards/{card_id}/address"

def generate_card_address(card_id, address_data, api_key=None):
    # Use provided API key or get from environment
    api_key = api_key or os.getenv("API_CARD_API_KEY")
    
    if not api_key:
        raise ValueError("No API key provided. Set API_CARD_API_KEY in .env file or pass as parameter.")
    
    if not address_data:
        raise ValueError("Address data is required")
        
    url = f"{BASE_URL}{ENDPOINT.format(card_id=card_id)}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Idempotency-Key": str(uuid.uuid4())
    }

    response = requests.post(url, headers=headers, json=address_data)
    response.raise_for_status()
    return response.json()

# For direct testing
if __name__ == "__main__":
    try:
        # Replace with an actual card ID and address data for testing
        card_id = "example_card_id"
        address_data = {"address1": "123 Test St", "city": "Test City", "state": "CA", "postal_code": "12345"}
        result = generate_card_address(card_id, address_data)
        print(f"Card address generated: {result}")
    except Exception as e:
        print(f"Error: {e}")
