def menu():
    print("\n----- To-Do List -----")
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("")
    return choice

def add_task(tasks):
    user_input = input("Enter task: ")
    tasks.append(user_input)
    show_tasks(tasks)
    return tasks

def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return
    try:
        user_input = int(input("Enter task index to delete: "))
        deleted = tasks.pop(user_input)
        print(f"\nDeleted task: {deleted}")
    except (ValueError, IndexError):
        print("Invalid index. Try again.")
    show_tasks(tasks)
    return tasks

def edit_task(tasks):
    if not tasks:
        print("\nNo tasks to edit.")
        return
    try:
        user_input_index = int(input("Enter task index to edit: "))
        new_task = input("Enter new task: ")
        tasks[user_input_index] = new_task
        print("Task updated.")
    except (ValueError, IndexError):
        print("Invalid index. Try again.")
    show_tasks(tasks)
    return tasks

def show_tasks(tasks):
    print("\nYour tasks:")
    for i, task in enumerate(tasks):
        print(f"{i}: {task}")

def main():
    tasks = []
    while True:
        choice = menu()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

main()
    