"""
=========================================
AURORA - Task Chamber

The Task Chamber allows User to:

• View quests
• Complete quests
• Review completed quests
• Add New Quest
• Add Notes to Quest
• Edit Quest
• Due Dates
• Due Dates
• Priority Visuals

Future Features
---------------
• Search & Filters
=========================================
"""

import customtkinter as ctk
import json
import os
from datetime import datetime

from Core.workshop_brain import WorkshopBrain

from Design.aurora_theme import (
    apply_theme,
    title_style,
    header_style,
    body_style,
    button_style,
    card_style,
    AURORA_DARK,
    AURORA_GLOW,
    AURORA_PANEL,
    AURORA_GREEN,
    AURORA_GOLD
)

# =========================================
# File Paths
# =========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

TASK_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "tasks.json"
)

brain = WorkshopBrain()

brain.awaken()

# =========================================
# Data Functions
# =========================================

# TODO:
# Remove these wrappers after all Task Chamber
# functions call WorkshopBrain directly.

def load_tasks():

    return brain.get_tasks()


def save_tasks(tasks):

    brain.tasks["tasks"] = tasks

    brain.save_tasks()


# =========================================
# Utility Functions
# =========================================

def clear_window(window):

    for widget in window.winfo_children():
        widget.destroy()

def create_task_button(parent, main_window, task, symbol):

    # -----------------------------
    # Quest Card
    # -----------------------------

    card = ctk.CTkFrame(
        parent,
        **card_style()
    )

    card.pack(
        fill="x",
        padx=20,
        pady=6
    )


    # -----------------------------
    # Header
    # -----------------------------

    header = ctk.CTkLabel(
        card,
        text="QUEST RECORD",
        font=("PT Sans", 12, "bold"),
        text_color=AURORA_GLOW,
        anchor="w"
    )

    header.pack(
        anchor="w",
        padx=15,
        pady=(12, 2)
    )


    # -----------------------------
    # Quest Title
    # -----------------------------

    title = ctk.CTkLabel(
        card,
        text=task["title"],
        font=("PT Serif", 20, "bold"),
        text_color=AURORA_GLOW,
        anchor="w",
        justify="left"
    )

    title.pack(
        anchor="w",
        padx=15
    )


    # -----------------------------
    # Project
    # -----------------------------

    project_label = ctk.CTkLabel(
        card,
        text=(
            f"PROJECT   {task.get('project', 'Unknown')}"
        ),
        justify="left",
        anchor="w",
        **body_style()
    )

    project_label.pack(
        anchor="w",
        padx=15,
        pady=(6, 2)
    )

    info_row = ctk.CTkFrame(
        card,
        fg_color="transparent"
    )

    info_row.pack(
        fill="x",
        padx=15,
        pady=(6, 2)
    )


    # -----------------------------
    # Priority
    # -----------------------------

    priority = task.get(
        "priority",
        "Unknown"
    )

    priority_colors = {
        "High": "#D96C6C",
        "Medium": "#D9B95B",
        "Low": "#7FAF8A"
    }

    priority_color = priority_colors.get(
        priority,
        "white"
    )

    priority_label = ctk.CTkLabel(
        info_row,
        text=f"PRIORITY  {priority.upper()}",
        font=("PT Sans", 14, "bold"),
        text_color=priority_color,
        anchor="w"
    )

    priority_label.pack(
        side="left",
        padx=(0, 30),
        pady=2
    )


    # -----------------------------
    # Due Date
    # -----------------------------

    due_date = task.get(
        "due_date",
        ""
    )

    if due_date:

        due_text = f"DUE DATE  {due_date}"

    else:

        due_text = "DUE DATE  None"


    due_label = ctk.CTkLabel(
        card,
        text=due_text,
        font=("PT Sans", 14),
        text_color="white",
        anchor="w"
    )

    due_label.pack(
        anchor="w",
        padx=15,
        pady=2
    )


    # -----------------------------
    # Status
    # -----------------------------

    status = task.get(
        "status",
        "Not Started"
    )

    status_label = ctk.CTkLabel(
        info_row,
        text=f"STATUS  {status.upper()}",
        font=("PT Sans", 12),
        text_color="white",
        anchor="w"
    )

    status_label.pack(
        side="left",
        pady=2
    )


    # -----------------------------
    # Button
    # -----------------------------

    open_button = ctk.CTkButton(
        card,
        text="Access Record",
        width=140,
        command=lambda: show_task_details(
            main_window,
            task
        ),
        **button_style()
    )

    open_button.pack(
        anchor="e",
        padx=15,
        pady=(8, 10)
    )
