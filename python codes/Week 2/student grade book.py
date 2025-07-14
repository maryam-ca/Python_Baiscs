import os
import ast

FILENAME = "grade_book.txt"

# Load data from file
def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return ast.literal_eval(file.read())
            except:
                return {}
    return {}

# Save data to file
def save_data(data):
    with open(FILENAME, "w") as file:
        file.write(str(data))

# Add a new student
def add_student(data):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    num_subjects = int(input("How many subjects? "))
    marks = []

    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    data[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")

# View all student records
def view_students(data):
    if not data:
        print("No student records found.")
    else:
        for roll, info in data.items():
            print(f"Roll No: {roll}")
            print(f"  Name : {info['name']}")
            print(f"  Marks: {info['marks']}")
            print(f"  Average: {sum(info['marks']) / len(info['marks']):.2f}")
            print("-" * 25)

# Search a student
def search_student(data):
    roll = input("Enter roll number to search: ")
    if roll in data:
        info = data[roll]
        print(f"Name: {info['name']}")
        print(f"Marks: {info['marks']}")
        print(f"Average: {sum(info['marks']) / len(info['marks']):.2f}")
    else:
        print("Student not found.")

# Delete a student
def delete_student(data):
    roll = input("Enter roll number to delete: ")
    if roll in data:
        del data[roll]
        print("Student record deleted.")
    else:
        print("Student not found.")

# Main program
def main():
    data = load_data()

    while True:
        print("\n📚 Student Grade Book")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
