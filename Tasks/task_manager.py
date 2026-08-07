import json
import os
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TASK_FILE = os.path.join(BASE_DIR, "Memory", "tasks.json")


def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)

    return {"tasks": []}


def save_tasks(data):
    with open(TASK_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_task():

    data = load_tasks()

    print()

    title = input("What task shall be added? ")
    project = input("Which creation does this belong to? ")
    priority = input("Priority (Low / Medium / High): ")

    task = {
        "title": title,
        "project": project,
        "priority": priority,
        "status": "Not Started",
        "created": str(date.today()),
        "due_date": "",
        "completed": False,
        "why": "",
        "notes": []
    }

    data["tasks"].append(task)

    save_tasks(data)

    print()
    print("🌿 The task has been added to today's Workshop.")

def view_tasks():
    data = load_tasks()

    tasks = data["tasks"]

    print()

    if not tasks:
        print("🌱 The Workshop Task Board is empty.")
        return
    
    print("╔══════════════════════════════╗")
    print("        🌿 TASK BOARD 🌿")
    print("╚══════════════════════════════╝")

    print()

    for task in tasks:
        print("━━━━━━━━━━━━━━━━━━━━")

        print(f"📌 {task['title']}")
        print(f"🌙 Project: {task.get('project', 'Unassigned')}")
        print(f"⭐ Priority: {task['priority']}")
        print(f"📖 Status: {task['status']}")

        print()

def count_tasks():

    data = load_tasks()

    return len(data["tasks"])

def get_guiding_task():

    data = load_tasks()

    tasks = data["tasks"]

    if not tasks:

        return None
    
    priority_order = {
        "High": 3,
        "Medium": 2,
        "low": 1
    }

    highest = max(
        tasks,
        key=lambda task: priority_order.get(task["priority"], 0)
    )

    return highest