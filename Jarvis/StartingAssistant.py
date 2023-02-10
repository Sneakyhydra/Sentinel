from pynput import keyboard
import pystray
from PIL import Image
from pystray import Menu, MenuItem
import os
import Jarvis
import whisper
import speech_recognition as sr

model = "medium.en"
audio_model = whisper.load_model(
    model, download_root=f"{os.path.dirname(os.path.abspath(__file__))}/models")

# Paths
common_path = os.path.dirname(os.path.abspath(__file__))
startingAssistant_icon_path = common_path + "\\StartingAssistant.jpg"
jarvis_path = common_path + "\\Jarvis.py"


def exit_action(icon):
    icon.visible = False
    os._exit(0)


# System tray icon
startingAssistant_image = Image.open(startingAssistant_icon_path)
startingAssistant_icon = pystray.Icon("Listening")
startingAssistant_icon.menu = Menu(
    MenuItem("Exit", lambda: exit_action(startingAssistant_icon)),)
startingAssistant_icon.icon = startingAssistant_image
startingAssistant_icon.title = "Starting Assistant"

global r
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # listen for 5 seconds and calculate the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=5)
    print("Calibrated")


def execute():
    vkeyboard = keyboard.Controller()
    vkeyboard.release(keyboard.Key.ctrl)
    vkeyboard.release(keyboard.Key.alt)
    vkeyboard.release(keyboard.Key.shift)

    Jarvis.main(audio_model, r.energy_threshold)


def setup(icon):
    icon.visible = True

    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<ctrl>+<alt>+<shift>'),
        execute)

    with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)
    ) as l:
        l.join()


startingAssistant_icon.run(setup)
