# There's a comment before every line you would want to edit that tells how to edit them
# A comment starts with "#"
# The string inside speak() is what jarvis says

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

def Common():
    # Change path immediately
    # Set path to the location of Jarvis Folder
    # For Example- path = "C:\\Program Files\\Jarvis\\"
    path = "Set this path immediately"
    return path

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
        time.sleep(0.8)
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
    # The string after if and elif is what you speak. If you edit those make sure they are all lower case
    try:
        # Opens Youtube
        if 'open youtube' in query:
            open_url("www.youtube.com")

        # Opens Chrome, You can change the chrome_path below
        elif 'open chrome' in query:
            os.startfile(chrome_path)

        # Tells the time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        # Opens Visual Studio Code, You can change the code_path below
        elif 'open code' in query:
            os.startfile(code_path)

        # Open StackOverflow
        elif 'open stack overflow' in query:
            open_url("www.stackoverflow.com")

        elif 'who are you' in query:
            # Change what your Jarvis says when you say "Who are you"
            speak("I am Jarvis, your assistant")

        # Opens Anaconda Navigator, You can change the anaconda_path below
        elif 'open anaconda' in query:
            os.startfile(anaconda_path)

        # Opens Udemy's My learning page, You can change the url to open another page
        elif 'open udemy' in query:
            open_url("https://www.udemy.com/home/my-courses/learning/")

        elif 'thank you' in query:
            # Change what your Jarvis says when you say "Thank You"
            speak("Anything for you Sir!")
 
        elif 'shutdown' in query:
            # Asks if you want to shutdown your laptop. You can change it to a computer or anything you want
            speak("Do you want to shutdown your laptop?")
            query = takeCommand().lower()
            # Confirmation if you want to shutdown your laptop or pc
            if 'yes' in query:
                os.system("shutdown /s /t 1")
            else:
                pass

        elif 'restart' in query:
            # Asks if you want to restart your laptop. You can change it to a computer or anything you want
            speak("Do you want to restart your laptop?")
            query = takeCommand().lower()
            # Confirmation if you want to restart your laptop or pc
            if 'yes' in query:
                os.system("shutdown /r /t 1")
            else:
                pass
        
        # Closes Jarvis and opens the script that starts Jarvis after pressing left_shift+j
        elif 'close' in query:
            os.startfile(StartingAssistant_path)
            exit()

        # Closes Jarvis and opens the script that starts Jarvis after saying wake_up or jarvis
        elif 'go to sleep' in query:
            os.startfile(WakeUpJarvis_path)
            exit()

        # Searches Youtube for anything you want
        elif 'search youtube for' in query:
            query = query.replace("search youtube for", "")
            url = search_youtube(query)
            url = url.replace(" ", "+")
            open_url(url)

        # Searches Youtube for anything you want
        elif 'youtube for' in query:
            query = query.replace("youtube for", "")
            url = search_youtube(query)
            url = url.replace(" ", "+")
            open_url(url)

        # Searches Youtube for anything you want
        elif 'search youtube' in query:
            query = query.replace("search youtube", "")
            url = search_youtube(query)
            url = url.replace(" ", "+")
            open_url(url)

        # Searches Google for anything you want
        elif 'search google for' in query:
            query = query.replace("search google for", "")
            url = search_google(query)
            url = url.replace(" ", "+")
            open_url(url)

        # Searches Google for anything you want
        elif 'google for' in query:
            query = query.replace("google for", "")
            url = search_google(query)
            url = url.replace(" ", "+")
            open_url(url)

        # Searches Google for anything you want
        elif 'search google' in query:
            query = query.replace("search google", "")
            url = search_google(query)
            url = url.replace(" ", "+")
            open_url(url)

        # Opens Gmail Inbox
        elif 'open gmail' in query:
            open_url("https://mail.google.com/mail/u/0/#inbox")

        # You can add more commands by following the below syntax
        # Do not put "#" sign before the lines and don't add or remove any extra spaces
        
        #elif 'voice command in lower case' in query:
        #    open_url("url you want to open")
        #    os.startfile("File path(replace "/" with "\\")")  -You can refer to above commands to know the syntax  
        #    speak("Jarvis will speak this")
        #    You are free to add anything you want if you know python     

        else:
            pass

    except Exception:
        speak("I couldn't find the specified command")

if __name__ == "__main__":

    Common_path = Common()    
    StartingAssistant_path = Common_path + "StartingAssistant.pyw"
    WakeUpJarvis_path = Common_path + "WakeUpJarvis.pyw"
    Listening_icon_path = Common_path + "Listening.png"
    Recognizing_icon_path = Common_path + "Recognizing.png"
    Ididnotget_icon_path = Common_path + "Ididnotget.png"
    
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
    
    # You can change below paths so that they point to whatever you want
    # These are the default paths
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    code_path = "C:\\Users\\username\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    anaconda_path = "C:\\Users\\username\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator (anaconda3)"        
    
    while True:
        Listening_icon.visible = False
        Recognizing_icon.visible = False
        Ididnotget_icon.visible = False
        
        query = takeCommand().lower()
        voiceCommands(query)
