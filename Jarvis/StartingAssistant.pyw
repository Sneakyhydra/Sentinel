# There's a comment before every line you would want to edit that tells how to edit them
# A comment starts with "#"

from pynput import keyboard
import os
import pystray
from PIL import Image
from pystray import Menu, MenuItem

# The key combination to check
# You can change the key combination to launch jarvis by changing the below List
# You can replace the j with any other letter and capital J with the capital of that same letter
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='j')},
    {keyboard.Key.shift, keyboard.KeyCode(char='J')}
]

# The currently active modifiers
current = set()

StartingAssistant_icon_path = "C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\StartingAssistant.gif"

StartingAssistant_image = Image.open(StartingAssistant_icon_path)
StartingAssistant_icon = pystray.Icon("Listening")
StartingAssistant_icon.menu = Menu(MenuItem('Exit', lambda : exit_action(StartingAssistant_icon)),)
StartingAssistant_icon.icon = StartingAssistant_image
StartingAssistant_icon.title = 'Starting Assistant'

StartingAssistant_icon.visible = True

def exit_action(icon):
    icon.visible = False

def execute():
    os.startfile("C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\Jarvis.pyw")
    StartingAssistant_icon.visible = False
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