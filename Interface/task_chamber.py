"""
=========================================
AURORA - Task Chamber

The Task Chamber allows Moss to:

• View quests
• Complete quests
• Review completed quests
• Add New Quest
• Add Notes to Quest

Future Features
---------------
• Edit Quest
• Due Dates
• Search & Filters
• Scrollable
• Due Dates
• Priority Visuals
=========================================
"""

import customtkinter as ctk
import json
import os

from Core.workshop_brain import WorkshopBrain

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
        corner_radius=12
    )

    card.pack(
        fill="x",
        padx=20,
        pady=10
    )


    # -----------------------------
    # Header
    # -----------------------------

    header = ctk.CTkLabel(
        card,
        text="◈ QUEST RECORD",
        font=("Arial", 12, "bold"),
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
        font=("Arial", 20, "bold"),
        anchor="w",
        justify="left"
    )

    title.pack(
        anchor="w",
        padx=15
    )


    # -----------------------------
    # Information
    # -----------------------------

    info = ctk.CTkLabel(
        card,
        text=(
            f"PROJECT LINK\n"
            f"{task.get('project', 'Unknown')}\n\n"
            f"PRIORITY MATRIX\n"
            f"{task.get('priority', 'Unknown')}"
        ),
        justify="left",
        anchor="w",
        font=("Arial", 14)
    )

    info.pack(
        anchor="w",
        padx=15,
        pady=(10, 10)
    )


    # -----------------------------
    # Status
    # -----------------------------

    status = "ARCHIVED" if task.get("completed") else "ACTIVE"

    status_label = ctk.CTkLabel(
        card,
        text=f"STATUS: {status}",
        font=("Arial", 12)
    )

    status_label.pack(
        anchor="w",
        padx=15
    )


    # -----------------------------
    # Button
    # -----------------------------

    open_button = ctk.CTkButton(
        card,
        text="Access Record",
        width=140,
        command=lambda: show_task_details(main_window, task)
    )

    open_button.pack(
        anchor="e",
        padx=15,
        pady=15
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

    dialog.grab_set()

    message = ctk.CTkLabel(
        dialog,
        text=(
            "Complete this quest?\n\n"
            f"{task['title']}\n\n"
            "This task will be moved to\n"
            "Completed Records."
        ),
        justify="center"
    )

    message.pack(pady=20)

    confirm_button = ctk.CTkButton(
        dialog,
        text="Confirm",
        command=lambda: finish_complete_task(dialog, window, task)
    )

    confirm_button.pack(pady=10)

    cancel_button = ctk.CTkButton(
        dialog,
        text="Cancel",
        command=dialog.destroy
    )

    cancel_button.pack()

def finish_delete_task(Dialog, window, task):

    brain.delete_task(task)

    dialog.destroy()

    show_task_list(window)

def confirm_delete_task(window, task):

    dialog = ctk.CTkToplevel(window)

    dialog.title("Remove Quest")
    dialog.geometry("400x220")

    dialog.grab_set()

    message = ctk.CTkLabel(
        dialog,
        text=(
            "Remove this Quest?\n\n"
            f"{task['title']}\n\n"
            "This Quest will be permanemtly\n"
            "removed from the Workshop."
        ),
        justify="center"
    )

    message.pack(pady=20)

    remove_button = ctk.CTkButton(
        dialog,
        text="Remove Quest",
        command=lambda: finish_delete_task(
            dialog,
            window,
            task
        )
    )

    remove_button.pack(pady=10)

    cancel_button = ctk.CTkButton(

        dialog,
        text="Cancel",
        command=dialog.destroy
    )

    cancel_button.pack()


# =========================================
# Views
# =========================================

def show_task_details(window, task):

    clear_window(window)

    title = ctk.CTkLabel(
        window,
        text="🕯️ Task Details",
        font=("Arial", 28)
    )

    title.pack(pady=20)

    notes = task.get("notes", [])

    if notes:
        notes_text = "\n".join(f"• {note}" for note in notes)
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
        window,
        text=task_summary,
        justify="left",
        anchor="w"
    )

    details.pack(
        padx=30,
        pady=20
    )

    edit_button = ctk.CTkButton(
        window,
        text="Edit Quest",
        command=lambda: show_edit_task_page(window, task)
    )

    edit_button.pack(pady=10)

    delete_button = ctk.CTkButton(
        window,
        text="Remove Quest",
        command=lambda: confirm_complete_task(
            window,
            task
        )
    )

    delete_button.pack(pady=10)

    complete_button = ctk.CTkButton(
        window,
        text="✓ Complete Quest",
        command=lambda: confirm_complete_task(window, task)
    )

    complete_button.pack(pady=10)

    back_button = ctk.CTkButton(
        window,
        text="← Back to Tasks",
        command=lambda: show_task_list(window)
    )

    back_button.pack(pady=10)


