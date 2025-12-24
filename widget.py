import tkinter as tk
from datetime import date
import json
import os

# ==================================================
# CONFIG
# ==================================================
TOTAL_DAYS = 30

# State file lives next to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(SCRIPT_DIR, "state.json")

# ==================================================
# REMEMBERED STATE
# ==================================================
state = {}

if os.path.exists(STATE_FILE):
    try:
        with open(STATE_FILE, "r") as f:
            content = f.read().strip()
            if content:
                state = json.loads(content)
    except Exception:
        state = {}

# Initialize required fields safely
if "start_date" not in state:
    state["start_date"] = date.today().isoformat()

if "x" not in state:
    state["x"] = 120

if "y" not in state:
    state["y"] = 120

# Always write back a valid state file
with open(STATE_FILE, "w") as f:
    json.dump(state, f, indent=2)

START_DATE = date.fromisoformat(state["start_date"])
WIN_X = state["x"]
WIN_Y = state["y"]

def save_position(x, y):
    state["x"] = x
    state["y"] = y
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def days_remaining():
    elapsed = (date.today() - START_DATE).days
    return max(TOTAL_DAYS - elapsed, 0)

# ==================================================
# WINDOW
# ==================================================
root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)

# Transparency (best-effort under Cinnamon)
try:
    root.attributes("-alpha", 0.85)
except tk.TclError:
    pass

root.geometry(f"360x130+{WIN_X}+{WIN_Y}")
root.configure(bg="#1c1f26")

# ==================================================
# DRAGGING
# ==================================================
def start_move(e):
    root.x = e.x
    root.y = e.y

def do_move(e):
    x = e.x_root - root.x
    y = e.y_root - root.y
    root.geometry(f"+{x}+{y}")
    save_position(x, y)

# ==================================================
# HEADER
# ==================================================
header = tk.Frame(root, bg="#232732", height=34)
header.pack(fill="x")
header.bind("<Button-1>", start_move)
header.bind("<B1-Motion>", do_move)

title = tk.Label(
    header,
    text="🐧  Linux Mint Challenge",
    bg="#232732",
    fg="#f5f7fa",
    font=("Segoe UI", 11, "bold")
)
title.pack(side="left", padx=10)

close_btn = tk.Label(
    header,
    text="✕",
    bg="#232732",
    fg="#ff6b6b",
    font=("Segoe UI", 11),
    cursor="hand2"
)
close_btn.pack(side="right", padx=10)
close_btn.bind("<Button-1>", lambda e: root.destroy())

# ==================================================
# BODY
# ==================================================
body = tk.Frame(root, bg="#1c1f26")
body.pack(expand=True, fill="both")

main = tk.Label(
    body,
    text=f"{days_remaining()} days remaining",
    bg="#1c1f26",
    fg="#ffffff",
    font=("Segoe UI", 20, "bold")
)
main.pack(expand=True)

# ==================================================
# REFRESH
# ==================================================
def refresh():
    main.config(text=f"{days_remaining()} days remaining")
    root.after(3_600_000, refresh)  # hourly refresh

refresh()
root.mainloop()