# =========================================
# Task Actions
# =========================================

def complete_task(task):

    brain.complete_task(task)

# =========================================
# Dialogs
# =========================================

def finish_complete_task(dialog, window, task):

    complete_task(task)

    dialog.destroy()

    show_task_list(window)

def confirm_complete_task(window, task):

    dialog = ctk.CTkToplevel(window)

    dialog.title("Complete Quest")
    dialog.geometry("400x220")

    dialog.configure(
        fg_color=AURORA_DARK
    )

    dialog.grab_set()

    message = ctk.CTkLabel(
        dialog,
        text=(
            "Complete this quest?\n\n"
            f"{task['title']}\n\n"
            "This task will be moved to\n"
            "Completed Records."
        ),
        justify="center",
        **body_style()
    )

    message.pack(
        pady=20
    )

    confirm_button = ctk.CTkButton(
        dialog,
        text="Confirm",
        command=lambda: finish_complete_task(
            dialog,
            window,
            task
        ),
        **button_style()
    )

    confirm_button.pack(
        pady=10
    )

    cancel_button = ctk.CTkButton(
        dialog,
        text="Cancel",
        command=dialog.destroy,
        **button_style()
    )

    cancel_button.pack()

def finish_delete_task(dialog, window, task):

    brain.delete_task(task)

    dialog.destroy()

    show_task_list(window)

def confirm_delete_task(window, task):

    dialog = ctk.CTkToplevel(window)

    dialog.title("Remove Quest")
    dialog.geometry("400x220")

    dialog.configure(
        fg_color=AURORA_DARK
    )

    dialog.grab_set()

    message = ctk.CTkLabel(
        dialog,
        text=(
            "Remove this Quest?\n\n"
            f"{task['title']}\n\n"
            "This Quest will be permanently\n"
            "removed from the Workshop."
        ),
        justify="center",
        **body_style()
    )

    message.pack(
        pady=20
    )

    remove_button = ctk.CTkButton(
        dialog,
        text="Remove Quest",
        command=lambda: finish_delete_task(
            dialog,
            window,
            task
        ),
        **button_style()
    )

    remove_button.pack(
        pady=10
    )

    cancel_button = ctk.CTkButton(
        dialog,
        text="Cancel",
        command=dialog.destroy,
        **button_style()
    )

    cancel_button.pack()

# =========================================
# Views
# =========================================
def show_task_details(window, task):

    apply_theme()

    clear_window(window)

    window.configure(
        fg_color=AURORA_DARK
    )

    title = ctk.CTkLabel(
        window,
        text="Task Details",
        **title_style()
    )

    title.pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(
        window,
        width=650,
        height=450,
        fg_color=AURORA_DARK
    )

    scroll_frame.pack(
        padx=20,
        pady=(0, 20),
        fill="both",
        expand=True
    )

    notes = task.get("notes", [])

    if notes:
        notes_text = "\n".join(
            f"• {note}" for note in notes
        )
    else:
        notes_text = "No notes yet."

    task_summary = (
        f"{task['title']}\n\n"
        f"Project: {task.get('project', 'Unknown')}\n"
        f"Priority: {task.get('priority', 'Unknown')}\n"
        f"Due Date: {task.get('due_date', 'No due date')}\n"
        f"Created: {task.get('created', 'Unknown')}\n\n"
        f"Why:\n{task.get('why', 'No reason added')}\n\n"
        f"Notes:\n{notes_text}"
    )

    details = ctk.CTkLabel(
        scroll_frame,
        text=task_summary,
        justify="left",
        anchor="w",
        **body_style()
    )

    details.pack(
        padx=30,
        pady=20,
        anchor="w"
    )

    edit_button = ctk.CTkButton(
        scroll_frame,
        text="Edit Quest",
        command=lambda: show_edit_task_page(window, task),
        **button_style()
    )

    edit_button.pack(
        pady=10
    )

    delete_button = ctk.CTkButton(
        scroll_frame,
        text="Remove Quest",
        command=lambda: confirm_delete_task(
            window,
            task
        ),
        **button_style()
    )

    delete_button.pack(
        pady=10
    )

    complete_button = ctk.CTkButton(
        scroll_frame,
        text="Complete Quest",
        command=lambda: confirm_complete_task(
            window,
            task
        ),
        **button_style()
    )

    complete_button.pack(
        pady=10
    )

    back_button = ctk.CTkButton(
        scroll_frame,
        text="Back to Tasks",
        command=lambda: show_task_list(window),
        **button_style()
    )

    back_button.pack(
        pady=10
    )

