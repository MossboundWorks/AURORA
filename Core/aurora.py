import datetime
import json
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARCHIVE_DIR = os.path.join(BASE_DIR, "Archive")
TASK_DIR = os.path.join(BASE_DIR, "Tasks")

sys.path.append(ARCHIVE_DIR)
sys.path.append(TASK_DIR)


from project_manager import view_projects, add_project, show_project
from task_manager import (
    add_task,
    view_tasks,
    count_tasks,
    get_guiding_task
)
from memory_keeper import add_moment, view_memories
from workshop_status import workshop_status
from welcome_system import welcome

CONFIG_FILE = os.path.join(
    BASE_DIR,
    "Config",
    "personality.json"
)


def load_personality():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


personality = load_personality()

current_hour = datetime.datetime.now().hour

MEMORY_FILE = os.path.join(BASE_DIR, "Memory", "memories.json")

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
        
    return {
        "creator": "Moss",
        "projects": [],
        "notes": []
    }

memory = load_memory()

# Aurora Core
# Version 0.2 - The Listening Spark

if current_hour < 12:
    greeting = "The spirits whisper of a new morning in the Workshop."
elif current_hour < 18:
    greeting = "The Workshop hums beneath the afternoon light."
else:
    greeting = "The lanterns of the Workshop glow as evening arrives."

print(greeting)
welcome()


task_count = count_tasks()

print()

if task_count == 0:
    print("🌱 The Workshop is peaceful today.")
elif task_count == 1:
    print("🌿 There is 1 task waiting in the Workshop.")
else:
    print(f"🌿 There are {task_count} tasks waiting in the Workshop.")

guiding_task = get_guiding_task()

if guiding_task:
    print()
    print("✨ Your Guiding Lantern:")
    print(f"📌 {guiding_task['title']}")
    print(f"🌙 Project: {guiding_task['project']}")
    print(f"⭐ Priority: {guiding_task['priority']}")


print()

command = input("Awaiting your command, Moss:")

print()

if command.lower() == "hello":
    print("Greetings, Moss. The Workshop is ready.")

elif command.lower() == "status":
    print("Aurora Core: Online")
    print("Archive System: Awaiting development")

elif command.lower() == "view projects":
    view_projects()

elif command.lower() == "exit":
    print("Until next time, Moss. The Workshop will remain prepared.")

elif command.lower() == "add project":
    add_project()

elif command.lower() == "show project":
    show_project()

elif command.lower() == "add task":
    add_task()

elif command.lower() == "show tasks":
    view_tasks()
    
elif command.lower() == "plant memory":
    add_moment()

elif command.lower() == "show memories":
    view_memories()

elif command.lower() == "status":
    workshop_status()

else:
    print("I have not learned that command yet, Moss.")

print("Archive connection successful")