# taskmaster.py

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks):
                status = "Done" if task.completed else "Pending"
                print(f"{i + 1}. [{status}] {task.description} (Priority: {task.priority})")
        else:
            print("No tasks.")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTaskMaster - Command Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            task_manager.add_task(description, priority)
        elif choice == "2":
            index = int(input("Enter task index to complete: ")) - 1
            task_manager.complete_task(index)
        elif choice == "3":
            task_manager.display_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
