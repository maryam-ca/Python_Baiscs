# File names
AVAILABLE_FILE = "available.txt"
BORROWED_FILE = "borrowed.txt"

# Load books from file into set
def load_books(filename):
    try:
        with open(filename, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

# Save books to file
def save_books(filename, books):
    with open(filename, "w") as f:
        for book in books:
            f.write(book + "\n")

# Borrow a book
def borrow_book(available, borrowed):
    book = input("Enter book name to borrow: ").strip()
    if book in available:
        available.remove(book)
        borrowed.add(book)
        print(f"'{book}' borrowed successfully.")
    else:
        print("Book not available.")

# Return a book
def return_book(available, borrowed):
    book = input("Enter book name to return: ").strip()
    if book in borrowed:
        borrowed.remove(book)
        available.add(book)
        print(f"'{book}' returned successfully.")
    else:
        print("Book not in borrowed list.")

# View books
def view_books(available, borrowed):
    print("\nAvailable Books:")
    for book in sorted(available):
        print(f"📗 {book}")
    print("\nBorrowed Books:")
    for book in sorted(borrowed):
        print(f"📕 {book}")

# Main function
def main():
    available = load_books(AVAILABLE_FILE)
    borrowed = load_books(BORROWED_FILE)

    while True:
        print("\n--- Library Book Tracker ---")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_books(available, borrowed)
        elif choice == "2":
            borrow_book(available, borrowed)
        elif choice == "3":
            return_book(available, borrowed)
        elif choice == "4":
            save_books(AVAILABLE_FILE, available)
            save_books(BORROWED_FILE, borrowed)
            print("Library data saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()