def show_completed_tasks(window):

    clear_window(window)

    window.configure(
        fg_color=AURORA_DARK
    )

    title = ctk.CTkLabel(
        window,
        text="Completed Records",
        **title_style()
    )

    title.pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(
        window,
        width=650,
        height=450,
        fg_color=AURORA_DARK
    )

    scroll_frame.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )

    completed_tasks = brain.get_completed_tasks()

    completed_title = ctk.CTkLabel(
        scroll_frame,
        text="Archived Quests",
        **header_style()
    )

    completed_title.pack(
        pady=10
    )

    for task in completed_tasks:

        create_task_button(
            scroll_frame,
            window,
            task,
            "✓"
        )

    back_button = ctk.CTkButton(
        window,
        text="Back to Task Chamber",
        command=lambda: show_task_list(window),
        **button_style()
    )

    back_button.pack(
        pady=(0, 20)
    )

def search_tasks(search_text, project=None):

    tasks = brain.get_tasks()

    search_text = search_text.lower().strip()

    results = []

    for task in tasks:

        if project is not None:

            if task.get("project") != project:
                continue

        if task.get("completed", False):
            continue
        title = task.get("title", "").lower()
        task_project = task.get("project", "").lower()
        priority = task.get("priority", "").lower()
        status = task.get("status", "").lower()

        if (
            search_text in title
            or search_text in task_project
            or search_text in priority
            or search_text in status
        ):
            results.append(task)

    return results

def show_task_list(
        window,
        project=None,
        include_title=False,
        search_text=""
    ):

    clear_window(window)

    window.configure(
        fg_color=AURORA_DARK
    )

    title = ctk.CTkLabel(
        window,
        text="Task Chamber",
        **title_style()
    )

    title.pack(
        pady=20
    )

    search_frame = ctk.CTkFrame(
        window,
        fg_color="transparent"
    )

    search_frame.pack(
        fill="x",
        padx=20,
        pady=(0, 10)
    )

    search_entry = ctk.CTkEntry(
        search_frame,
        width=400,
        placeholder_text="Search quests...",
        fg_color=AURORA_PANEL,
        text_color="white",
        border_color=AURORA_GREEN
    )

    search_entry.pack(
        side="left",
        padx=(0, 10)
    )

    search_entry.insert(
        0,
        search_text
    )

    search_button = ctk.CTkButton(
        search_frame,
        text="Search",
        command=lambda: show_task_list(
            window,
            project,
            include_title,
            search_entry.get()
        ),
        **button_style()
    )

    search_button.pack(
        side="left"
    )

    new_task_button = ctk.CTkButton(
        window,
        text="New Quest",
        command=lambda: show_new_task_page(window),
        **button_style()
    )

    new_task_button.pack(
        pady=(0, 10)
    )

    completed_button = ctk.CTkButton(
        window,
        text="Completed Records",
        command=lambda: show_completed_tasks(window),
        **button_style()
    )

    completed_button.pack(
        pady=(0, 20)
    )

    scroll_frame = ctk.CTkScrollableFrame(
        window,
        width=650,
        height=450,
        fg_color=AURORA_DARK
    )

    scroll_frame.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )

    # -----------------------------------------
    # Get Tasks From WorkshopBrain
    # -----------------------------------------

    if search_text:

        tasks = search_tasks(
            search_text,
            project
        )

    else:

        tasks = brain.get_tasks()

    active_tasks = []

    for task in tasks:

        if project is not None:

            if task.get("project") != project:
                continue

        if not task.get("completed", False):

            active_tasks.append(task)

    # -----------------------------------------
    # Active Quests
    # -----------------------------------------

    active_title = ctk.CTkLabel(
        scroll_frame,
        text="Active Quests",
        **header_style()
    )

    active_title.pack(
        pady=10
    )

    for task in active_tasks:

        create_task_button(
            scroll_frame,
            window,
            task,
            "○"
        )

