# Discord Group Cleaner 🧹

A simple Python script that automatically leaves inactive Discord Group DMs based on how long ago the last message was sent.

---

## ⚠️ Disclaimer

This script uses a **user token**, which technically violates Discord's Terms of Service. Use it at your own risk. The author is not responsible for any consequences. It is recommended to run it **manually and occasionally**, not as an automated background process.

---

## 🚀 How it works

1. Fetches all your Discord Group DMs
2. Checks the timestamp of the last message in each group
3. If the last message is older than `days_since_last_msg` days, it leaves the group

---

## 📋 Requirements

- Python 3.x
- `requests`
- `python-dotenv`

Install dependencies:

```bash
pip install requests python-dotenv
```

---

## ⚙️ Setup

1. Clone the repository
2. Create a `.env` file based on `.env.example`
3. Add your Discord user token to the `.env` file

### How to get your Discord token

1. Open Discord in your **browser** (discord.com)
2. Open **DevTools** (F12)
3. Go to the **Network** tab
4. Reload the page or perform any action
5. Look for any request to `discord.com/api`
6. In the request headers find **`Authorization`** — that value is your token

> ⚠️ Never share your token with anyone. Treat it like a password.

---

## 🔧 Configuration

In `cleaner.py` you will find this variable:

```python
days_since_last_msg = 1
```

Change this value to however many days you want to have passed since the last message for the group to be removed. For example, set it to `3` if you want to leave groups with no activity in the last 3 days.

---

## ▶️ Usage

```bash
python cleaner.py
```

The script will print which groups it is leaving and a final summary of how many groups were cleaned up.

---

## 📁 Project structure

```
discord-group-cleaner/
├── .gitignore
├── .env.example
├── README.md
└── cleaner.py
```
