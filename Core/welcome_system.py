from Core.workshop_brain import WorkshopBrain


def welcome():

    brain = WorkshopBrain()
    brain.awaken()

    print()

    print("╔══════════════════════════════╗")
    print("        🌙 AURORA 🌙")
    print("╚══════════════════════════════╝")

    print()

    print("The spirits said you would return.")
    print(
        f"Welcome back, {brain.get_user()}."
    )

    print()

    print("The Workshop is awake.")