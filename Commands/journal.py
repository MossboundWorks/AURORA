from Core.workshop_brain import WorkshopBrain

brain = WorkshopBrain()

def journal_command():

    brain.awaken()

    print()

    project = input(
        "Project: "
    ).strip()

    focus = input(
        "What was the focus? "
    ).strip()

    accomplishment = input(
        "What did you accomplish? "
    ).strip()

    next_step = input(
        "What comes next? "
    ).strip()


    entry = brain.write_journal_entry(
        project,
        focus,
        accomplishment,
        next_step
    )


    print()

    print("📖 Journal Entry Saved")
    print("----------------------------")

    print(
        f"Project: {entry['project']}"
    )

    print(
        f"Focus: {entry['focus']}"
    )

    print(
        f"Accomplished: {entry['accomplishment']}"
    )

    print(
        f"Next: {entry['next_step']}"
    )

    print()

def journal_view_command():

    brain.awaken()

    entries = brain.journal.get(
        "entries",
        []
    )

    print()

    print("📖 Workshop Journal")
    print("----------------------------")

    if not entries:

        print("No journal entries found.")
        print()
        return
    
    for entry in entries:
        
        print()

        print(
            f"🌿 {entry['date']}"
        )

        print(
            f"Projects: {entry.get('project', 'Unknown')}"
        )
            

        print(
            f"Focus: {entry.get('focus', 'Unknown')}"
        )

        print(
            f"Accomplished: {entry.get('accomplishment', 'Unknown')}"
        )

        print(
            f"Next Step: {entry.get('next_step', 'Unknown')}"
        )

        print()