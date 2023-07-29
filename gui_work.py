import time
import json
import tkinter as tk
from pynput import mouse, keyboard
from threading import Thread

actions = []
start_time = time.time()
OUTPUT_FILE = 'actions.json'
recording = False

def on_key_press(key):
    global start_time, recording
    if recording:
        actions.append(('key', key.char if hasattr(key, 'char') else key.name, 'press', time.time() - start_time))

def on_key_release(key):
    global start_time, recording
    if recording:
        actions.append(('key', key.char if hasattr(key, 'char') else key.name, 'release', time.time() - start_time))

def on_mouse_click(x, y, button, pressed):
    global start_time, recording
    if recording:
        if pressed:
            actions.append(('mouse', (x, y), button.name, 'press', time.time() - start_time))
        else:
            actions.append(('mouse', (x, y), button.name, 'release', time.time() - start_time))

def start_listeners():
    # Start the listener for keyboard in a separate thread
    keyboard_listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
    keyboard_listener.start()

    # Start the listener for mouse in the main thread
    mouse_listener = mouse.Listener(on_click=on_mouse_click)
    mouse_listener.start()

def start_recording():
    global recording, actions, start_time
    recording = True
    actions = []
    start_time = time.time()
    print("Recording started.")

def stop_recording():
    global recording
    recording = False
    # Save actions to a file
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(actions, f)
    print(f"Recording stopped. Actions saved to {OUTPUT_FILE}.")

def create_gui():
    root = tk.Tk()
    root.title("Action Recorder")

    start_button = tk.Button(root, text="Start Recording", command=start_recording)
    start_button.pack(fill='x')

    stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
    stop_button.pack(fill='x')

    root.mainloop()

if __name__ == "__main__":
    listener_thread = Thread(target=start_listeners)
    listener_thread.start()

    create_gui()

