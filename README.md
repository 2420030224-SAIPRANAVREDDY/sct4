Task 04 - Basic Keylogger Program This repository contains a simple Python implementation of a keylogger designed to log keyboard input to a file. This project was developed as part of an internship task for SkillCraft Technology to demonstrate knowledge of input monitoring, event handling, and standard file logging in Python.

📌 Features Asynchronous Key Monitoring: Listens for keystrokes in real-time using pynput.keyboard.

Structured Logging: Automatically formats and saves logged keys with timestamps into keylog.txt.

Special Key Handling: Separates alphanumeric input from special functional keys (e.g., Space, Enter, Shift).

Graceful Exit: Safely stops execution when the Esc key is pressed.

🛠️ Requirements Python 3.x

pynput library

🚀 Installation & Setup Navigate to the project directory:

Bash cd C:\Skillkraft\task4 Install the required dependencies:

Bash py -m pip install pynput 💻 Usage Run the script:

Bash py keylogger.py Test keystroke recording:

Type text anywhere on your machine while the program is running.

The keystrokes will be captured in real-time.

Stop the program:

Focus on the terminal window where the script is running.

Press the Esc key to terminate execution.

View recorded logs:

Open the generated keylog.txt file located in the same directory to view the recorded keystroke log.

📁 Output Format Example Plaintext 2026-08-03 23:15:00,123: Key pressed: 'h' 2026-08-03 23:15:00,210: Key pressed: 'e' 2026-08-03 23:15:00,305: Key pressed: 'l' 2026-08-03 23:15:00,380: Key pressed: 'l' 2026-08-03 23:15:00,450: Key pressed: 'o' 2026-08-03 23:15:01,012: Special key pressed: Key.space
