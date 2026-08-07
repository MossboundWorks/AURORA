import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


MEMORY_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "memories.json"
)


TASK_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "tasks.json"
)

def load_data(path):

    if os.path.exists(path):

        with open(path, "r") as file:
            return json.load(file)

    return {}

def workshop_status():

    memory = load_data(MEMORY_FILE)

    tasks = load_data(TASK_FILE)


    projects = memory.get("projects", [])

    task_list = tasks.get("tasks", [])

    moments = memory.get("moments", [])


    print()

    print("╔══════════════════════════════╗")
    print("       🌙 WORKSHOP STATUS 🌙")
    print("╚══════════════════════════════╝")

    print()

    print(f"📚 Creations: {len(projects)}")

    print(f"📋 Tasks: {len(task_list)}")

    print(f"🌿 Memories: {len(moments)}")

