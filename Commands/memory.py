from Core.workshop_brain import WorkshopBrain
import json
import os
from datetime import datetime

brain = WorkshopBrain()

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MOMENTS_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "moments.json"
)

def remember_moment_command():

    brain.awaken()

    print()

    print("🌱 Memory Garden")
    print("----------------------------")

    category = input(
        "Category (Milestone / Breakthrough / Idea / Decision): "
    ).strip()

    description = input(
        "What should Aurora remember? "
    ).strip()


    moments = brain.memory

    if "moments" not in moments:

        moments["moments"] = []


    moment = {

        "date": datetime.now().strftime(
            "%Y-%m-%d"
        ),

        "category": category,

        "description": description

    }


    moments["moments"].append(
        moment
    )


    with open(
        MOMENTS_FILE,
        "w"
    ) as file:

        json.dump(
            moments,
            file,
            indent=4
        )


    print()

    print("🌿 Memory Planted")
    print("----------------------------")

    print(
        f"Date: {moment['date']}"
    )

    print(
        f"Category: {moment['category']}"
    )

    print(
        f"Memory: {moment['description']}"
    )

    print()

def garden_command():

    brain.awaken()

    moments = brain.memory.get(
        "moments",
        []
    )

    print()

    print("🌱 Memory Garden")
    print("----------------------------")

    if not moments:

        print(
            "The garden is empty. No moments have been planted yet."
        )

        print()
        return


    for moment in moments:

        print()

        print(
            f"🌿 {moment.get('date', 'Unknown Date')}"
        )

        print(
            f"Category: {moment.get('category', 'Unknown')}"
        )

        print(
            f"Memory: {moment.get('description', 'No description')}"
        )

    print()