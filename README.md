# <img src="https://www.guerrillamail.com/favicon.ico" width="28" style="vertical-align:middle;" /> guerrilla_mail.py

> Web-API for [Guerrilla Mail](https://www.guerrillamail.com) to create and manage disposable temporary email addresses and read incoming emails

## Quick Start
```python
from guerrilla_mail import GuerrillaMail

mail = GuerrillaMail()

# Get a temporary email address
email = mail.get_email_address()
print(email["email_addr"])  # e.g. randomname@guerrillamail.com
```

---

## Constructor Options
```python
GuerrillaMail(
    language="en"  # response language
)
```

---

## Methods

| Method | Description |
|--------|-------------|
| `get_email_address()` | Generate a new temporary email address |
| `set_email_user(email_user)` | Set a custom username for the email address |
| `check_email(seq)` | Check for new emails since a sequence number |
| `get_email_list(seq, offset)` | Get a paginated list of received emails |
| `fetch_email(email_id)` | Get the full content of an email by ID |
| `delete_email(email_id)` | Delete an email by ID |

---

## Examples
```python
mail = GuerrillaMail()

# Get a random address
address = mail.get_email_address()
print(address["email_addr"])

# Set a custom username
mail.set_email_user("myusername")

# Check for new emails
new_emails = mail.check_email()

# List all emails
emails = mail.get_email_list()

# Read a specific email
email = mail.fetch_email(email_id=12345)
print(email["mail_body"])

# Delete an email
mail.delete_email(email_id=12345)
```
