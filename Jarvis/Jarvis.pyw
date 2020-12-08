import pyttsx3
import datetime
import speech_recognition as sr
import os
import pystray
from PIL import Image
from pystray import Menu, MenuItem
import time

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
        Listening_icon.visible = True
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        Listening_icon.visible = False
        Recognizing_icon.visible = True
        query = r.recognize_google(audio, language='en-IN')
        Recognizing_icon.visible = False
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("I didn't get it")
        Listening_icon.visible = False
        Recognizing_icon.visible = False
        Ididnotget_icon.visible = True
        time.sleep(0.5)
        Ididnotget_icon.visible = False
        return "None"

    return query
    
def open_url(url):
    os.system(f"start \"\" {url}")

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    return url

def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    return url

def voiceCommands(query):
    if 'open youtube' in query:
        open_url("www.youtube.com")

    elif 'open chrome' in query:
        os.startfile(chrome_path)

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        os.startfile(code_path)

    elif 'open stack overflow' in query:
        open_url("www.stackoverflow.com")

    elif 'who are you' in query:
        speak("I am Jarvis, your assistant")

    elif 'open anaconda' in query:
        os.startfile(anaconda_path)

    elif 'open udemy' in query:
        open_url("https://www.udemy.com/home/my-courses/learning/")

    elif 'thank you' in query:
        speak("Anything for you Sir!")

    elif 'shutdown' in query:
        speak("Do you want to shutdown your laptop?")
        query = takeCommand().lower()
        if 'yes' in query:
            os.system("shutdown /s /t 1")
        else:
            pass

    elif 'restart' in query:
        speak("Do you want to restart your laptop?")
        query = takeCommand().lower()
        if 'yes' in query:
            os.system("shutdown /r /t 1")
        else:
            pass
    
    elif 'close' in query:
        os.startfile("C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\StartingAssistant.pyw")
        exit()

    elif 'go to sleep' in query:
        os.startfile("C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\WakeUpJarvis.pyw")
        exit()

    elif 'search youtube for' in query:
        query = query.replace("search youtube for", "")
        url = search_youtube(query)
        url = url.replace(" ", "+")
        print(url)
        open_url(url)

    elif 'youtube for' in query:
        query = query.replace("youtube for", "")
        url = search_youtube(query)
        url = url.replace(" ", "+")
        print(url)
        open_url(url)

    elif 'search youtube' in query:
        query = query.replace("search youtube", "")
        url = search_youtube(query)
        url = url.replace(" ", "+")
        print(url)
        open_url(url)

    elif 'search google for' in query:
        query = query.replace("search google for", "")
        url = search_google(query)
        url = url.replace(" ", "+")
        print(url)
        open_url(url)

    elif 'google for' in query:
        query = query.replace("google for", "")
        url = search_google(query)
        url = url.replace(" ", "+")
        print(url)
        open_url(url)

    elif 'search google' in query:
        query = query.replace("search google", "")
        url = search_google(query)
        url = url.replace(" ", "+")
        print(url)
        open_url(url)

    elif 'open gmail' in query:
        open_url("https://mail.google.com/mail/u/0/#inbox")

    else:
        pass

if __name__ == "__main__":

    Listening_icon_path = "C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\Listening.png"
    Recognizing_icon_path = "C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\Recognizing.png"
    Ididnotget_icon_path = "C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\Ididnotget.png"
    chrome_path_browsing = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    code_path = "C:\\Users\\dhruv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    anaconda_path = "C:\\Users\\dhruv\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator (anaconda3)"        
    
    Listening_image = Image.open(Listening_icon_path)
    Listening_icon = pystray.Icon("Listening")
    Listening_icon.menu = Menu(MenuItem('Exit', lambda : exit_action(Listening_icon)),)
    Listening_icon.icon = Listening_image
    Listening_icon.title = 'Jarvis'
    
    Recognizing_image = Image.open(Recognizing_icon_path)
    Recognizing_icon = pystray.Icon("Recognizing")
    Recognizing_icon.menu = Menu(MenuItem('Exit', lambda : exit_action(Recognizing_icon)),)
    Recognizing_icon.icon = Recognizing_image
    Recognizing_icon.title = 'Jarvis'

    Ididnotget_image = Image.open(Ididnotget_icon_path)
    Ididnotget_icon = pystray.Icon("I did not get that")
    Ididnotget_icon.menu = Menu(MenuItem('Exit', lambda : exit_action(Ididnotget_icon)),)
    Ididnotget_icon.icon = Ididnotget_image
    Ididnotget_icon.title = 'Jarvis'

    while True:
        Listening_icon.visible = False
        Recognizing_icon.visible = False
        Ididnotget_icon.visible = False
        
        query = takeCommand().lower()
        voiceCommands(query)