def create_new_task(
    window,
    title_entry,
    project_entry,
    priority_menu,
    due_date_entry,
    why_entry,
    notes_entry
):

    new_task = {
        "title": title_entry.get(),
        "project": project_entry.get(),
        "priority": priority_menu.get(),
        "status": "Not Started",
        "created": datetime.now().strftime("%Y-%m-%d"),
        "due_date": due_date_entry.get(),
        "completed": False,
        "why": why_entry.get("1.0", "end-1c"),
        "notes": notes_entry.get("1.0", "end-1c").split("\n")
    }

    brain.add_task(new_task)

    show_task_list(window)

def show_new_task_page(window):

    clear_window(window)

    title = ctk.CTkLabel(
        window,
        text="Record a New Quest",
        **title_style()
    )

    title.pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(
        window,
        width=620,
        height=420,
        fg_color=AURORA_DARK
    )

    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 20)
    )


    quest_title_label = ctk.CTkLabel(
        scroll_frame,
        text="Quest Title"
    )

    quest_title_label.pack(pady=5)


    quest_title_entry = ctk.CTkEntry(
        scroll_frame,
        width=400,
        placeholder_text="Enter quest name...",
        fg_color=AURORA_PANEL,
        text_color="white",
        border_color=AURORA_GREEN
    )

    quest_title_entry.pack(pady=5)

    project_label = ctk.CTkLabel(
        scroll_frame,
        text="Project",
        **body_style()
    )

    project_label.pack(pady=5)

    project_entry = ctk.CTkEntry(
        scroll_frame,
        width=400,
        placeholder_text="Example: Aurora, Faerie Veil...",
        fg_color=AURORA_PANEL,
        text_color="white",
        border_color=AURORA_GREEN
    )

    project_entry.pack(pady=5)


    priority_label = ctk.CTkLabel(
        scroll_frame,
        text="Priority"
    )

    priority_label.pack(pady=5)


    priority_menu = ctk.CTkOptionMenu(
        scroll_frame,
        values=[
            "Low",
            "Medium",
            "High"
        ],
        fg_color=AURORA_GREEN,
        button_color=AURORA_GREEN,
        button_hover_color=AURORA_GOLD,
        text_color="white"
    )

    priority_menu.set("Medium")

    priority_menu.pack(pady=5)

    due_date_label = ctk.CTkLabel(
        scroll_frame,
        text="Due Date"
    )

    due_date_label.pack(pady=5)

    due_date_entry = ctk.CTkEntry(
        scroll_frame,
        width=400,
        placeholder_text="YYYY-MM-DD",
        fg_color=AURORA_PANEL,
        text_color="white",
        border_color=AURORA_GREEN
    )

    due_date_entry.pack(pady=5)

    why_label = ctk.CTkLabel(
        scroll_frame,
        text="Why does this quest matter?"
    )

    why_label.pack(pady=5)


    why_entry = ctk.CTkTextbox(
        scroll_frame,
        width=400,
        height=100,
        fg_color=AURORA_PANEL,
        text_color="white",
        border_width=1,
        border_color=AURORA_GREEN
    )

    why_entry.pack(pady=5)

    notes_label = ctk.CTkLabel(
        scroll_frame,
        text="Notes"
    )

    notes_label.pack(pady=5)


    notes_entry = ctk.CTkTextbox(
        scroll_frame,
        width=400,
        height=100,
        fg_color=AURORA_PANEL,
        text_color="white",
        border_width=1,
        border_color=AURORA_GREEN
    )

    notes_entry.pack(pady=5)

    create_button = ctk.CTkButton(
        scroll_frame,
        text="Create Quest",
        command=lambda: create_new_task(
            window,
            quest_title_entry,
            project_entry,
            priority_menu,
            due_date_entry,
            why_entry,
            notes_entry
        ),
        **button_style()
    )

    create_button.pack(pady=20)

    back_button = ctk.CTkButton(
        scroll_frame,
        text="← Back",
        command=lambda: show_task_list(window),
        **button_style()
    )
    
    back_button.pack(pady=20)
    

