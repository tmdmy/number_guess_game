# main.py

task = []

def show_manue():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    
def add_task():
    task_name = input("Enter the task name: ")
    task.append(task_name)
    print(f"Task '{task_name}' added successfully.")

def show_tasks():
    if not task:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, t in enumerate(task, start=1):
            print(f"{i}. {t}")  

def main():
    while True:
        show_manue()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
