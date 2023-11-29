# Imports
import speech_recognition as sr
import os
import numpy as np
import queue
import torch
import webbrowser
import tkinter as tk
from win32api import GetMonitorInfo, MonitorFromPoint
import threading
from sys import exit
import json


# Custom paths
username = os.getlogin()
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
code_path = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
anaconda_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator (anaconda3)"


def takeCommand(energy_threshold, audio_model):
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
    result = audio_model.transcribe(audio_data, language='english', fp16=False)
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
        f = open('command_data.json')
        data = json.load(f)
        f.close()
        
        for command in data["urls"]:
            if command == query:
                open_url(data["urls"][command])
                break

        for command in data["app"]:
            if command == query:
                os.startfile(data["app"][command])
                break
        # # Open urls
        # if "open youtube" == query or "open you tube" == query or "open your tube" == query:
        #     open_url("https://www.youtube.com")

        # elif "open stack" == query:
        #     open_url("https://www.stackoverflow.com")

        # elif "open udemy" == query:
        #     open_url("https://www.udemy.com/home/my-courses/learning/")

        # elif "open gmail" == query:
        #     open_url("https://mail.google.com/mail/u/0/#inbox")

        # elif "open whatsapp" == query:
        #     open_url("https://web.whatsapp.com/")

        # Search
        # Search youtube
        if "youtube " == query[:8]:
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
        # elif "open chrome" == query:
        #     os.startfile(chrome_path)

        elif "open code" == query:
            os.startfile(code_path)

        elif "open anaconda" == query:
            os.startfile(anaconda_path)

        else:
            pass

    except Exception:
        pass


def run(energy_threshold, audio_model, string_queue):
    string = takeCommand(energy_threshold, audio_model)

    query = ""
    for char in string:
        if char == ' ' or char.isalpha():
            query += char
    query = query.strip().lower()

    string_queue.put(query)

    if query != "":
        voiceCommands(query)

def main(energy_threshold, audio_model):
    monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
    monitor_area = monitor_info.get("Monitor")
    work_area = monitor_info.get("Work")
    th = monitor_area[3]-work_area[3]

    root : tk.Tk
    root = tk.Tk()
    root.configure(
        background='#292929')
    root.attributes('-alpha', 0.8)

    root.overrideredirect(True)
    root.wm_attributes('-topmost', True)
    root.wm_attributes('-toolwindow', True)

    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    w = ws/5 # width of the window
    h = hs/15 # height of the window
    x = ws - w # x coordinate
    y = hs - h - th # y coordinate (40 is the height of the taskbar)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Create a Canvas widget with a red background
    canvas = tk.Canvas(root, bg="#292929", highlightthickness=0, highlightcolor="#292929", highlightbackground="#292929", width=w, height=h)
    canvas.pack(fill="both", expand=True)

    # Get the size of the canvas
    canvas_width = w
    canvas_height = h

    # Add a text label to the canvas
    text_item : tk.Canvas
    text_item = canvas.create_text(canvas_width/10, canvas_height/1.65, text="Listening . . .", fill="white", font=("Helvetica", 12, "bold"), anchor="w")

    string_queue = queue.Queue()
    string_queue.put("Listening .")
    string_queue.put("Listening . .")
    string_queue.put("Listening . . .")

    # Define the function to animate the text
    def animate_text(cnt, string_queue=string_queue):
        text = string_queue.get()

        if(text != "Listening ."):
            while not string_queue.empty():
                # remove all items in the queue
                string_queue.get()
            cnt += 1

        if(cnt == 5):
            root.quit()
            exit()

        string_queue.put(text)
        canvas.itemconfigure(text_item, text=text)
        root.after(300, animate_text2, cnt)

    def animate_text2(cnt, string_queue=string_queue):
        text = string_queue.get()

        if(text != "Listening . ."):
            while not string_queue.empty():
                # remove all items in the queue
                string_queue.get()
            cnt += 1

        if(cnt == 5):
            root.quit()
            exit()

        string_queue.put(text)
        canvas.itemconfigure(text_item, text=text)
        root.after(300, animate_text3, cnt)

    def animate_text3(cnt, string_queue=string_queue):
        text = string_queue.get()

        if(text != "Listening . . ."):
            while not string_queue.empty():
                # remove all items in the queue
                string_queue.get()
            cnt += 1

        if(cnt == 5):
            root.quit()
            exit()

        string_queue.put(text)
        canvas.itemconfigure(text_item, text=text)
        root.after(300, animate_text, cnt)

    cnt = 0
    root.after(300, animate_text, cnt)

    threading.Thread(target=run, args=(energy_threshold, audio_model, string_queue)).start()

    root.mainloop()

    
