import customtkinter as ctk
import json
import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(BASE_DIR)

MEMORY_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "memories.json"
)

MOMENTS_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "moments.json"
)

TASK_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "tasks.json"
)

from project_room import open_project_room
from memory_room import open_memory_room
from Interface.task_chamber import open_task_room
from Design.aurora_theme import (
    apply_theme,
    title_style,
    button_style
)
from Core.aurora_boot import run_boot_sequence

def load_data(path):
    
    if os.path.exists(path):

        with open(path, "r") as file:
            return json.load(file)
        
    return{}

def get_dashboard():

    memory = load_data(MEMORY_FILE)

    moments = load_data(MOMENTS_FILE)

    tasks = load_data(TASK_FILE)

    projects = memory.get("projects", [])

    task_list = tasks.get("tasks", [])

    memory_moments = moments.get("moments", [])


    return f"""
📚 Creations: {len(projects)}

📋 Tasks Waiting: {len(task_list)}

🌱 Memories Preserved: {len(memory_moments)}

━━━━━━━━━━━━━━

Current Focus:
Faerie Veil
"""

# Aurora appearance
apply_theme()

run_boot_sequence()

window = ctk.CTk(
    fg_color="#1B241B"
)

window.title("🌿 Aurora Workshop")

window.geometry("700x700")


title = ctk.CTkLabel(
    window,
    text="🌿 AURORA WORKSHOP 🌿",
    **title_style()
)

title.pack(pady=40)


message = ctk.CTkLabel(
    window,
    text=get_dashboard(),
    font=("Arial", 18)
)

message.pack(pady=20)

project_button = ctk.CTkButton(
    window,
    text="📚 Projects",
    font=("Arial", 16),
    command=open_project_room,
    **button_style()
)

project_button.pack(pady=10)


task_button = ctk.CTkButton(
    window,
    text="📋 Tasks",
    font=("Arial", 16),
    command=open_task_room,
    **button_style()
)

task_button.pack(pady=10)


memory_button = ctk.CTkButton(
    window,
    text="🌱 Memory Garden",
    font=("Arial", 16),
    command=open_memory_room,
    **button_style()
)

memory_button.pack(pady=10)

window.mainloop()
