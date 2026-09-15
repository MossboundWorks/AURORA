import customtkinter as ctk
import json
import os

from Design.aurora_theme import (
    apply_theme,
    title_style,
    body_style,
    button_style,
    header_style,
    AURORA_DARK
)


def clear_window(window):

    for widget in window.winfo_children():
        widget.destroy()


def show_reflection(window, brain):

    apply_theme()

    clear_window(window)

    window.configure(
        fg_color=AURORA_DARK
    )

    title = ctk.CTkLabel(
        window,
        text="Reflection",
        **title_style()
    )

    title.pack(
        pady=(30, 10)
    )

    subtitle = ctk.CTkLabel(
        window,
        text="Look back at the Workshop and everything it has preserved.",
        **body_style()
    )

    subtitle.pack(
        pady=(0, 25)
    )

    menu = ctk.CTkFrame(
        window,
        fg_color="transparent"
    )

    menu.pack(
        fill="x",
        padx=40
    )

    memory_button = ctk.CTkButton(
        menu,
        text="Memory Garden",
        command=lambda: window.navigation.show(
            show_memory_garden
        ),
        **button_style()
    )

    memory_button.pack(
        pady=6
    )

    sessions_button = ctk.CTkButton(
        menu,
        text="Sessions",
        command=lambda: window.navigation.show(
            show_sessions
        ),
        **button_style()
    )

    sessions_button.pack(
        pady=6
    )

    history_button = ctk.CTkButton(
        menu,
        text="Workshop History",
        command=lambda: window.navigation.show(
            show_history
        ),
        **button_style()
    )

    history_button.pack(
        pady=6
    )

    back_button = ctk.CTkButton(
        window,
        text="Back to Workshop",
        command=lambda: window.navigation.go_to_workshop(),
        **button_style()
    )

    back_button.pack(
        pady=30
    )

def show_memory_garden(window, brain):

    clear_window(window)

    apply_theme()

    window.configure(
        fg_color=AURORA_DARK
    )

    title = ctk.CTkLabel(
        window,
        text="Memory Garden",
        **title_style()
    )

    title.pack(
        pady=(25, 10)
    )

    subtitle = ctk.CTkLabel(
        window,
        text="Moments AURORA has chosen to preserve.",
        **body_style()
    )

    subtitle.pack(
        pady=(0, 15)
    )

    scroll_frame = ctk.CTkScrollableFrame(
        window,
        width=620,
        height=450,
        fg_color=AURORA_DARK
    )

    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 10)
    )

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    memory_file = os.path.join(
        base_dir,
        "Memory",
        "milestones.json"
    )

    if not os.path.exists(memory_file):

        message = ctk.CTkLabel(
            scroll_frame,
            text="Memory Garden could not locate milestones.json.",
            **body_style()
        )

        message.pack(
            pady=30
        )

    else:

        with open(
            memory_file,
            "r"
        ) as file:

            data = json.load(file)

        milestones = data.get(
            "milestones",
            []
        )

        if not milestones:

            message = ctk.CTkLabel(
                scroll_frame,
                text="Memory Garden is currently empty.",
                **body_style()
            )

            message.pack(
                pady=30
            )

        else:

            for milestone in milestones:

                card = ctk.CTkFrame(
                    scroll_frame,
                    fg_color="#273327",
                    corner_radius=12
                )

                card.pack(
                    fill="x",
                    padx=10,
                    pady=8
                )

                category = ctk.CTkLabel(
                    card,
                    text=milestone.get(
                        "category",
                        "Memory"
                    ),
                    **header_style()
                )

                category.pack(
                    anchor="w",
                    padx=15,
                    pady=(12, 2)
                )

                date = ctk.CTkLabel(
                    card,
                    text=milestone.get(
                        "date",
                        "Unknown date"
                    ),
                    **body_style()
                )

                date.pack(
                    anchor="w",
                    padx=15
                )

                description = ctk.CTkLabel(
                    card,
                    text=milestone.get(
                        "description",
                        "No description."
                    ),
                    **body_style(),
                    wraplength=540,
                    justify="left",
                    anchor="w"
                )

                description.pack(
                    anchor="w",
                    padx=15,
                    pady=(5, 12)
                )

    back_button = ctk.CTkButton(
        window,
        text="Back to Reflection",
        width=220,
        command=lambda: window.navigation.back(),
        **button_style()
    )

    back_button.pack(
        pady=(5, 15)
    )

def show_journal(window):

    clear_window(window)

    title = ctk.CTkLabel(
        window,
        text="Journal",
        **title_style()
    )

    title.pack(
        pady=30
    )

    message = ctk.CTkLabel(
        window,
        text="The Workshop Journal will appear here.",
        **body_style()
    )

    message.pack(
        pady=20
    )

    back_button = ctk.CTkButton(
        window,
        text="Back to Reflection",
        command=lambda: show_reflection(window),
        **button_style()
    )

    back_button.pack(
        pady=30
    )


def show_sessions(window, brain):

    clear_window(window)

    title = ctk.CTkLabel(
        window,
        text="Work Sessions",
        **title_style()
    )

    title.pack(
        pady=30
    )

    message = ctk.CTkLabel(
        window,
        text="Recorded work sessions will appear here.",
        **body_style()
    )

    message.pack(
        pady=20
    )

    back_button = ctk.CTkButton(
        window,
        text="Back to Reflection",
        command=lambda: window.navigation.back(),
        **button_style()
    )

    back_button.pack(
        pady=30
    )


def show_history(window, brain):

    clear_window(window)

    title = ctk.CTkLabel(
        window,
        text="Workshop History",
        **title_style()
    )

    title.pack(
        pady=30
    )

    message = ctk.CTkLabel(
        window,
        text="Workshop history will appear here.",
        **body_style()
    )

    message.pack(
        pady=20
    )

    back_button = ctk.CTkButton(
        window,
        text="Back to Reflection",
        command=lambda: window.navigation.back(),
        **button_style()
    )

    back_button.pack(
        pady=30
    )

def return_to_dashboard(window, brain):

    clear_window(window)

    from Interface.workshop_dashboard import show_dashboard

    show_dashboard(
        window,
        brain
    )