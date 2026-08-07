import customtkinter as ctk
import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

from Design.aurora_theme import (
    apply_theme,
    title_style
)

MEMORY_FILE = os.path.join(
    BASE_DIR,
    "Memory",
    "moments.json"
)


def load_memories():

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    return {}


def open_memory_room():

    apply_theme()

    room = ctk.CTkToplevel(
        fg_color="#1B241B"
    )

    room.title("🌱 Memory Garden")

    room.geometry("650x600")


    title = ctk.CTkLabel(
        room,
        text="🌱 MEMORY GARDEN",
        **title_style()
    )

    title.pack(pady=20)


    data = load_memories()

    memories = data.get("moments", [])


    for memory in memories:

        card = ctk.CTkLabel(
            room,
            text=(
                f"✨ {memory['category']}\n"
                f"{memory['description']}"
            ),
            font=("Arial", 16),
            wraplength=550
        )

        card.pack(pady=15)