# 🐍 API-Card Python SDK

[![License](https://img.shields.io/github/license/apicardcom/api-card-python?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg?style=flat-square)](https://www.python.org/)
[![Postman Docs](https://img.shields.io/badge/docs-Postman-orange?logo=postman&style=flat-square)](https://documenter.getpostman.com/view/38099920/2sAXjNYWSK)
[![Telegram](https://img.shields.io/badge/support-Telegram-blue?logo=telegram&style=flat-square)](https://t.me/api_card_support)

A simple Python wrapper around the [api-card.com](https://api-card.com) API using `requests`.  
Useful for issuing virtual cards, querying transactions, and managing your account securely via code.

---

## 🚀 Quickstart

```bash
git clone https://github.com/apicardcom/api-card-python.git
cd api-card-python
pip install -r requirements.txt

# Set up your API key in .env file
echo "API_CARD_API_KEY=your_api_key_here" > .env

# Run the basic test script
python test-basic.py
```

> 🔐 API keys are loaded from a `.env` file in the project root or can be provided directly to each function.

Example test output:
```
API-CARD PYTHON SDK - BASIC TEST

1. Testing Authentication...
✓ Authentication successful!

2. Getting Account Balance...
✓ Success!
   Balance USD: $404.59
   Total Replenishment USD: $16261.25
   Total Spend USD: $3816
   Balance Cards: 14
   Total Cards: 57
   Active Cards: 3
   Active Cards Available Balance USD: $45.07
   Is New Cards Available: True
   Top Up Required Amount: $0

3. Checking Available Bins...
✓ Found 36 bin(s)
✓ You have access to 2 bin(s)
   Bin 1: MasterCard 537100 (Accessible)
   Bin 2: MasterCard 52489792 (Accessible)

Test completed in 3.00 seconds

✨ You're all set to use the API-Card Python SDK!
```

---

## 📦 What's Inside?

Production-ready examples using the official base URL:  
`https://api-card.com/api/v1`

- ✅ Clean `requests` usage
- 🧪 Test mode support
- 💬 Human-readable responses
- 🛡️ Idempotency key usage for safe POST/PUT
- 🔄 Environment variable support (.env)

---

## 🧩 Examples by Endpoint

### 🔐 Authentication
| File       | Method | Description         |
|------------|--------|---------------------|
| `auth.py`  | GET    | Test API key        |

### 💼 Account API
| File             | Method | Description         |
|------------------|--------|---------------------|
| `get_balance.py` | GET    | Get account balance |
| `get_bins.py`    | GET    | Get BINs list       |

### 💳 Card Management
| File                        | Method | Description                   |
|-----------------------------|--------|-------------------------------|
| `list_cards.py`             | GET    | List all cards                |
| `get_card.py`               | GET    | Get specific card             |
| `generate_card.py`          | POST   | Create new card               |
| `generate_card_address.py`  | POST   | Create card + auto address    |
| `update_card_address.py`    | PUT    | Update card name/address      |
| `update_card_limit.py`      | PUT    | Update card spending limit    |
| `update_card_status.py`     | PUT    | Activate / deactivate card    |
| `update_card_closing.py`    | PUT    | Set card closing date         |

### 📊 Transactions API
| File                        | Method | Description                      |
|-----------------------------|--------|----------------------------------|
| `list_transactions.py`      | GET    | All account transactions         |
| `list_card_transactions.py` | GET    | Specific card transactions       |
| `list_internal_txns.py`     | GET    | Internal balance movements       |

---

## 🧪 Testing

To quickly test your API setup, run:

```bash
python test-basic.py
```

This script will:
1. Verify your API key authentication
2. Display your current account balance details
3. Show available BINs and which ones you have access to

All example scripts can also be run individually:

```bash
python examples/get_balance.py
```

---

## 💡 Code Style

Each script includes:
- `requests` with proper headers
- Base URL and endpoint clarity
- API key loaded from environment or passed as parameter
- Example JSON responses in comments
- Clean error handling (minimal but real)

---

## 🧰 Requirements

- Python 3.7+
- `requests`
- `python-dotenv` (for reading .env files)

Install with:

```bash
pip install -r requirements.txt
```

---

## 📄 API Reference

- 🔗 [Full Postman Docs](https://documenter.getpostman.com/view/38099920/2sAXjNYWSK)
- 📘 Base URL: `https://api-card.com/api/v1`

---

## 🤝 Contribute

Have suggestions or new use cases?  
Open a PR, raise an issue, or fork and star ⭐ the repo!

---

## 👥 Community

- [Telegram Support](https://t.me/api_card_support)
- [Website](https://api-card.com)

---

© API-Card.com — All trademarks belong to their respective owners.
