import json
import os

FILE_NAME = "inventory.json"

# Load inventory from file
def load_inventory():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save inventory to file
def save_inventory(inventory):
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file)

# Add product
def add_product(inventory):
    name = input("Enter product name: ").strip()
    if name in inventory:
        print("Product already exists. Use update option instead.")
    else:
        quantity = int(input("Enter quantity: "))
        inventory[name] = quantity
        print("Product added.")

# Remove product
def remove_product(inventory):
    name = input("Enter product name to remove: ").strip()
    if name in inventory:
        del inventory[name]
        print("Product removed.")
    else:
        print("Product not found.")

# Update product quantity
def update_quantity(inventory):
    name = input("Enter product name: ").strip()
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        print("Quantity updated.")
    else:
        print("Product not found.")

# View inventory and out-of-stock products
def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nCurrent Inventory:")
    for product, qty in inventory.items():
        print(f"{product}: {qty} units")

    out_of_stock = {name for name, qty in inventory.items() if qty == 0}
    if out_of_stock:
        print("\nOut of Stock Items:", ', '.join(out_of_stock))
    else:
        print("\nAll items in stock.")

# Main menu
def main():
    inventory = load_inventory()

    while True:
        print("\n--- Inventory Management ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Quantity")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            remove_product(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            view_inventory(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Inventory saved. Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

main()
