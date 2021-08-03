import pyttsx3
import datetime

# Initialize voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 5 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")


if __name__ == "__main__":
    wishMe()
