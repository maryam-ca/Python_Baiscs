import json
import os

FILENAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added!")

# Search contact
def search_contact(contacts):
    keyword = input("Search by name, phone, or email: ").lower()
    found = False
    for name, info in contacts.items():
        if keyword in name.lower() or keyword in info["phone"] or keyword in info["email"].lower():
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            found = True
    if not found:
        print("No contact found.")

# Main program loop
def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Search App ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
