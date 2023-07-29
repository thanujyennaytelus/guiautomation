import time
import json
from pynput import mouse, keyboard

INPUT_FILE = 'actions.json'

# Load actions from a file
with open(INPUT_FILE, 'r') as f:
    actions = json.load(f)

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

# Map string names to Button and Key objects
button_map = {'left': mouse.Button.left, 'right': mouse.Button.right, 'middle': mouse.Button.middle}
key_map = {k.name: k for k in list(keyboard.Key)}

last_time = 0
for action in actions:
    time.sleep(action[-1] - last_time)  # Delay until next action should occur
    last_time = action[-1]

    if action[0] == 'mouse':
        # Perform mouse action
        (x, y), button_name, event_type = action[1:-1]
        button = button_map[button_name]
        mouse_controller.position = (x, y)
        if event_type == 'press':
            mouse_controller.press(button)
        else:
            mouse_controller.release(button)
    elif action[0] == 'key':
        # Perform keyboard action
        key_name, event_type = action[1:-1]
        key = key_map.get(key_name, key_name)  # If not found in the map, assume it's a character
        if event_type == 'press':
            keyboard_controller.press(key)
        else:
            keyboard_controller.release(key)

