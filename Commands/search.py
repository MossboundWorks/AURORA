from Core.workshop_brain import WorkshopBrain

brain = WorkshopBrain()

def search_command():

    brain.awaken()

    print()

    query = input(
        "🔎 Search the Workshop: "
    ).lower().strip()

    print()

    print("🔎 Workshop Search")
    print("----------------------------")

    found = False

    # ----------------------------
    # Search Projects
    # ----------------------------

    for project in brain.get_projects():

        text = " ".join([
            project.get("name", ""),
            project.get("type", ""),
            project.get("description", "")
        ]).lower()

        if query in text:

            found = True

            print()

            print("📚 Project")

            print(
                f"✨ {project['name']}"
            )

            print(
                f"Type: {project['type']}"
            )

            print(
                f"Status: {project['status']}"
            )

    # ----------------------------
    # Search Tasks
    # ----------------------------

    tasks = brain.tasks.get(
        "tasks",
        []
    )

    for task in tasks:

        text = " ".join([
            task.get("title", ""),
            task.get("project", ""),
            task.get("priority", "")
        ]).lower()

        if query in text:

            found = True

            print()

            print("📋 Task")

            status = (
                "✅ Completed"
                if task.get(
                    "completed",
                    False
                )
                else "🌱 In Progress"
            )

            print(
                f"Task: {task['title']}"
            )

            print(
                f"Project: {task['project']}"
            )

            print(status)

    # ----------------------------
    # Search Journal
    # ----------------------------

    entries = brain.journal.get(
        "entries",
        []
    )

    for entry in entries:

        text = " ".join([
            entry.get("project", ""),
            entry.get("focus", ""),
            entry.get("accomplishment", ""),
            entry.get("next_step", "")
        ]).lower()

        if query in text:

            found = True

            print()

            print("📖 Journal")

            print(
                f"Date: {entry.get('date', 'Unknown')}"
            )

            print(
                f"Project: {entry.get('project', 'Unknown')}"
            )

            print(
                f"Focus: {entry.get('focus', 'Unknown')}"
            )

            print(
                f"Accomplished: {entry.get('accomplishment', 'Unknown')}"
            )

            print(
                f"Next: {entry.get('next_step', 'Unknown')}"
            )

    # ----------------------------
    # Search Memory Garden
    # ----------------------------

    moments = brain.memory.get(
        "milestones",
        []
    )

    for moment in moments:

        text = " ".join([
            moment.get("category", ""),
            moment.get("description", "")
        ]).lower()

        if query in text:

            found = True

            print()

            print("🌱 Memory")

            print(
                f"Date: {moment.get('date', 'Unknown')}"
            )

            print(
                f"Category: {moment.get('category', 'Unknown')}"
            )

            print(
                f"Memory: {moment.get('description', 'No description')}"
            )

        if not found:

            print(
                "Nothing matched your search."
            )

        print()