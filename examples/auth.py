"""
API-Card Authentication Example
Tests the API key against the auth endpoint to verify it's valid
"""
import os
import sys
import requests
from dotenv import load_dotenv

# Add parent directory to path to find .env in root folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment variables from .env file in project root
load_dotenv()

BASE_URL = "https://api-card.com/api/v1"
ENDPOINT = "/test-auth"

def authenticate(api_key=None):
    """
    Test authentication with API-Card using API key
    
    Args:
        api_key (str, optional): Your API key from dashboard.api-card.com
                                If not provided, will look for API_CARD_API_KEY in environment
        
    Returns:
        dict: JSON response with the following structure:
            - Status (int): Status code (0 for success)
            - Good (bool): True if authentication successful, False otherwise
            - Message (str, optional): Error message if authentication failed
    """
    # Use provided API key or get from environment
    api_key = api_key or os.getenv("API_CARD_API_KEY")
    
    if not api_key:
        return {
            "Status": 5, 
            "Good": False, 
            "Message": "No API key provided. Set API_CARD_API_KEY in .env file or pass as parameter."
        }
    
    url = f"{BASE_URL}{ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError if not 2xx
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            return {"Status": 1, "Good": False, "Message": "Authentication failed - Invalid API key"}
        else:
            return {"Status": 2, "Good": False, "Message": f"HTTP Error: {e}"}
    except requests.exceptions.RequestException as e:
        return {"Status": 3, "Good": False, "Message": f"Request Error: {e}"}
    except Exception as e:
        return {"Status": 4, "Good": False, "Message": f"Unexpected Error: {e}"}

# For direct testing
if __name__ == "__main__":
    print(f"Testing API authentication to {BASE_URL}{ENDPOINT}...")
    result = authenticate()
    print(f"Response: {result}")
    
    if result.get("Good", False):
        print("Authentication successful!")
    else:
        print(f"Authentication failed: {result.get('Message', 'Unknown error')}")
