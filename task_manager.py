import argparse

class Task:
    def __init__(self,task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"id:{self.id}, title:{self.title} is completed: {self.completed}"

class TaskManager(Task):

    def __init__(self):
        self.tasks = {}

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id,title, description)
        self.tasks[task_id] = new_task

    def remove_task(self, id):
        if id in self.tasks:
            del self.tasks[id]
        else:
            return "id not found"

    def mark_task_completed(self, id):
        task = self.tasks.get(id)
        if task:
            task.mark_as_completed()
            return task
        else:
            return "Task not found"

    def list_tasks(self):
        for task_id, task in self.tasks.items():
            print(f"id:{task_id}, title:{task.title}, is_completed: {task.completed}")

    def find_task(self, id):
        if id in self.tasks:
            return self.tasks[id]
        else:
            return "Task not found"

def main():
    parser = argparse.ArgumentParser(description="Task Manager")

    args = parser.parse_args()

    task_manager = TaskManager()

    while True:
        command = input("Enter command (add/remove/completed/list/quit): ").lower()

        if command == "add":
            title= input("title: ")
            description =input("description: ")
            task_manager.add_task(title, description)
        elif command == "remove":
            id= int(input("Id: "))
            task_manager.remove_task(id)
        elif command == "completed":
            id= int(input("Id: "))
            task_manager.mark_task_completed(id)
        elif command == "list":
            task_manager.list_tasks()
        elif command == "quit":
            break

if __name__ == "__main__":
    main()

