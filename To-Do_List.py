import json
import os
# 1. Task class
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed
    def to_dict(self):
        return {"title": self.title, "completed": self.completed}
    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["completed"])
# 2. TaskManager class
class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()
    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
        for idx, task in enumerate(self.tasks):
            status = "\u2714" if task.completed else "\u274C"
            print(f"{idx + 1}. [{status}] {task.title}")
    def mark_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid index.")
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
            print("Task deleted.")
        else:
            print("Invalid index.")
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
# 3. Console interface
def main():
    manager = TaskManager()
    while True:
        print("\nTo-Do List")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            manager.view_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == "3":
            manager.view_tasks()
            idx = int(input("Enter task number to mark complete: ")) - 1
            manager.mark_complete(idx)
        elif choice == "4":
            manager.view_tasks()
            idx = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(idx)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()