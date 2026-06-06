import json
import os
import random
import string
from getpass import getpass
import hashlib
import sys

FILE_NAME = "passwords.json"
MASTER_FILE = "master.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def setup_master_password():

    print("=== First Time Setup ===")

    while True:

        password = getpass("Create Master Password: ")
        confirm = getpass("Confirm Master Password: ")

        if password == confirm:

            data = {
                "master_password": hash_password(password)
            }

            with open(MASTER_FILE, "w") as file:
                json.dump(data, file)

            print("Master Password Created.\n")
            break

        else:
            print("Passwords do not match.\n")


def verify_master_password():

    if not os.path.exists(MASTER_FILE):
        setup_master_password()

    with open(MASTER_FILE, "r") as file:
        data = json.load(file)

    attempts = 3

    while attempts > 0:

        password = getpass("Enter Master Password: ")

        if hash_password(password) == data["master_password"]:
            print("Access Granted\n")
            return

        attempts -= 1
        print("Wrong Password")

    print("Too many attempts.")
    sys.exit()

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    return password


def add_password(data):
    website = input("Website/App: ").strip()
    username = input("Username/Email: ").strip()

    choice = input("Generate password? (y/n): ").lower()

    if choice == "y":
        password = generate_password()
        print("Generated Password:", password)
    else:
        password = getpass("Enter Password: ")

    data[website] = {
        "username": username,
        "password": password
    }

    save_data(data)
    print("Password Saved Successfully.\n")


def view_accounts(data):
    if not data:
        print("No accounts saved.\n")
        return

    print("\nSaved Accounts:")
    for site in data:
        print("-", site)
    print()


def search_password(data):
    website = input("Enter Website/App Name: ")

    if website in data:
        print("\nFound:")
        print("Username:", data[website]["username"])
        print("Password:", data[website]["password"])
    else:
        print("Account not found.")

    print()


def delete_account(data):
    website = input("Enter account to delete: ")

    if website in data:
        del data[website]
        save_data(data)
        print("Deleted Successfully.\n")
    else:
        print("Account not found.\n")


def menu():
    data = load_data()

    while True:
        print("====== PASSWORD MANAGER ======")
        print("1. Add Password")
        print("2. View Accounts")
        print("3. Search Password")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_password(data)

        elif choice == "2":
            view_accounts(data)

        elif choice == "3":
            search_password(data)

        elif choice == "4":
            delete_account(data)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid Option\n")


verify_master_password()
menu()
