import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_FILE = os.path.join(BASE_DIR, "Memory", "memories.json")


def load_projects():

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            memory = json.load(file)
            return memory["projects"]

    return []


def view_projects():
    projects = load_projects()

    if not projects:
        print("The Workshop Archive is currently empty.")
        return

    print("The Workshop Archive contains:")

    for project in projects:
        print()
        print(f"Name: {project['name']}")
        print(f"Type: {project['type']}")
        print(f"Status: {project['status']}")

def save_memory(memory):
    backup_file = MEMORY_FILE.replace(
        "memories.json",
        "memories_backup.json"
    )

    # Create backup before changing memory
    with open(MEMORY_FILE, "r") as original:
        old_memory = original.read()

    with open(backup_file, "w") as backup:
        backup.write(old_memory)

    # Save new memory
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

    print("Memory vault protected. Backup created.")

def add_project():
    with open(MEMORY_FILE, "r") as file:
        memory = json.load(file)

        print()
        name = input("What shall this creation be called?")

        project_type = input("What kind of creation is it?")

        status = input("What is its current status?")

        description = input("Describe it in a sentence:")

        creator = input("Who is creating this? (Press enter for Moss):")

        if creator.strip() == "":
            creator = "Moss"

        contributors = []

        feeling = input("What feeling does this project carry?")

        vision = input("Describe your vision for this creation:")

        new_project = {
            "name": name,
            "type": project_type,
            "status": status,
            "creator": creator,
            "contributors": contributors,
            "description": description,
            "feeling": feeling,
            "vision": vision,
            "notes": [],
            "next_steps": []
        }

        memory["projects"].append(new_project)

        save_memory(memory)

        print()
        print(f'"{name}" has been preserved within the Workshop Archive.')

def show_project():
        with open(MEMORY_FILE, "r") as file:
            memory = json.load(file)

        search_name = input("Which project shall I open? ")

        for project in memory["projects"]:
         if project["name"].lower() == search_name.lower():
            print()
            print("Opening archive entry...")
            print()

            print("╔══════════════════════════════╗")
            print("        🌙 ARCHIVE ENTRY 🌙")
            print("╚══════════════════════════════╝")

            print()

            print("✨ Name:")
            print(project["name"])

            print()

            print("📜 Type:")
            print(project["type"])

            print()

            print("🌱 Status:")
            print(project["status"])

            print()

            print("🧚 Creator:")
            print(project.get("creator", "Unknown"))

            print()

            print("🌙 Feeling:")
            print(project.get("feeling", "No feeling recorded."))

            print()

            print("🔮 Vision:")
            print(project.get("vision", "No vision recorded."))

            print()

            print("📖 Description:")
            print(project.get("description", "No description recorded."))

            print()
            print("Archive entry complete.")

            return

        print()
        print("I could not find that creation in the Workshop Archive.")    