# Linux Mint Widget Timer
A lightweight desktop widget for Linux Mint that displays a persistent countdown timer.
Designed to stay out of the way while quietly holding you accountable.

# Features
Always-on-top desktop widget
Clean, Linux-native dark theme
Draggable window with close (✕) button
Displays days remaining in a countdown
Persists state across reboots
Remembers start date
Restores last screen position
Optional auto-start on login

# How It Works
The widget records the start date on first run
Remaining days are calculated dynamically (no background timer required)
State is stored locally in a small state.json file
Closing or rebooting does not reset the countdown

# Usage
Run the widget manually:
python3 widget.py
To start automatically on login, add it to your Linux Mint autostart configuration.

# Files
widget.py – main application
state.json – persistent state (auto-generated)

# Requirements
Linux Mint (Cinnamon)
Python 3
Tkinter (usually included with Python)

If Tkinter is missing:

sudo apt install python3-tk

# Use Cases
30-day Linux challenge

# Habit tracking
Quiet accountability reminders
Lightweight desktop motivation tools

# Notes

Transparency support depends on your window manager and compositor
Designed for simplicity — not a full task or timer suite


mkdir -p ~/.config/autostart
nano ~/.config/autostart/widget_timer.desktop

[Desktop Entry]
Type=Application
Exec=python3 /home/YOURUSER/widget_timer/widget.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Linux Mint Challange
