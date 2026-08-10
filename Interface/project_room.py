import customtkinter as ctk
import json
import os

from Design.aurora_theme import (
    apply_theme,
    title_style,
    header_style,
    body_style,
    button_style,
    card_style,
    AURORA_DARK
)

from Interface.task_chamber import show_task_list


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

PROJECT_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "projects.json"
)

def load_projects():

    if os.path.exists(PROJECT_FILE):

        with open(PROJECT_FILE, "r") as file:
            return json.load(file)
        
    return{}


def open_project_room():

    apply_theme()

    room = ctk.CTkToplevel(
        fg_color="#1B241B"
    )

    room.title("📚 Project Archive")

    room.geometry("600x500")


    title = ctk.CTkLabel(
        room,
        text="📚 Project Archive",
        **title_style()
    )

    title.pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(
        room,
        width=550,
        height=380,
        fg_color=AURORA_DARK
    )

    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 20)
    )


    data = load_projects()

    projects = data.get("projects", [])


    for project in projects:

        card = ctk.CTkFrame(
            scroll_frame,
            **card_style()
        )

        card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        info = ctk.CTkLabel(
            card,
            text=(
                f"🌿 {project['name']}\n"
                f"Type: {project['type']}\n"
                f"Status: {project['status']}\n"
                f"Creator: {project['creator']}\n\n"
                f"Contributors: {project['contributors']}\n"
                f"Description:\n{project['description']}\n\n"
                f"Feeling: {project['feeling']}\n"
                f"Vision:\n{project['vision']}\n\n"
                f"Notes: {project['notes']}\n"
                f"Next Steps: {project['next_steps']}"
            ),
            **body_style(),
            justify="left",
            anchor="w"
        )

        info.pack(
            padx=15,
            pady=10,
            anchor="w"
        )

        task_button = ctk.CTkButton(
            card,
            text="View Tasks",
            command=lambda p=project: open_project_tasks(p),
            **button_style()
        )

        task_button.pack(
            padx=15,
            pady=(0, 15),
            anchor="w"
        )

def open_project_tasks(project):

    # TEMP CHANGE DELETE LATER 
    
    print("PROJECT SENT:")
    print(project["name"])

    window = ctk.CTkToplevel()

    window.title(
        f"{project['name']} Quests"
    )

    window.geometry(
        "700x600"
    )

    show_task_list(
        window,
        project["name"]
    )