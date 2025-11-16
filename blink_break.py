import time 
import threading
import sys
import json
import os
import tkinter as tk
from tkinter import simpledialog
import pystray
from PIL import Image
from pystray import MenuItem as item
from plyer import notification

# SETTINGS FILE
SETTINGS_FILE = 'settings.json'

# GLOBALS
running = True
settings = {}

# Load settings
def load_settings():
    global settings
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
        print("✅ Settings loaded:", settings)
    else:
        settings = {
            "break_interval_minutes": 5,
            "break_duration_minutes": 5,
            "sound_enabled": True,
            "notifications_enabled": True,
            "window_transparency": 0.9
        }
        save_settings()

# Save settings
def save_settings():
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)
    print("✅ Settings saved.")

# Play simple beep (or message)
def play_sound():
    if settings.get('sound_enabled', False):
        print("🔔 Beep! (Imagine sound playing)")

# Show notification
def show_notification(title="Blink Break Reminder", message="Time to rest your eyes! 🌼"):
    if settings.get('notifications_enabled', True):
        notification.notify(
            title=title,
            message=message,
            timeout=5
        )

# Break Screen
def show_break_screen():
    root = tk.Tk()
    root.title("💖 ❤︎ Blink Break Time! ❤︎ 💖")

    root.attributes('-fullscreen', False)
    root.geometry("400x200")
    root.configure(bg='black')

    try:
        root.wm_attributes('-alpha', settings.get('window_transparency', 0.9))
    except:
        pass

    label = tk.Label(root, text="🌼 Rest your eyes!", font=("Helvetica", 24), fg="white", bg="black")
    label.pack(pady=30)

    timer_label = tk.Label(root, text="", font=("Helvetica", 36), fg="lightgreen", bg="black")
    timer_label.pack()

    seconds = int(settings.get('break_duration_minutes', 5) * 60)

    def update_timer():
        nonlocal seconds
        if seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer_label.config(text=f"{mins:02d}:{secs:02d}")
            seconds -= 1
            root.after(1000, update_timer)
        else:
            root.destroy()

    update_timer()
    root.mainloop()

# Break timer loop
def break_loop():
    global running
    while running:
        interval = settings.get('break_interval_minutes', 5) * 60
        time.sleep(interval)
        if running:
            play_sound()
            show_notification()
            show_break_screen()

# Stop program cleanly
def stop_program(icon, item):
    global running
    running = False
    print("👋 Exiting program...")
    icon.stop()

# Open settings window
def open_settings(icon, item):
    def save_and_close():
        settings['break_interval_minutes'] = float(interval_var.get())
        settings['break_duration_minutes'] = float(duration_var.get())
        settings['sound_enabled'] = bool(sound_var.get())
        settings['notifications_enabled'] = bool(notification_var.get())
        settings['window_transparency'] = float(transparency_var.get())
        save_settings()
        settings_window.destroy()

    settings_window = tk.Tk()
    settings_window.title("Settings")
    settings_window.geometry("300x350")

    interval_var = tk.StringVar(value=str(settings.get('break_interval_minutes', 5)))
    duration_var = tk.StringVar(value=str(settings.get('break_duration_minutes', 5)))
    sound_var = tk.BooleanVar(value=settings.get('sound_enabled', True))
    notification_var = tk.BooleanVar(value=settings.get('notifications_enabled', True))
    transparency_var = tk.StringVar(value=str(settings.get('window_transparency', 0.9)))

    tk.Label(settings_window, text="Break interval (minutes)").pack()
    tk.Entry(settings_window, textvariable=interval_var).pack()

    tk.Label(settings_window, text="Break duration (minutes)").pack()
    tk.Entry(settings_window, textvariable=duration_var).pack()

    tk.Label(settings_window, text="Sound on?").pack()
    tk.Checkbutton(settings_window, variable=sound_var).pack()

    tk.Label(settings_window, text="Notification on?").pack()
    tk.Checkbutton(settings_window, variable=notification_var).pack()

    tk.Label(settings_window, text="Window transparency (0 to 1)").pack()
    tk.Entry(settings_window, textvariable=transparency_var).pack()

    tk.Button(settings_window, text="Save", command=save_and_close).pack(pady=10)

    settings_window.mainloop()

# Create tray icon
def create_tray_icon():
    image = Image.open("icon.ico")
    menu = (
        item('Settings', open_settings),
        item('Quit', stop_program)
    )
    icon = pystray.Icon("Blink Breaker", image, "Blink Break Reminder", menu)
    return icon

# Main function
def main():
    load_settings()
    tray_icon = create_tray_icon()
    threading.Thread(target=break_loop, daemon=True).start()
    tray_icon.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Program exited cleanly.")

















