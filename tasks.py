tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("✅ Task added!\n")

def view_tasks():
    if not tasks:
        print("No tasks found.\n")
    else:
        print("📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Removed: {removed}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def menu():
    while True:
        print("📝 To-Do List")
        print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Choose: ")

        if choice == '1': add_task()
        elif choice == '2': view_tasks()
        elif choice == '3': delete_task()
        elif choice == '4': break
        else: print("Invalid option\n")

if __name__ == "__main__":
    menu()
