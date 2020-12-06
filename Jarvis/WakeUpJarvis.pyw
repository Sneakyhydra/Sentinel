import pyttsx3
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

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "close" in query:
            os.startfile("C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\StartingAssistant.pyw")
            exit()
        elif "jarvis" in query:
            speak("Yes Sir")
            os.startfile("C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\Jarvis.pyw")
            exit()
        elif "wake up" in query:
            speak("Yes Sir")
            os.startfile("C:\\Users\\dhruv\\Desktop\\Code Playground\\Jarvis\\Jarvis.pyw")
            exit()
        else:
            pass