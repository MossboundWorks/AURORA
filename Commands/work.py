from Core.workshop_brain import WorkshopBrain


brain = WorkshopBrain()


def work_command():

    work = brain.get_current_work()

    if work:

        print()
        print("You already have an active work session.")
        print()

        print(
            f"Project: {work.get('project', 'Unknown')}"
        )

        if work.get("task"):

            print(
                f"Task: {work.get('task')}"
            )

        print(
            f"Started: {work.get('started', 'Unknown')}"
        )

        print(
            f"Status: {work.get('status', 'Unknown')}"
        )

        print()

        return

    task = brain.select_work()

    if not task:

        print()
        print("No valid task was selected.")
        print()

        return

    session = brain.start_work(
        task.get("project"),
        task.get("title")
    )

    print()
    print("Work session started.")
    print()

    print(
        f"Project: {session.get('project')}"
    )

    print(
        f"Task: {session.get('task')}"
    )

    print(
        f"Started: {session.get('started')}"
    )

    print(
        f"Status: {session.get('status')}"
    )

    print()

def end_work_command():

    work = brain.get_current_work()

    if not work:

        print()
        print("There is no active work session.")
        print()

        return

    print()
    print(
        f"Ending work on: {work.get('task', 'Unknown')}"
    )
    print()

    accomplishments_input = input(
        "What did you accomplish? "
    )

    next_step = input(
        "What is the next step? "
    )

    accomplishments = []

    if accomplishments_input.strip():

        accomplishments.append(
            accomplishments_input.strip()
        )

    session = brain.finish_work(
        accomplishments,
        next_step
    )

    print()
    print("Work session completed.")
    print()

    print(
        f"Project: {session.get('project')}"
    )

    print(
        f"Task: {session.get('task')}"
    )

    print(
        f"Started: {session.get('started')}"
    )

    print(
        f"Ended: {session.get('ended')}"
    )

    print(
        f"Duration: "
        f"{session.get('duration_minutes')} minutes"
    )

    print(
        f"Status: {session.get('status')}"
    )

    print()