from Core.workshop_brain import WorkshopBrain
import json
import os

brain = WorkshopBrain()

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

TASK_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "tasks.json"
)
def tasks_command():

    brain.awaken()

    tasks = brain.tasks.get(
        "tasks",
        []
    )

    print()

    print("📋 Workshop Tasks")
    print("----------------------------")

    if not tasks:

        print("No tasks found.")
        print()
        return

    for task in tasks:

        status = "✅" if task.get(
            "completed",
            False
        ) else "🌱"

        print()

        print(
            f"{status} {task['title']}"
        )

        print(
            f"   Project: {task['project']}"
        )

        print(
            f"   Priority: {task['priority']}"
        )

    print()

def add_task_command():

    brain.awaken()

    print()

    project = input(
        "Project: "
    ).strip()

    title = input(
        "Task: "
    ).strip()

    priority = input(
        "Priority (High / Medium / Low): "
    ).strip().capitalize()

    tasks = brain.tasks

    if "tasks" not in tasks:
        tasks["tasks"] = []

    new_task = {
        "title": title,
        "project": project,
        "priority": priority,
        "completed": False
    }

    tasks["tasks"].append(
        new_task
    )

    with open(
        TASK_FILE,
        "w"
    ) as file:

        json.dump(
            tasks,
            file,
            indent=4
        )

    print()

    print("🌱 Task Added")
    print("----------------------------")

    print(f"Task: {title}")
    print(f"Project: {project}")
    print(f"Priority: {priority}")

    print()

def complete_task_command():

    brain.awaken()

    tasks = brain.tasks.get(
        "tasks",
        []
    )

    print()

    print("📋 Incomplete Tasks")
    print("----------------------------")

    incomplete = []

    for index, task in enumerate(tasks):

        if not task.get(
            "completed",
            False
        ):

            incomplete.append(task)

            print(
                f"{len(incomplete)}. {task['title']}"
            )

            print(
                f"   Project: {task['project']}"
            )

            print()

    if not incomplete:

        print("🌱 No incomplete tasks found.")

        print()
        return


    choice = input(
        "Complete which task? "
    ).strip()


    try:

        selection = int(choice) - 1

        task = incomplete[selection]

    except (
        ValueError,
        IndexError
    ):

        print()

        print(
            "❌ Invalid task selection."
        )

        print()

        return


    task["completed"] = True


    with open(
        TASK_FILE,
        "w"
    ) as file:

        json.dump(
            brain.tasks,
            file,
            indent=4
        )


    print()

    print("✅ Task Completed")
    print("----------------------------")

    print(
        f"{task['title']}"
    )

    print(
        f"Project: {task['project']}"
    )

    print()