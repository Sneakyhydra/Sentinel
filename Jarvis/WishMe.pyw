# There's a comment before every line you would want to edit that tells how to edit them
# A comment starts with "#"

import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# You can change the number in the condition after if and elif to change the wish at that specific time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # Will wish "Good Morning Sir!" between 5 am and 12 pm
    if hour>=5 and hour<12:
        speak("Good Morning Sir!")

    # Will wish "Good Afternoon Sir!" between 12 pm and 5 pm
    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir!")

    # If you want Jarvis to say something else then remove "#" before the 2 lines below and don't add or remove any extra spaces 
    #elif hour>=12 and hour<17:
    #    speak("Good Afternoon Sir!")

    # Will wish "Good Evening Sir!" at all other time
    else:
        speak("Good Evening Sir!")


if __name__ == "__main__":
    wishMe()