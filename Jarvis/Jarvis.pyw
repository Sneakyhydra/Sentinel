import pyttsx3
import datetime
import speech_recognition as sr
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("I didn't get it")
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

    chrome_path_browsing = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    code_path = "C:\\Users\\dhruv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    anaconda_path = "C:\\Users\\dhruv\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator (anaconda3)"        
    
    while True:
        query = takeCommand().lower()
    
        voiceCommands(query)