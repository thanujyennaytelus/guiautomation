import time
import json
from pynput import mouse, keyboard
import tkinter as tk
from tkinter import filedialog
import pandas as pd

INPUT_FILE = 'actions.json'
excel_values = []
current_value_index = 0

def import_excel():
    global excel_values
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    df = pd.read_excel(filename)
    excel_values = df.iloc[:, 0].tolist()

# Function to replay the actions
def replay():
    global excel_values, current_value_index
    with open(INPUT_FILE, 'r') as f:
        actions = json.load(f)
    mouse_controller = mouse.Controller()
    keyboard_controller = keyboard.Controller()
    button_map = {'left': mouse.Button.left, 'right': mouse.Button.right, 'middle': mouse.Button.middle}
    key_map = {k.name: k for k in list(keyboard.Key)}
    last_time = 0
    for action in actions:
        time.sleep(action[-1] - last_time)
        last_time = action[-1]
        if action[0] == 'mouse':
            if action[-2] == 'press':
                mouse_controller.press(button_map[action[2]])
            elif action[-2] == 'release':
                mouse_controller.release(button_map[action[2]])
        elif action[0] == 'key':
            if action[-2] == 'press':
                if action[1] == 'v':
                    keyboard_controller.type(excel_values[current_value_index])
                    current_value_index += 1
                else:
                    keyboard_controller.press(key_map[action[1]])
            elif action[-2] == 'release':
                keyboard_controller.release(key_map[action[1]])

def create_gui():
    root = tk.Tk()
    root.title("Action Replay")

    import_button = tk.Button(root, text="Import Excel", command=import_excel)
    import_button.pack(fill='x')

    replay_button = tk.Button(root, text="Replay", command=replay)
    replay_button.pack(fill='x')

    root.mainloop()

if __name__ == "__main__":
    create_gui()
