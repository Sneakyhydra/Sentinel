from pynput import keyboard
import os

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='j')},
    {keyboard.Key.shift, keyboard.KeyCode(char='J')}
]

# The currently active modifiers
current = set()

def execute():
    os.startfile("C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\WakeUpJarvis.pyw")
    exit()

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()