import customtkinter as ctk


# =========================================
# Aurora Colors
# =========================================

AURORA_GREEN = "#6B8E6B"
AURORA_DARK = "#1B241B"
AURORA_PANEL = "#273327"
AURORA_GLOW = "#A8D8A8"
AURORA_GOLD = "#C9A227"


# =========================================
# Aurora Typography
# =========================================

TITLE_FONT = ("Apple Chancery", 30)

HEADER_FONT = ("PT Serif", 20, "bold")

BODY_FONT = ("PT Sans", 16)

BUTTON_FONT = ("PT Sans", 15, "bold")


# =========================================
# Aurora Theme
# =========================================

def apply_theme():

    ctk.set_appearance_mode("dark")

    ctk.set_default_color_theme(
        "green"
    )


def title_style():

    return {
        "font": TITLE_FONT,
        "text_color": AURORA_GLOW
    }

def header_style():

    return {
        "font": HEADER_FONT,
        "text_color": AURORA_GLOW
    }

def body_style():

    return {
        "font": BODY_FONT,
        "text_color": "white"
    }


def button_style():

    return {
        "fg_color": AURORA_GREEN,
        "hover_color": AURORA_GOLD,
        "text_color": "white",
        "corner_radius": 12,
        "height": 42,
        "font": BUTTON_FONT
    }


def card_style():

    return {
        "fg_color": AURORA_PANEL,
        "corner_radius": 12
    }