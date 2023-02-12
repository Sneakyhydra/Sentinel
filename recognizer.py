# Imports
import speech_recognition as sr
import os
import numpy as np
import queue
import torch
from assets.lib import whisper
import webbrowser

global audio_model
model = "base.en"
audio_model = whisper.load_model(
    model, download_root=f"{os.path.dirname(os.path.abspath(__file__))}/assets/models")


# Custom paths
username = os.getlogin()
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
code_path = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
anaconda_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator (anaconda3)"


def takeCommand(energy_threshold):
    r = sr.Recognizer()
    r.energy_threshold = energy_threshold
    r.pause_threshold = 0.8
    r.dynamic_energy_threshold = False

    audio_queue = queue.Queue()
    query = ""

    with sr.Microphone(sample_rate=16000) as source:
        audio = r.listen(source)

        audio_data = torch.from_numpy(np.frombuffer(
            audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)

        audio_queue.put(audio_data)

    audio_data = audio_queue.get()
    result = audio_model.transcribe(audio_data, language='english')
    query = result["text"]

    return query


def open_url(url):
    # Opens an url
    webbrowser.open_new_tab(url)


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
        # Open urls
        if "open youtube" == query or "open you tube" == query or "open your tube" == query:
            open_url("https://www.youtube.com")

        elif "open stack" == query:
            open_url("https://www.stackoverflow.com")

        elif "open udemy" == query:
            open_url("https://www.udemy.com/home/my-courses/learning/")

        elif "open gmail" == query:
            open_url("https://mail.google.com/mail/u/0/#inbox")

        elif "open whatsapp" == query:
            open_url("https://web.whatsapp.com/")

        # Search
        # Search youtube
        elif "youtube " == query[:8]:
            query = query[8:]
            url = search_youtube(query)
            url = url.replace(" ", "+")
            open_url(url)

        # Search google
        elif "google " == query[:7]:
            query = query[7:]
            url = search_google(query)
            url = url.replace(" ", "+")
            open_url(url)

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
        pass


def main(energy_threshold):
    string = takeCommand(energy_threshold)

    query = ""
    for char in string:
        if char == ' ' or char.isalpha():
            query += char
    query = query.strip().lower()

    if query != "":
        voiceCommands(query)
