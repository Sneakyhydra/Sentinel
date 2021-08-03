from pynput import keyboard
import os
import pystray
from PIL import Image
from pystray import Menu, MenuItem
import Jarvis

# Key combinations
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='j')},
    {keyboard.Key.shift, keyboard.KeyCode(char='J')}
]

current = set()

# Paths
Common_path = Jarvis.Common()
StartingAssistant_icon_path = Common_path + "StartingAssistant.gif"
Jarvis_path = Common_path + "Jarvis.pyw"

# System tray icon
StartingAssistant_image = Image.open(StartingAssistant_icon_path)
StartingAssistant_icon = pystray.Icon("Listening")
StartingAssistant_icon.menu = Menu(
    MenuItem('Exit', lambda: exit_action(StartingAssistant_icon)),)
StartingAssistant_icon.icon = StartingAssistant_image
StartingAssistant_icon.title = 'Starting Assistant'

StartingAssistant_icon.visible = True


def exit_action(icon):
    icon.visible = False


def execute():
    # Run Jarvis
    os.startfile(Jarvis_path)
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
