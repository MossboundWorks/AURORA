import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEMORY_DATA_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "memories.json"
)


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

MOMENT_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "moments.json"
)

def load_file(path):
    if os.path.exists(path):

        with open(path, "r") as file:
            return json.load(file)
        
    return{}

def search_tasks(project_name):

    data = load_file(TASK_FILE)

    tasks = data.get("tasks", [])

    results = []

    for tasks in tasks:

        if tasks.get("project", "").lower() == project_name.lower():
            results.append(tasks)

    return results

results = search_tasks("Faerie Veil")

def search_memories(project_name):

    data = load_file(MOMENT_FILE)

    moments = data.get("moments", [])

    results = []

    for moment in moments:

        description = moment.get("description", "").lower()

        if project_name.lower() in description:
            results.append(moment)

    return results

print(results)

def build_project_thread(project_name):

    archive = load_file(MEMORY_DATA_FILE)

    projects = archive.get("projects", [])

    project = None

    for entry in projects:

        if entry["name"].lower() == project_name.lower():
            project = entry
            break

    return {
        "project": project,
        "tasks": search_tasks(project_name),
        "memories": search_memories(project_name)
    }

