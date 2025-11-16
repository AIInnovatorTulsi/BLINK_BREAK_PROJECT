🚨 Blink Breaker – Eye-Care Reminder App

A lightweight Python-based desktop tool that reminds users to take eye breaks at regular intervals.
It helps reduce eye strain, especially for developers, students, and professionals who spend long hours on screens.

📌 Features

✔️ Automatic break reminders at customizable intervals
✔️ Popup break screen with countdown timer
✔️ System tray icon for easy control
✔️ Configurable settings (via simple GUI):
Break interval
Break duration
Window transparency
Sound alerts
Desktop notifications
✔️ Settings saved in settings.json
✔️ Runs in the background using a system tray icon
✔️ Lightweight — built using Tkinter, PyStray, and Plyer

📂 Project Structure
BLINK_BREAKER/
│── blink_break.py          # Main application script
│── blink_break.spec        # PyInstaller build file
│── settings.json           # User settings storage
│── icon.ico                # System tray icon
│── build/                  # Auto-generated
│── dist/                   # Auto-generated executable
│── .venv/                  # Virtual environment (ignored)

🛠️ Tech Stack
Python 3.10+
Tkinter (for UI)
PyStray (system tray integration)
PIL / Pillow (image handling)
Plyer (cross-platform notifications)
Threading (background break timer)

 How It Works
1️⃣ Break Timer
Runs in the background and waits for the specified interval:
interval = settings.get('break_interval_minutes', 5) * 60
time.sleep(interval)
2️⃣ Notification 
When time is up:
show_notification()
show_break_screen()
3️⃣ Break Screen
A small window appears showing a countdown timer, helping you rest your eyes.
4️⃣ Tray Icon
The app sits quietly in the system tray with options for:
⚙️ Settings
❌ Quit

⚙️ Installation
1. Clone the Repository
git clone https://github.com/AIInnovatorTulsi/BLINK_BREAKER.git
cd BLINK_BREAKER

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt
(If you don’t have a requirements file, generate it with:
pip freeze > requirements.txt)

4. Run the Application
python blink_break.py

🖥️ Build Executable (Windows)

To create a .exe file:
pyinstaller --onefile --windowed --icon=icon.ico blink_break.py
The final executable will be generated inside the dist/ folder.

⚙️ Configurable Settings

Stored automatically in settings.json:
{
  "break_interval_minutes": 5,
  "break_duration_minutes": 5,
  "sound_enabled": true,
  "notifications_enabled": true,
  "window_transparency": 0.9
}
Users can modify these values from the Settings window accessible via tray icon.

🎯 Use Case

This tool is ideal for:
Programmers
Designers
Students
Office workers
Anyone spending long hours on the computer

🤝 Contributions

Pull requests are welcome!
Feel free to suggest new features like:
Dark mode
Longer break animations
Custom sound alerts
