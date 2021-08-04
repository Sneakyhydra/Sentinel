from pynput import keyboard
import os
import pystray
from PIL import Image
from pystray import Menu, MenuItem
import subprocess as s
import psutil
import Jarvis

# Key combinations
combinations = [
    {keyboard.Key.shift, keyboard.KeyCode(char="j")},
    {keyboard.Key.shift, keyboard.KeyCode(char="J")}
]

current = set()

# Paths
common_path = Jarvis.common()
startingAssistant_icon_path = common_path + "StartingAssistant.gif"
jarvis_icon_path = common_path + "Jarvis.png"
jarvis_path = common_path + "Jarvis.pyw"

# System tray icon
# Starting Assistant
startingAssistant_image = Image.open(startingAssistant_icon_path)
startingAssistant_icon = pystray.Icon("Listening")
startingAssistant_icon.menu = Menu(
    MenuItem("Exit", lambda: exit_action(startingAssistant_icon)),)
startingAssistant_icon.icon = startingAssistant_image
startingAssistant_icon.title = "Starting Assistant"

# Jarvis
jarvis_image = Image.open(jarvis_icon_path)
jarvis_icon = pystray.Icon("Listening")
jarvis_icon.menu = Menu(
    MenuItem("Exit", lambda: exit_action(jarvis_icon)),)
jarvis_icon.icon = jarvis_image
jarvis_icon.title = "Jarvis"

startingAssistant_icon.visible = True


def exit_action(icon):
    icon.visible = False


def execute():
    if os.path.isfile("pidJarvis.txt"):
        f = open("pidJarvis.txt", "r")
        pid = f.readline()
        f.close()
        os.remove("pidJarvis.txt")

        if psutil.pid_exists(int(pid)):
            s.Popen("taskkill /F /PID {0}".format(int(pid)), shell=True)
            startingAssistant_icon.visible = True
            jarvis_icon.visible = False

        else:
            os.startfile(jarvis_path)
            startingAssistant_icon.visible = False
            jarvis_icon.visible = True

    else:
        # Run Jarvis
        os.startfile(jarvis_path)
        startingAssistant_icon.visible = False
        jarvis_icon.visible = True


def on_press(key):
    if any([key in combo for combo in combinations]):
        current.add(key)
        if any(all(k in current for k in combo) for combo in combinations):
            execute()


def on_release(key):
    if any([key in combo for combo in combinations]):
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
