# To-Do List Application
# This application allows users to manage a simple to-do list.

# List to store tasks
list_of_tasks = []

# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Function to view tasks
def view_tasks():
    try:
        if not list_of_tasks:
            raise ValueError("No tasks available.")
        print("\nYour Tasks:")
        for index, task in enumerate(list_of_tasks, start=1):  # Index facilitates deleting tasks later
            print(f"{index}. {task}")
    except ValueError as e:
        print(e)
    finally:
        print("Finished viewing tasks.")

# Function to add a task
def add_task():
    task = input("Enter the task to add: ").strip()  # Remove leading/trailing whitespace

    if task:
        list_of_tasks.append(task)
        print(f'Task "{task}" added.')
    else:
        print("No task entered. Please try again.")

# Function to remove a task
def remove_task():
    if not list_of_tasks:
        print("No tasks available to remove.")
        return

    try:
        view_tasks()  # Show current tasks to the user
        task_index = int(input("Enter the task number to remove: ")) - 1

        if 0 <= task_index < len(list_of_tasks):
            removed_task = list_of_tasks.pop(task_index)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main loop
def main():
    print("Welcome to the To-Do List Application!")

    while True:
        display_menu()

        try:
            choice = int(input("Choose an option (1-4): "))

            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                remove_task()
            elif choice == 4:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        finally:
            print("Returning to the main menu.")

# Run the application
if __name__ == "__main__":
    main()
