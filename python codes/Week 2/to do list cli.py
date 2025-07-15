import os

TASK_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Add a new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f" Removed: {removed}")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

main()
