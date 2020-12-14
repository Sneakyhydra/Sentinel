# There's a comment before every line you would want to edit that tells how to edit them
# A comment starts with "#"

import pyttsx3
import speech_recognition as sr
import os
import pystray
from PIL import Image
from pystray import Menu, MenuItem
import Jarvis

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def exit_action(icon):
    icon.visible = False

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        WakeUpJarvis_icon.visible = True
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        WakeUpJarvis_icon.visible = False
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("I didn't get it")
        return "None"

    return query

if __name__ == "__main__":
    
    Common_path = Jarvis.Common()
    WakeUpJarvis_icon_path = Common_path + "WakeUpJarvis.png"
    Jarvis_path = Common_path + "Jarvis.pyw"
    StartingAssistant_path = Common_path + "StartingAssistant.pyw"
    
    WakeUpJarvis_image = Image.open(WakeUpJarvis_icon_path)
    WakeUpJarvis_icon = pystray.Icon("Listening")
    WakeUpJarvis_icon.menu = Menu(MenuItem('Exit', lambda : exit_action(WakeUpJarvis_icon)),)
    WakeUpJarvis_icon.icon = WakeUpJarvis_image
    WakeUpJarvis_icon.title = 'Wake Up Jarvis'

    while True:
        # You can change the voice commands according to your preference
        query = takeCommand().lower()
        if "close" in query:
            os.startfile(StartingAssistant_path)
            exit()
        elif "jarvis" in query:
            speak("Yes Sir")
            os.startfile(Jarvis_path)
            exit()
        elif "wake up" in query:
            speak("Yes Sir")
            os.startfile(Jarvis_path)
            exit()
        else:
            pass
