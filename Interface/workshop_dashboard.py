import tkinter as tk

from Core.workshop_brain import WorkshopBrain
from Interface.memory_room import open_memory_room 
from Interface.project_room import open_project_room
from Interface.task_chamber import open_task_chamber

class WorkshopDashboard:

    def __init__(self):

        self.brain = WorkshopBrain()

        self.window = tk.Tk()

        self.window.title(
            "🌿 AURORA Workshop"
        )

        self.window.geometry(
            "700x500"
        )


    def load_workshop(self):

        self.brain.awaken()

        summary = self.brain.get_workshop_summary()

        return summary


    def build(self):

        self.window.configure(
            bg="#101820"
        )

        title = tk.Label(
            self.window,
            text="🌿 AURORA",
            font=(
                "Helvetica",
                24
            )
        )

        title.pack(
            pady=20
        )


        subtitle = tk.Label(
            self.window,
            text="The Workshop is awake.",
            font=(
                "Helvetica",
                14
            )
        )

        subtitle.pack()

        menu = tk.Frame(
            self.window
        )

        menu.pack(
            pady=10
        )


        buttons = [
            ("📚 Projects", open_project_room),
            ("📋 Tasks", open_task_chamber),
            ("📖 Journal", None),
            ("🌱 Memory Garden", open_memory_room),
            ("🌙 Reflection", None),
            ("⚙ Health", None)
        ]


        for text, command in buttons:

            tk.Button(
                menu,
                text=text,
                width=20,
                command=command
            ).pack(
                pady=3
            )


        summary = self.load_workshop()


        summary_box = tk.Text(
            self.window,
            height=15,
            width=70
        )

        summary_box.pack(
            pady=20
        )


        for line in summary:

            summary_box.insert(
                tk.END,
                line + "\n"
            )


        summary_box.config(
            state="disabled"
        )


    def run(self):

        self.build()

        self.window.mainloop()