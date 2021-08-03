import pyttsx3
import datetime
import speech_recognition as sr
import os
import pystray
from PIL import Image
from pystray import Menu, MenuItem
import time


# Initialize voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def Common():
    # Set the common path for all files
    path = "Set this path immeadiately"
    return path


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def exit_action(icon):
    icon.visible = False


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # Listen
        Listening_icon.visible = True
        r.pause_threshold = 0.65
        audio = r.listen(source)

    try:
        # Recognize
        Listening_icon.visible = False
        Recognizing_icon.visible = True
        query = r.recognize_google(audio, language='en-IN')
        Recognizing_icon.visible = False

    except Exception as e:
        # Error
        Listening_icon.visible = False
        Recognizing_icon.visible = False
        Ididnotget_icon.visible = True
        time.sleep(0.65)
        Ididnotget_icon.visible = False
        return "None"

    return query


def open_url(url):
    # Opens an url
    os.system(f"start \"\" {url}")


def search_google(query):
    # Search google
    url = f"https://www.google.com/search?q={query}"
    return url


def search_youtube(query):
    # Search youtube
    url = f"https://www.youtube.com/results?search_query={query}"
    return url


def voiceCommands(query):
    # Commands
    try:
        # Open files
        if "close" == query:
            # Open starting assistant
            os.startfile(StartingAssistant_path)
            exit()

        elif 'go to sleep' == query:
            # Open wakeup jarvis
            os.startfile(WakeUpJarvis_path)
            exit()

        # Talk
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'who are you' in query:
            speak("I am Jarvis")

        elif 'thank you' in query:
            speak("You're Welcome")

        # Open urls
        elif 'open youtube' in query:
            open_url("www.youtube.com")

        elif 'open stack' in query:
            open_url("www.stackoverflow.com")

        elif 'open udemy' in query:
            open_url("https://www.udemy.com/home/my-courses/learning/")

        elif 'open gmail' in query:
            open_url("https://mail.google.com/mail/u/0/#inbox")

        # Search
        # Search youtube
        elif 'search youtube for' in query:
            query = query.replace("search youtube for", "")
            url = search_youtube(query)
            url = url.replace(" ", "+")
            open_url(url)

        elif 'youtube for' in query:
            query = query.replace("youtube for", "")
            url = search_youtube(query)
            url = url.replace(" ", "+")
            open_url(url)

        elif 'search youtube' in query:
            query = query.replace("search youtube", "")
            url = search_youtube(query)
            url = url.replace(" ", "+")
            open_url(url)

        # Search google
        elif 'search google for' in query:
            query = query.replace("search google for", "")
            url = search_google(query)
            url = url.replace(" ", "+")
            open_url(url)

        elif 'google for' in query:
            query = query.replace("google for", "")
            url = search_google(query)
            url = url.replace(" ", "+")
            open_url(url)

        elif 'search google' in query:
            query = query.replace("search google", "")
            url = search_google(query)
            url = url.replace(" ", "+")
            open_url(url)

        # System commands
        elif 'shutdown' == query:
            # Confirmation
            speak("Do you want to shutdown your laptop?")
            query = takeCommand().lower()
            if 'yes' == query:
                os.system("shutdown /s /t 1")
            else:
                pass

        elif 'restart' == query:
            # Confirmation
            speak("Do you want to restart your laptop?")
            query = takeCommand().lower()
            if 'yes' == query:
                os.system("shutdown /r /t 1")
            else:
                pass

        # Launch apps
        elif 'open chrome' in query:
            os.startfile(chrome_path)

        elif 'open code' in query:
            os.startfile(code_path)

        elif 'open anaconda' in query:
            os.startfile(anaconda_path)

        else:
            pass

    except Exception:
        speak("Not found")


if __name__ == "__main__":
    # Paths
    Common_path = Common()
    StartingAssistant_path = Common_path + "StartingAssistant.pyw"
    WakeUpJarvis_path = Common_path + "WakeUpJarvis.pyw"
    Listening_icon_path = Common_path + "Listening.png"
    Recognizing_icon_path = Common_path + "Recognizing.png"
    Ididnotget_icon_path = Common_path + "Ididnotget.png"

    # System Tray Icons
    # Listening
    Listening_image = Image.open(Listening_icon_path)
    Listening_icon = pystray.Icon("Listening")
    Listening_icon.menu = Menu(
        MenuItem('Exit', lambda: exit_action(Listening_icon)),)
    Listening_icon.icon = Listening_image
    Listening_icon.title = 'Jarvis'

    # Recognizing
    Recognizing_image = Image.open(Recognizing_icon_path)
    Recognizing_icon = pystray.Icon("Recognizing")
    Recognizing_icon.menu = Menu(
        MenuItem('Exit', lambda: exit_action(Recognizing_icon)),)
    Recognizing_icon.icon = Recognizing_image
    Recognizing_icon.title = 'Jarvis'

    # Error
    Ididnotget_image = Image.open(Ididnotget_icon_path)
    Ididnotget_icon = pystray.Icon("I did not get that")
    Ididnotget_icon.menu = Menu(
        MenuItem('Exit', lambda: exit_action(Ididnotget_icon)),)
    Ididnotget_icon.icon = Ididnotget_image
    Ididnotget_icon.title = 'Jarvis'

    # Custom paths
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    code_path = "C:\\Users\\(username)\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    anaconda_path = "C:\\Users\\(username)\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator (anaconda3)"

    while True:
        Listening_icon.visible = False
        Recognizing_icon.visible = False
        Ididnotget_icon.visible = False

        query = takeCommand().lower()
        voiceCommands(query)