def show_task_list(window, project=None, include_title=False):

    clear_window(window)

    title = ctk.CTkLabel(
        window,
        text="🕯️ Task Chamber",
        font=("Arial", 28)
    )

    title.pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(
        window,
        width=650,
        height=450
    )

    scroll_frame.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )

    new_task_button = ctk.CTkButton(
        window,
        text="✨ New Quest",
        command=lambda: show_new_task_page(window)
    )

    new_task_button.pack(pady=(0, 20))

    tasks = load_tasks()

    active_tasks = []
    completed_tasks = []

    for task in tasks:

        if project is not None:

            if task.get("project") != project:
                continue

        if task.get("completed"):
            completed_tasks.append(task)
        else:
            active_tasks.append(task)

    active_title = ctk.CTkLabel(
        scroll_frame,
        text="◈ Active Quests",
        font=("Arial", 22)
    )

    active_title.pack(pady=10)

    for task in active_tasks:
        create_task_button(
            scroll_frame, 
            window,
            task,
            "○")

    completed_title = ctk.CTkLabel(
        scroll_frame,
        text="◈ Completed Records",
        font=("Arial", 22)
    )

    completed_title.pack(pady=20)

    for task in completed_tasks:
        create_task_button(
            scroll_frame, 
            window,
            task,
            "✓")

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
        "created": "2026-07-19",
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
        text="✨ Record a New Quest",
        font=("Arial", 28)
    )

    title.pack(pady=20)

    scroll_frame = ctk.CTkScrollableFrame(
        window,
        width=620,
        height=420
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
        placeholder_text="Enter quest name..."
    )

    quest_title_entry.pack(pady=5)

    project_label = ctk.CTkLabel(
        scroll_frame,
        text="Project"
    )

    project_label.pack(pady=5)

    project_entry = ctk.CTkEntry(
        scroll_frame,
        width=400,
        placeholder_text="Example: Aurora, Faerie Veil..."
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
        ]
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
        placeholder_text="YYYY-MM-DD"
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
        height=100
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
        height=100
    )

    notes_entry.pack(pady=5)

    create_button = ctk.CTkButton(
        scroll_frame,
        text="✨ Create Quest",
        command=lambda: create_new_task(
            window,
            quest_title_entry,
            project_entry,
            priority_menu,
            due_date_entry,
            why_entry,
            notes_entry
        )
    )

    create_button.pack(pady=20)

    back_button = ctk.CTkButton(
        scroll_frame,
        text="← Back",
        command=lambda: show_task_list(window)
    )
    
    back_button.pack(pady=20)
    

def show_edit_task_page(window, task):

    clear_window(window)

    title = ctk.CTkLabel(
        window,
        text="✏️ Edit Quest",
        font=("Arial", 28)
    )

    title.pack(pady=20)


    quest_title_entry = ctk.CTkEntry(
        window,
        width=400
    )

    quest_title_entry.insert(
        0,
        task["title"]
    )

    quest_title_entry.pack(pady=5)


    project_entry = ctk.CTkEntry(
        window,
        width=400
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
        ]
    )

    priority_menu.set(
        task.get(
            "priority",
            "Medium"
        )
    )

    priority_menu.pack(pady=5)


    why_entry = ctk.CTkTextbox(
        window,
        width=400,
        height=100
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
        height=100
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
        text="💾 Save Changes",
        command=lambda: save_edited_task(
            window,
            task,
            quest_title_entry,
            project_entry,
            priority_menu,
            why_entry,
            notes_entry
        )
    )

    save_button.pack(pady=20)

def save_edited_task(
    window,
    old_task,
    title_entry,
    project_entry,
    priority_menu,
    why_entry,
    notes_entry
):

    updated_task = {

        "title": title_entry.get(),

        "project": project_entry.get(),

        "priority": priority_menu.get(),

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