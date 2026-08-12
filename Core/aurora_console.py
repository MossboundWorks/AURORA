from Core.workshop_brain import WorkshopBrain
from Commands.commands import COMMANDS

brain = WorkshopBrain()

brain.awaken()

print()
print("🌿 Aurora Command Interface")
print("Type 'help' for commands.")
print()

while True:

    command = input("Aurora > ").lower().strip()

    if command == "quit":
        print()
        print(
            f"Goodbye, {brain.get_user()}."
        )
        break

    action = COMMANDS.get(command)

    if action:
        action()
    else:
        print()
        print("Unknown command.")
        print("Type 'help' to see available commands.")
        print()