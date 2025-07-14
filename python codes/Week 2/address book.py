import os
import ast

# File to store contact data
FILENAME = "address_book.txt"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return ast.literal_eval(file.read())
            except:
                return {}
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        file.write(str(contacts))

# Display all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"  Phone: {info['phone']}")
            print(f"  Email: {info['email']}")
            print("-" * 20)

# Add or update a contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact saved!")

# Search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Found: {name}")
        print(f"  Phone: {contacts[name]['phone']}")
        print(f"  Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n--- CLI Address Book ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
