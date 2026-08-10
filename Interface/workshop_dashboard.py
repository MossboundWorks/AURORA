import customtkinter as ctk

from Core.workshop_brain import WorkshopBrain
from Interface.memory_room import open_memory_room 
from Interface.project_room import open_project_room
from Interface.task_chamber import open_task_chamber

from Design.aurora_theme import (
    apply_theme,
    title_style,
    header_style,
    body_style,
    button_style,
    card_style,
    AURORA_DARK,
    AURORA_PANEL,
    AURORA_GLOW
)

class WorkshopDashboard:

    def __init__(self):

        self.brain = WorkshopBrain()

        self.window = ctk.CTk()

        self.window.title(
            "AURORA Workshop"
        )

        self.window.geometry(
            "700x650"
        )


    def load_workshop(self):

        self.brain.awaken()

        summary = self.brain.get_workshop_summary()

        return summary


    def build(self):

        apply_theme()

        self.window.configure(
            fg_color=AURORA_DARK
        )

        title = ctk.CTkLabel(
            self.window,
            text="AURORA",
            **title_style()
        )

        title.pack(
            pady=20
        )

        subtitle = ctk.CTkLabel(
            self.window,
            text="The Workshop is awake.",
            **body_style()
        )

        subtitle.pack()

        menu = ctk.CTkFrame(
            self.window,
            fg_color="transparent"
        )

        menu.pack(
            pady=10
        )


        buttons = [
            ("Projects", open_project_room),
            ("Tasks", open_task_chamber),
            ("Journal", None),
            ("Memory Garden", open_memory_room),
            ("Reflection", None),
            ("Health", None)
        ]


        for text, command in buttons:

            ctk.CTkButton(
                menu,
                text=text,
                width=220,
                command=command,
                **button_style()
            ).pack(
                pady=5
            )


        summary = self.load_workshop()


        summary_box = ctk.CTkTextbox(
            self.window,
            height=180,
            width=620,
            fg_color=AURORA_PANEL,
            text_color="white",
            border_width=0
        )

        summary_box.pack(
            pady=20
        )


        for line in summary:

            summary_box.insert(
                ctk.END,
                line + "\n"
            )


        summary_box.configure(
            state="disabled"
        )


    def run(self):

        self.build()

        self.window.mainloop()