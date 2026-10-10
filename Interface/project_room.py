import customtkinter as ctk

from Core.workshop_brain import WorkshopBrain

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

def open_project_room(window, brain):

    apply_theme()

    for widget in window.winfo_children():
        widget.destroy()

    window.configure(
        fg_color=AURORA_DARK
    )

    title = ctk.CTkLabel(
        window,
        text="Project Archive",
        **title_style()
    )

    title.pack(
        pady=20
    )

    scroll_frame = ctk.CTkScrollableFrame(
        window,
        width=550,
        height=450,
        fg_color=AURORA_DARK
    )

    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 10)
    )

    projects = brain.get_projects()

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
                f"{project['name']}\n"
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
            command=lambda p=project: open_project_tasks(
                window,
                brain,
                p
            ),
            **button_style()
        )

        task_button.pack(
            padx=15,
            pady=(0, 15),
            anchor="w"
        )

    back_button = ctk.CTkButton(
        window,
        text="Back to Workshop",
        command=lambda: window.navigation.go_to_workshop(),
        **button_style()
    )

    back_button.pack(
        pady=15
    )

def return_to_dashboard(window, brain):

    for widget in window.winfo_children():
        widget.destroy()

    from Interface.workshop_dashboard import show_dashboard

    show_dashboard(
        window,
        brain
    )

def open_project_tasks(window, brain, project):

    window.navigation.show(
        show_task_list,
        project["name"]
    )