from pynput import keyboard
import pystray
from PIL import Image
from pystray import Menu, MenuItem
import os
import recognizer
import speech_recognition as sr
import win32.win32gui as win32gui
import win32.lib.win32con as win32con

global r
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and calculate the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    print("Calibrated")

# Hide the window
window = win32gui.GetForegroundWindow()
win32gui.ShowWindow(window, win32con.SW_HIDE)


def exit_action(icon):
    icon.visible = False
    os._exit(0)


# System tray icon
assistant_logo_path = os.path.dirname(
    os.path.abspath(__file__)) + "\\assets\\images\\logo.jpg"
assistant_logo = Image.open(assistant_logo_path)
assistant_icon = pystray.Icon("Assistant")
assistant_icon.menu = Menu(
    MenuItem("Exit", lambda: exit_action(assistant_icon)),)
assistant_icon.icon = assistant_logo
assistant_icon.title = "Assistant"


global vkeyboard
vkeyboard = keyboard.Controller()


def quit_program():
    assistant_icon.visible = False
    os._exit(0)


def execute():
    vkeyboard.release(keyboard.Key.ctrl)
    vkeyboard.release(keyboard.Key.alt)
    vkeyboard.release(keyboard.Key.shift)

    recognizer.main(r.energy_threshold)


def setup(icon):
    icon.visible = True

    with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+<shift>': execute,
            '<ctrl>+<alt>+q': quit_program}) as h:
        h.join()


assistant_icon.run(setup)
