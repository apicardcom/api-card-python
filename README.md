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
python examples/auth.py
```

> 🔐 Set your API key in each script using:  
> `Authorization: Bearer YOUR_API_KEY`

---

## 📦 What's Inside?

Production-ready examples using the official base URL:  
`https://api-card.com/api/v1`

- ✅ Clean `requests` usage
- 🧪 Test mode support
- 💬 Human-readable responses
- 🛡️ Idempotency key usage for safe POST/PUT

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

## 💡 Code Style

Each script includes:
- `requests` with proper headers
- Base URL and endpoint clarity
- `Authorization: Bearer YOUR_API_KEY`
- Example JSON responses in comments
- Clean error handling (minimal but real)

---

## 🧰 Requirements

- Python 3.7+
- `requests` (standard lib)
- `uuid`, `json` (for idempotency)

Install with:

```bash
pip install requests
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
