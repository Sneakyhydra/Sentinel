from pynput import keyboard
import pystray
from PIL import Image
from pystray import Menu, MenuItem
import os
import subprocess as s

# Key combinations
combinations = [
    {keyboard.Key.shift, keyboard.KeyCode(char="j")},
    {keyboard.Key.shift, keyboard.KeyCode(char="J")}
]

current = set()

common_path = os.path.dirname(os.path.abspath(__file__))
startingAssistant_icon_path = common_path + "\\StartingAssistant.jpg"
jarvis_path = common_path + "\\Jarvis.py"
isJarvisRunning = False


def exit_action(icon):
    icon.visible = False
    icon.stop()
    os._exit(0)


# System tray icon
startingAssistant_image = Image.open(startingAssistant_icon_path)
startingAssistant_icon = pystray.Icon("Listening")
startingAssistant_icon.menu = Menu(
    MenuItem("Exit", lambda: exit_action(startingAssistant_icon)),)
startingAssistant_icon.icon = startingAssistant_image
startingAssistant_icon.title = "Starting Assistant"

startingAssistant_icon.run_detached()


def execute():
    global isJarvisRunning
    global jarvis_path

    if isJarvisRunning == True:
        isJarvisRunning = False

        try:
            if os.path.exists("pidJarvis.txt") == True:
                f = open("pidJarvis.txt", "r")
                pid = f.readline()
                f.close()
                os.remove("pidJarvis.txt")
                s.Popen("taskkill /F /PID {0}".format(int(pid)), shell=True)
        except Exception:
            pass
    else:
        # Run Jarvis
        os.startfile(jarvis_path)
        isJarvisRunning = True


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
