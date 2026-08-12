import time
import json
import os
import random

from Core.aurora_focus import get_today_focus
from Core.workshop_brain import WorkshopBrain
from datetime import datetime

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MEMORY_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "milestones.json"
)

PROJECT_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "projects.json"
)

TASK_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "tasks.json"
)

STATE_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "workshop_state.json"    
)

JOURNAL_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "workshop_journal.json"
)

def load_data(path):

    if os.path.exists(path):

        with open(path, "r") as file:
            return json.load(file)

    return {}

def system_report():

    memories = load_data(MEMORY_FILE)
    projects = load_data(PROJECT_FILE)
    tasks = load_data(TASK_FILE)

    project_list = projects.get("projects", [])

    project_names = []

    for project in project_list:
        project_names.append(
            project["name"]
        )

    memory_count = len(
        memories.get("milestones", [])
    )

    project_count = len(
        projects.get("projects", [])
    )

    task_count = len(
        tasks.get("tasks", [])
    )


    return {

    "memory_count": memory_count,

    "project_count": project_count,

    "project_names": project_names,

    "task_count": task_count

    }

def display_system_report():

    report = system_report()

    print(
        f"Memory Garden: "
        f"{report['memory_count']} memories preserved."
    )

    print(
        f"Project Archive: "
        f"{report['project_count']} projects found."
    )

    print(
        f"    Projects: "
        f"{', '.join(report['project_names'])}"
    )

    print(
        f"Task Board: "
        f"{report['task_count']} tasks tracked."
    )

def focus_report():

    focus = get_today_focus()


    projects = focus["projects"]
    tasks = focus["tasks"]


    report = []


    report.append(
        "Workshop Overview:"
    )


    report.append(
        ""
    )


    report.append(
        "Active Projects:"
    )


    for project in projects[:3]:

        report.append(
            f"   {project['name']}"
        )


    report.append(
        ""
    )


    report.append(
        "Pending Tasks:"
    )


    for task in tasks[:3]:

        report.append(
            f"   🌱 {task['title']} "
            f"({task['priority']} priority)"
        )


    return report

def work_status_report():

    brain = WorkshopBrain()

    work = brain.get_work_status()

    if not work:

        return [
            "There is no active work session."
        ]

    return work.splitlines()

def run_boot_sequence():

    messages = [
        "Initializing Aurora Workshop...",
        "Connecting Design Engine...",
        "Dusting Project Archive...",
        "Watering Memory Garden...",
        "Loading Task Board...",
        "",
        get_greeting()
    ]

    for message in messages:

        print(message)

        time.sleep(0.7)

    print()

    for message in work_status_report():

        print(message)

        time.sleep(0.7)

def workshop_ready():
    return True

def get_greeting():

    brain = WorkshopBrain()
    brain.awaken()

    user = brain.get_user()

    greetings = [

        f"Welcome back, {user}. The Workshop has been waiting.",

        f"Good to see you again, {user}. Everything is just as you left it.",

        f"Your projects are safe, {user}. Shall we continue building?",

        f"The Memory Garden has been quiet while you were away, {user}.",

        f"Systems ready, {user}. Magic stable. Workshop prepared.",

        f"Welcome home, {user}. Your next creation is waiting."
    ]

    return random.choice(greetings)

def load_workshop_state():

    if os.path.exists(STATE_FILE):

        with open(STATE_FILE, "r") as file:
            return json.load(file)
        
    return {
        "memory_count": 0,
        "project_count": 0,
        "task_count": 0
    }

def save_workshop_state(state):

    with open(STATE_FILE, "w") as file:
        json.dump(
            state,
            file,
            indent=4
        )

def workshop_progress():

    previous = load_workshop_state()

    memories = system_report()["memory_count"]
    projects = system_report()["project_count"]
    tasks = system_report()["task_count"]

    messages = []

    if memories > previous["memory_count"]:

        messages.append(
            "The Memory Garden has grown."
        )

    if projects > previous["project_count"]:

        messages.append(
            "The Project Archive welcomed something new."
        )

    if tasks > previous["task_count"]:

        messages.append(
            "New work has appeared on the Task Board."
        )

    save_workshop_state({

        "memory_count": memories,
        "project_count": projects,
        "task_count": tasks
    })

    return messages


def daily_briefing():

    brain = WorkshopBrain()

    brain.awaken()

    action = brain.get_next_action()

    report = []

    report.append(
        "Today's Focus:"
    )

    report.append(
        ""
    )

    if action["task"]:

        report.append(
            f"{action['task']['title']}"
        )

        report.append(
            f"Project: {action['task']['project']}"
        )

        report.append(
            f"{action['reason']}"
        )

    else:

        report.append(
            "No active tasks found."
        )


    return report

def write_journal_entry():

    print("Writing workshop journal...")    

    journal = load_data(JOURNAL_FILE)

    if "entries" not in journal:
        journal["entries"] = []


    report = system_report()


    entry = {

        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        ),

        "memories": report["memory_count"],

        "projects": report["project_count"],

        "tasks": report["task_count"]

    }


    journal["entries"].append(entry)


    with open(JOURNAL_FILE, "w") as file:

        json.dump(
            journal,
            file,
            indent=4
        )


    return entry

if __name__ == "__main__":

    run_boot_sequence()

    progress = workshop_progress()

    if progress:

        print()

        print("Since your last visit:")

        print()

        for message in progress:

            print(message)

        print()

    display_system_report()

    print()

    for focus in focus_report():

        print(focus)

        time.sleep(0.7)

    print()

    for message in daily_briefing():

        print(message)

        time.sleep(0.7)

    write_journal_entry()