def show_edit_task_page(window, task):

    clear_window(window)

    title = ctk.CTkLabel(
        window,
        text="Edit Quest",
        **title_style()
    )

    title.pack(pady=20)


    quest_title_entry = ctk.CTkEntry(
        window,
        width=400,
        fg_color=AURORA_PANEL,
        text_color="white",
        border_color=AURORA_GREEN
    )

    quest_title_entry.insert(
        0,
        task["title"]
    )

    quest_title_entry.pack(pady=5)


    project_entry = ctk.CTkEntry(
        window,
        width=400,
        fg_color=AURORA_PANEL,
        text_color="white",
        border_color=AURORA_GREEN
    )

    project_entry.insert(
        0,
        task.get("project", "")
    )

    project_entry.pack(pady=5)


    priority_menu = ctk.CTkOptionMenu(
        window,
        values=[
            "Low",
            "Medium",
            "High"
        ],
        fg_color=AURORA_GREEN,
        button_color=AURORA_GREEN,
        button_hover_color=AURORA_GOLD,
        text_color="white"
    )

    priority_menu.set(
        task.get(
            "priority",
            "Medium"
        )
    )

    priority_menu.pack(pady=5)

    due_date_label = ctk.CTkLabel(
        window,
        text="Due Date"
    )

    due_date_label.pack(pady=5)

    due_date_entry = ctk.CTkEntry(
        window,
        width=400,
        placeholder_text="YYYY-MM-DD",
        fg_color=AURORA_PANEL,
        text_color="white",
        border_color=AURORA_GREEN
    )

    due_date_entry.insert(
        0,
        task.get(
            "due_date",
            ""
        )
    )

    due_date_entry.pack(pady=5)

    why_entry = ctk.CTkTextbox(
        window,
        width=400,
        height=100,
        fg_color=AURORA_PANEL,
        text_color="white",
        border_width=1,
        border_color=AURORA_GREEN
    )

    why_entry.insert(
        "1.0",
        task.get(
            "why",
            ""
        )
    )

    why_entry.pack(pady=5)


    notes_entry = ctk.CTkTextbox(
        window,
        width=400,
        height=100,
        fg_color=AURORA_PANEL,
        text_color="white",
        border_width=1,
        border_color=AURORA_GREEN
    )

    notes_entry.insert(
        "1.0",
        "\n".join(
            task.get(
                "notes",
                []
            )
        )
    )

    notes_entry.pack(pady=5)

    save_button = ctk.CTkButton(
        window,
        text="Save Changes",
        command=lambda: save_edited_task(
            window,
            task,
            quest_title_entry,
            project_entry,
            priority_menu,
            due_date_entry,
            why_entry,
            notes_entry
        ),
        **button_style()
    )

    save_button.pack(pady=20)

def save_edited_task(
    window,
    old_task,
    title_entry,
    project_entry,
    priority_menu,
    due_date_entry,
    why_entry,
    notes_entry
):

    updated_task = {

        "title": title_entry.get(),

        "project": project_entry.get(),

        "priority": priority_menu.get(),

        "due_date": due_date_entry.get(),

        "why": why_entry.get(
            "1.0",
            "end-1c"
        ),

        "notes": notes_entry.get(
            "1.0",
            "end-1c"
        ).split("\n")

    }


    brain.update_task(
        old_task,
        updated_task
    )


    show_task_list(window)

# =========================================
# Launcher
# =========================================

def open_task_chamber():

    window = ctk.CTkToplevel()

    window.title("Task Chamber")
    window.geometry("700x600")

    show_task_list(
        window,
        include_title=False
    )