import json

THEME_PATH = "/opt/shellos/core/config/theme.json"

with open(THEME_PATH, "r") as f:
    THEME = json.load(f)

def get_color(name):
    return THEME["colors"].get(name, "#FFFFFF")

def get_icon_style():
    return THEME["icons"]

def animations_enabled():
    return THEME["animations"]
