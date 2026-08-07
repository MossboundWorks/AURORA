from Core.workshop_brain import WorkshopBrain

brain = WorkshopBrain()

def help_command():
    print()
    print("Available Commands")
    print("------------------")
    print("help")
    print("identity")
    print("mission")
    print("welcome")
    print("projects")
    print("record")
    print("journal")
    print("view journal")
    print("reflect")
    print("health")
    print("quit")
    print("tasks")
    print("add task")
    print("complete task")
    print("remember moment")
    print("garden")
    print("search")
    print()

def identity_command():

    brain.awaken()

    identity = brain.get_identity()

    print()
    print("🌿 AURORA")
    print("----------------------------")

    print(
        identity.get(
            "role",
            "Artificial Unified Reasoning & Organizational Response Assistant"
        )    
    )

    print()

    print(
        f"Creator: {brain.get_creator()}"
    )
    
    print()

def mission_command():

    brain.awaken()

    mission = brain.get_mission()

    print()
    print("Mission")
    print("----------------------------")

    print(
        mission.get(
            "primary",
            "Mission data unavailable."
        )
    )

    print()

    secondary = mission.get(
        "secondary",
        []
    )

    for goal in secondary:
        print(f"🌱 {goal}")

    print()
