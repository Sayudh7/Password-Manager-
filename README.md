# 🔐 Password Manager

A simple terminal-based password manager written in Python. Store, retrieve, and manage your credentials locally — no internet required.

---

## Features

- Add passwords manually or auto-generate secure ones
- View all saved accounts at a glance
- Search for a specific account's credentials
- Delete accounts you no longer need
- Stores data locally in a `passwords.json` file

---

## Requirements

- Python 3.x (no external libraries needed — uses only the standard library)

---

## Getting Started

### 1. Clone or download the script


### 2. Run the script

```bash
python password_manager.py
```

---

## Usage

When you run the script, you'll see a menu:

```
====== PASSWORD MANAGER ======
1. Add Password
2. View Accounts
3. Search Password
4. Delete Account
5. Exit
```

### Option 1 — Add Password
Enter the website/app name and your username. You can either let the tool generate a strong random password or enter your own securely (input is hidden).

### Option 2 — View Accounts
Lists all websites/apps you've saved credentials for.

### Option 3 — Search Password
Enter a website/app name to retrieve its stored username and password.

### Option 4 — Delete Account
Removes a saved account entry permanently.

### Option 5 — Exit
Closes the program.

---

## Data Storage

All credentials are saved locally in a `passwords.json` file in the same directory as the script. Example structure:

```json
{
    "github.com": {
        "username": "johndoe",
        "password": "G#k2!mXpQ9wZ"
    }
}
```

> ⚠️ **Security Notice:** Passwords are stored in **plain text**. Do not use this tool for highly sensitive credentials without adding encryption. Avoid committing `passwords.json` to version control — add it to your `.gitignore`.

---

## .gitignore recommendation

```
passwords.json
```

---

## License

MIT License — free to use and modify.
