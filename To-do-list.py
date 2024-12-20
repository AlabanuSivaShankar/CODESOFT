

def display_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
        return
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['name']} [{status}]")

def add_task(tasks):
    task_name = input("\nEnter the task name: ").strip()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added successfully!")
    else:
        print("Task name cannot be empty.")

def update_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_name = input("Enter the new task name: ").strip()
            if new_name:
                tasks[task_index]["name"] = new_name
                print("Task updated successfully!")
            else:
                print("Task name cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task['name']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print(f"Task '{tasks[task_index]['name']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_completed(tasks)
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
