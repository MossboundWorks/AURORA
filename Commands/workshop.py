from Core.workshop_brain import WorkshopBrain

brain = WorkshopBrain()

def welcome_command():

    brain.awaken()

    print()

    print(
        brain.get_welcome_back()
    )

    print()

    print(
        "🌙 Workshop Summary"
    )

    print(
        "----------------------------"
    )

    for line in brain.get_workshop_summary():

        print(line)

    print()

def history_command():

    brain.awaken()

    history = brain.get_workshop_history()

    print()

    print("Workshop History")
    print("----------------------------")

    if not history:

        print()
        print("No completed Workshop sessions found.")
        print()

        return

    print()

    for session in history:

        print(
            f"Project: {session['project']}"
        )

        if session["task"]:

            print(
                f"Task: {session['task']}"
            )

        print(
            f"Started: {session['started']}"
        )

        print(
            f"Ended: {session['ended']}"
        )

        print(
            f"Status: {session['status']}"
        )

        if session["accomplishments"]:

            print("Accomplishments:")

            for accomplishment in session["accomplishments"]:

                print(
                    f"  - {accomplishment}"
                )

        if session["next_step"]:

            print(
                f"Next Step: {session['next_step']}"
            )

        print()

def reflect_command():

    brain.awaken()

    print()

    print("Workshop Reflection")
    print("----------------------------")

    print()

    summary = brain.get_system_summary()

    if summary["current_focus"]:

        print(
            f"Current Focus: {summary['current_focus']}"
        )

        print(
            f"Project: {summary['project']}"
        )

        print()

        print(
            f"Reason:"
        )

        print(
            summary["reason"]
        )

    else:

        print(
            "No current focus detected."
        )

    print()

    print("Observations")

    print()

    for observation in brain.make_observation():

        print(observation)

    print()

    print("Recommendation")

    print()

    for recommendation in brain.give_recommendation():

        print(recommendation)

    print()

def health_command():

    brain.awaken()

    checks = brain.health_check()

    print()
    print("⚙ Aurora Health Check")
    print("----------------------------")

    for system, status in checks.items():

        symbol = "✅" if status else "❌"

        print(
            f"{symbol} {system}"
        )

    print()

def record_command():

    brain.awaken()

    print()

    entry = brain.record_session()

    if not entry:

        print(
            "No completed work session found."
        )

        print()

        return

    print(
        "Workshop Record"
    )

    print(
        "----------------------------"
    )

    print(
        f"Project: "
        f"{entry['project']}"
    )

    print(
        f"Focus: "
        f"{entry['focus']}"
    )

    print(
        f"Accomplishment: "
        f"{entry['accomplishment']}"
    )

    print(
        f"Next Step: "
        f"{entry['next_step']}"
    )

    print()