import json
import os
import random
import string
from getpass import getpass

FILE_NAME = "passwords.json"


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


menu()