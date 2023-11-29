import win32.win32gui as win32gui
import win32.lib.win32con as win32con

global window
window = win32gui.GetForegroundWindow()

import recognizer
import threading
import time
import os
from pystray import Menu, MenuItem
from PIL import Image
import pystray
import speech_recognition as sr
from pynput import keyboard
import atexit
import whisper

global audio_model
model = "base.en"
audio_model = whisper.load_model(
    model, download_root=f"{os.path.dirname(os.path.abspath(__file__))}\\assets\\models")

global hidden
hidden = False
global vkeyboard
vkeyboard = keyboard.Controller()
global r
r = sr.Recognizer()

def gui_command():
    os.system("gui_command.py 1")

def calibrate():
    vkeyboard.release(keyboard.Key.ctrl)
    time.sleep(0.1)
    vkeyboard.release(keyboard.Key.alt)
    time.sleep(0.1)
    vkeyboard.release(keyboard.KeyCode.from_char('c'))
    time.sleep(0.1)

    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # listen for 5 seconds and calculate the ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=5)
        print("Calibrated")


def show_window():
    global window
    win32gui.ShowWindow(window, win32con.SW_SHOW)


def hide_window():
    global window
    win32gui.ShowWindow(window, win32con.SW_HIDE)


def toggle_window():
    vkeyboard.release(keyboard.Key.ctrl)
    time.sleep(0.1)
    vkeyboard.release(keyboard.Key.alt)
    time.sleep(0.1)
    vkeyboard.release(keyboard.KeyCode.from_char('s'))
    time.sleep(0.1)

    global hidden
    if hidden:
        show_window()
        hidden = False
    else:
        hide_window()
        hidden = True


def quit_program():
    assistant_icon.visible = False
    vkeyboard.release(keyboard.Key.ctrl)
    time.sleep(0.1)
    vkeyboard.release(keyboard.Key.alt)
    time.sleep(0.1)
    vkeyboard.release(keyboard.KeyCode.from_char('q'))
    time.sleep(0.1)
    os._exit(0)


def exit_action(icon):
    icon.visible = False
    os._exit(0)


def execute():
    threading.Thread(target=recognizer.main,
                     args=(r.energy_threshold, audio_model)).start()

    vkeyboard.release(keyboard.Key.ctrl)
    time.sleep(0.1)
    vkeyboard.release(keyboard.Key.alt)
    time.sleep(0.1)
    vkeyboard.release(keyboard.Key.shift)
    time.sleep(0.1)


def setup(icon):
    icon.visible = True

    # toggle_window()
    atexit.register(exit_action, icon)
    calibrate()

    print("Sentinel is running. Press Ctrl+Alt+Q to quit.")
    print()
    print("--------------------")
    # Command hotkeys
    print("Press Ctrl+Alt+C to calibrate microphone.")
    print("Press Ctrl+Alt+S to toggle window visibility.")
    print("Press Ctrl+Alt+Shift to execute a command.")
    print("Press Ctrl+Alt+X to edit commands.")

    with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+<shift>': execute,
            '<ctrl>+<alt>+q': quit_program,
            '<ctrl>+<alt>+c': calibrate,
            '<ctrl>+<alt>+s': toggle_window,
            '<ctrl>+<alt>+x': gui_command}) as h:
        h.join()


# System tray icon
assistant_logo_path = os.path.dirname(
    os.path.abspath(__file__)) + "\\assets\\images\\logo.png"
assistant_logo = Image.open(assistant_logo_path)
assistant_icon = pystray.Icon("Sentinel")
assistant_icon.menu = Menu(
    MenuItem("Exit", lambda: exit_action(assistant_icon)),
    MenuItem("Calibrate", calibrate),
    MenuItem("Toggle Window", toggle_window),
    MenuItem("Edit Commands", gui_command),)
assistant_icon.icon = assistant_logo
assistant_icon.title = "Sentinel"


assistant_icon.run(setup)
