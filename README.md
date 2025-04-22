# 🐍 API-Card Python Examples

This repo contains simple, ready-to-run Python examples using `requests` to interact with [API-Card.com](https://api-card.com).  
Perfect for developers building automations, bots, or fintech flows around virtual card issuance and payments.

📄 Official Docs: [Postman](https://documenter.getpostman.com/view/38099920/2sAXjNYWSK)  
💬 Telegram Support: [@api_card_support](https://t.me/api_card_support)

---

## 🚀 Quickstart

```bash
pip install requests
python examples/auth.py
```

---

## 🧩 Endpoints Covered

### 🔐 Authentication API
| File                  | Method | Description             |
|-----------------------|--------|-------------------------|
| `auth.py`             | GET    | Test Authentication     |

### 💼 Account API
| File                  | Method | Description             |
|-----------------------|--------|-------------------------|
| `get_balance.py`      | GET    | Get Account Balance     |
| `get_bins.py`         | GET    | Get BINS                |

### 💳 Cards API
| File                          | Method | Description                     |
|-------------------------------|--------|---------------------------------|
| `list_cards.py`               | GET    | List Cards                      |
| `get_card.py`                 | GET    | Get Card Details                |
| `generate_card.py`           | POST   | Generate New Card               |
| `generate_card_address.py`   | POST   | Generate Card + Address         |
| `update_card_address.py`     | PUT    | Change Card Address and Name    |
| `update_card_limit.py`       | PUT    | Change Card Limit               |
| `update_card_status.py`      | PUT    | Change Card Status              |
| `update_card_closing.py`     | PUT    | Change Card Closing Date        |

### 📊 Transactions API
| File                          | Method | Description                     |
|-------------------------------|--------|---------------------------------|
| `list_transactions.py`        | GET    | List All Transactions           |
| `list_card_transactions.py`   | GET    | List Card-Specific Transactions |
| `list_internal_txns.py`       | GET    | List Internal Transactions      |

---

## 💡 Usage Format

Each file contains:
- `requests`-based example
- Real endpoint URL
- Authorization format (`Bearer YOUR_API_KEY`)
- Clean, ready-to-copy usage

---

## ⭐ Contribute

Want to help improve examples or build something cool on top?  
PRs welcome! Or just star the repo to support the project.

---

## 👥 Connect with Us

- API Support: [@api_card_support](https://t.me/api_card_support)
- Website: [api-card.com](https://api-card.com)
