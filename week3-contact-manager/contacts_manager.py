import json
import os

FILE_NAME = "contacts_data.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)




def valid_phone(phone):
    phone = phone.replace(" ", "").replace("-", "")
    return phone.isdigit() and 10 <= len(phone) <= 15


def valid_email(email):
    return "@" in email and "." in email




def add_contact(contacts):
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    if not valid_phone(phone):
        print("Invalid phone number.")
        return

    email = input("Enter email (optional): ").strip()
    if email and not valid_email(email):
        print("Invalid email.")
        return

    group = input("Enter group (Friends/Work/Family): ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "group": group
    }

    save_contacts(contacts)
    print("Contact added successfully.")


def search_contact(contacts):
    keyword = input("Search name: ").lower()
    found = False

    for name, info in contacts.items():
        if keyword in name.lower():
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Group: {info['group']}")
            found = True

    if not found:
        print("No matching contact found.")


def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("New phone (leave blank to keep old): ").strip()
    email = input("New email (leave blank to keep old): ").strip()

    if phone:
        if valid_phone(phone):
            contacts[name]["phone"] = phone
        else:
            print("Invalid phone. Update cancelled.")
            return

    if email:
        if valid_email(email):
            contacts[name]["email"] = email
        else:
            print("Invalid email. Update cancelled.")
            return

    save_contacts(contacts)
    print("Contact updated.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    confirm = input("Are you sure? (y/n): ").lower()
    if confirm == "y":
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted.")


def view_all(contacts):
    if not contacts:
        print("No contacts available.")
        return

    for name, info in contacts.items():
        print("\n--------------------")
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Group: {info['group']}")



def menu():
    contacts = load_contacts()

    while True:
        print("\nCONTACT MANAGEMENT SYSTEM")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            view_all(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


menu()
