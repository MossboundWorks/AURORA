import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


TASK_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "tasks.json"
)


PROJECT_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "memories.json"
)


def load_data(path):

    if os.path.exists(path):

        with open(path, "r") as file:
            return json.load(file)

    return {}



def get_today_focus():

    tasks_data = load_data(TASK_FILE)

    tasks = tasks_data.get(
        "tasks",
        []
    )

    projects = load_data(PROJECT_FILE)


    active_tasks = []

    for task in tasks:

        if not task.get("completed", False):
            
            active_tasks.append(task)

    priority_order = {
        "high": 1,
        "High": 1,
        "medium": 2,
        "Medium": 2,
        "low": 3,
        "Low": 3
    }

    active_tasks.sort(
        key=lambda task: priority_order.get(
            task.get("priority", "low"),
            3
        )
    )

    active_projects = projects.get(
        "projects",
        []
    )

    project_map = {}

    for project in active_projects:

        project_map[
            project["name"]
        ] = project

    return {
        "projects": active_projects,
        "project_map": project_map,
        "tasks": active_tasks
    }



def get_next_action():

    focus = get_today_focus()

    tasks = focus["tasks"]

    project_map = focus["project_map"]


    if not tasks:

        return {
            "task": None,
            "reason": "No unfinished tasks found."
        }


    next_task = tasks[0]


    project = project_map.get(
    next_task["project"],
    {}
)


    project_type = project.get(
       "type",
        "Unknown"
)


    reason = (
        f"This is a {next_task['priority']} priority task "
        f"connected to {next_task['project']}, "
        f"a {project_type} project."
)

    details = (
        f"{next_task['title']} is currently marked "
        f"as {next_task['status']} and was created "
        f"on {next_task['created']}."
    )

    project_details = (
        f"Project: {next_task['project']}\n"
        f"Type: {project_type}"
)

    return {
        "task": next_task,
        "reason": reason,
        "details": details,
        "project_details": project_details
    }


if __name__ == "__main__":

    focus = get_today_focus()

    print("🌿 Aurora Focus Report")
    print()


    print("Projects:")

    for project in focus["projects"]:
        print(
            f"📚 {project['name']}"
        )


    print()


    print("Tasks:")

    for task in focus["tasks"]:
        print(
            f"📋 {task['title']} "
            f"({task['priority']} priority)"
        )


    print()


    action = get_next_action()

    print("🌿 Recommended Next Action:")
    print()


    if action["task"]:

        print(
            f"✨ {action['task']['title']}"
        )

        print(
            f"💡 Reason: {action['reason']}"
        )

        print(
            f"📖 Details: {action['details']}"
        )

        print(
            f"📚 {action['project_details']}"
        )

    else:

        print(action["reason"])