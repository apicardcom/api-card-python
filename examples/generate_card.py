# Placeholder for API-Card Python Example: generate_card.py
import os
import sys
import requests
import uuid
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Add parent directory to path to find .env in root folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables from .env file in project root
load_dotenv()

BASE_URL = "https://api-card.com/api/v1"
ENDPOINT = "/cards"

def generate_card(api_key=None, card_data=None):
    # Use provided API key or get from environment
    api_key = api_key or os.getenv("API_CARD_API_KEY")
    
    if not api_key:
        raise ValueError("No API key provided. Set API_CARD_API_KEY in .env file or pass as parameter.")
    
    if not card_data:
        raise ValueError("Card data is required")
        
    url = f"{BASE_URL}{ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Idempotency-Key": str(uuid.uuid4())
    }

    response = requests.post(url, headers=headers, json=card_data)
    response.raise_for_status()
    return response.json()

# For direct testing
if __name__ == "__main__":
    try:
        # More complete example card data for testing
        example_card_data = {
            "ProgramID": 38,
            "Limit": 1,
            "AddressGenerate": False,
            "FirstName": "test",
            "LastName": "test",
            "Address1": "Main str. 1",
            "City": "New York",
            "State": "NY",
            "Zip": "123456",
            "CountryIso": "US",
            "ExpMonth": "11",
            "ExpYear": "2026",
            "PhoneNumber": "5105551212",
            "Email": "test@test.com",
            "IsTest": True,
            "ClosingDate": (datetime.utcnow() + timedelta(days=30)).isoformat() + "Z"
        }
        
        print("Generating test card...")
        result = generate_card(card_data=example_card_data)
        print(f"Card generated successfully!")
        print(f"Card ID: {result.get('id')}")
        print(f"Card Details: {result}")
        
        # Save card ID for other tests
        if result.get('id'):
            with open("test_card_id.txt", "w") as f:
                f.write(result.get('id'))
            print(f"Card ID saved to test_card_id.txt for further testing")
    except Exception as e:
        print(f"Error: {e}")
