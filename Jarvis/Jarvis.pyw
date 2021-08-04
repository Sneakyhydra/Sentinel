import pyttsx3
import datetime
import speech_recognition as sr
import os

# Initialize voice
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def common():
    # Set the common path for all files
    # Example- path = "D:\\Coding\\Jarvis\\"
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
        # Listen
        r.pause_threshold = 0.65
        audio = r.listen(source)

    try:
        # Recognize
        query = r.recognize_google(audio, language="en-IN")

    except Exception as e:
        # Error
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
            os.startfile(startingAssistant_path)
            exit()

        # Talk
        elif "time" == query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif "who are you" == query:
            speak("I am Jarvis")

        elif "thank you" == query:
            speak("You're Welcome")

        # Open urls
        elif "open youtube" == query:
            open_url("www.youtube.com")

        elif "openstack" == query:
            open_url("www.stackoverflow.com")

        elif "open udemy" == query:
            open_url("https://www.udemy.com/home/my-courses/learning/")

        elif "open gmail" == query:
            open_url("https://mail.google.com/mail/u/0/#inbox")

        elif "open whatsapp" == query:
            open_url("https:/web.whatsapp.com/")

        # Search
        # Search youtube
        elif "youtube " in query:
            query = query.replace("youtube ", "")
            url = search_youtube(query)
            url = url.replace(" ", "+")
            open_url(url)

        # Search google
        elif "google " in query:
            query = query.replace("google ", "")
            url = search_google(query)
            url = url.replace(" ", "+")
            open_url(url)

        # System commands
        elif "shutdown" == query:
            # Confirmation
            speak("Do you want to shutdown your laptop?")
            query = takeCommand().lower()
            if "yes" == query:
                os.system("shutdown /s /t 1")
            else:
                pass

        elif "restart" == query:
            # Confirmation
            speak("Do you want to restart your laptop?")
            query = takeCommand().lower()
            if "yes" == query:
                os.system("shutdown /r /t 1")
            else:
                pass

        # Launch apps
        elif "open chrome" == query:
            os.startfile(chrome_path)

        elif "open code" == query:
            os.startfile(code_path)

        elif "open anaconda" == query:
            os.startfile(anaconda_path)

        else:
            pass

    except Exception:
        speak("Not found")


if __name__ == "__main__":
    # Pid
    f = open("pidJarvis.txt", "w")
    pid = str(os.getpid())
    f.write(pid)
    f.close()

    # Paths
    common_path = common()
    startingAssistant_path = common_path + "StartingAssistant.pyw"

    # Custom paths
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    code_path = "C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    anaconda_path = "C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator (anaconda3)"

    while True:
        query = takeCommand().lower()
        voiceCommands(query)
