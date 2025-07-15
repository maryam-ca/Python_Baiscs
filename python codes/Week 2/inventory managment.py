import json
import os

INVENTORY_FILE = "inventory.json"

# Load inventory from file
def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    return {}

# Save inventory to file
def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file)

# Get out-of-stock items
def get_out_of_stock(inventory):
    return {name for name, qty in inventory.items() if qty == 0}

# Add product
def add_product(inventory):
    name = input("Enter product name: ")
    if name in inventory:
        print("Product already exists.")
    else:
        qty = int(input("Enter quantity: "))
        inventory[name] = qty
        print("Product added.")

# Remove product
def remove_product(inventory):
    name = input("Enter product name to remove: ")
    if name in inventory:
        del inventory[name]
        print("Product removed.")
    else:
        print("Product not found.")

# Update quantity
def update_quantity(inventory):
    name = input("Enter product name: ")
    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name] = qty
        print("Quantity updated.")
    else:
        print("Product not found.")

# Check stock
def check_stock(inventory):
    print("\nCurrent Inventory:")
    for name, qty in inventory.items():
        print(f"{name}: {qty} units")
    print("\nOut of Stock Items:", get_out_of_stock(inventory))

# Main menu
def main():
    inventory = load_inventory()
    while True:
        print("\n--- Inventory Management ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Quantity")
        print("4. Check Stock")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_product(inventory)
            save_inventory(inventory)
        elif choice == "2":
            remove_product(inventory)
            save_inventory(inventory)
        elif choice == "3":
            update_quantity(inventory)
            save_inventory(inventory)
        elif choice == "4":
            check_stock(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Exiting. Inventory saved.")
            break
        else:
            print("Invalid option. Try again.")

main()
