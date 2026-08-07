from Core.workshop_brain import WorkshopBrain

brain = WorkshopBrain()

def projects_command():

    brain.awaken()

    projects = brain.get_projects()

    print()
    print("📚 Workshop Projects")
    print("----------------------------")

    if not projects:
        print("No projects found.")
        print()
        return

    for project in projects:

        print()

        print(
            f"✨ {project.get('name', 'Unnamed Project')}"
        )

        print(
            f"   Type: {project.get('type', 'Unknown')}"
        )

        print(
            f"   Status: {project.get('status', 'Unknown')}"
        )

        if project.get("description"):

            print(
                f"   {project['description']}"
            )

    print()
