import json
import os
from datetime import date


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MOMENT_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "milestones.json"
)


def load_moments():

    if os.path.exists(MOMENT_FILE):

        with open(MOMENT_FILE, "r") as file:
            return json.load(file)

    return {"milestones": []}


def save_moments(data):

    with open(MOMENT_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_moment():

    data = load_moments()
    
    print()

    category = input("What kind of memory is this?")

    description = input("What should Aurora remember?")

    moment = {
        "date": str(date.today()),
        "category": category,
        "description": description
    }

    data["milestones"].append(moment)

    save_moments(data)

    print()
    print("🌿 The memory has been planted in the Garden.")

def view_memories():

    data = load_moments()

    moments = data["milestones"]

    print()

    if not moments:
        print("🌱 The Memory Garden is empty.")
        return

    print("╔══════════════════════════════╗")
    print("        🌿 MEMORY GARDEN 🌿")
    print("╚══════════════════════════════╝")

    print()

    for moment in moments:

        print("━━━━━━━━━━━━━━━━━━━━")

        print(f"📅 {moment['date']}")
        print(f"✨ {moment['category']}")
        print(f"🌱 {moment['description']}")

        print()