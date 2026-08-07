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

def reflect_command():

    brain.awaken()

    print()

    print("🌿 Workshop Reflection")
    print("----------------------------")

    print()

    summary = brain.get_system_summary()

    if summary["current_focus"]:

        print(
            f"🎯 Current Focus: {summary['current_focus']}"
        )

        print(
            f"📚 Project: {summary['project']}"
        )

        print()

        print(
            f"💡 Reason:"
        )

        print(
            summary["reason"]
        )

    else:

        print(
            "🌱 No current focus detected."
        )

    print()

    print("🌿 Observations")

    print()

    for observation in brain.make_observation():

        print(observation)

    print()

    print("💡 Recommendation")

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

    project = input(
        "Project name: "
    ).strip()

    note = input(
        "What did you accomplish? "
    ).strip()

    session = brain.record_session(
        project,
        note
    )

    print()

    print("🌿 Session Recorded")
    print("----------------------------")

    print(
        f"Project: {session['project']}"
    )

    print(
        f"Note: {session['note']}"
    )

    print()