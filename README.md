# JARVIS

## Voice Assistant

Voice assistant made with python 3.  
It uses OpenAI's Whisper to convert speech to text.  
Speech Recognition is offline but online commands can be added.  
It understands English only.

## Setup

1. Install Latest Version of Python 3 (Preferably 3.9.9 but should work on 3.8-3.10) and add to path
2. Open cmd-here.exe

- If you have a GPU that supports CUDA toolkit then the performance can be increased.
- Remove the # from the last line in the requirements.txt file.
- NOTE: This will increase the download size by 2.0 GB.

3. Type pip install -r requirements.txt
4. Restart your pc

- The program will download the "base.en" whisper model on the first launch (Approx. 140 MB).
- Optional, if you want to launch the program at startup (For Windows).
  1. Create a Desktop Shortcut of "StartingAssistant.py".
  2. Press win + r.
  3. Type shell:startup and press enter.
  4. Move the shortcut to the startup folder.

## Commands

### Open urls

1. Open youtube
2. Open stack
3. Open udemy
4. Open gmail

### Launch apps

1. Open chrome (You may need to edit path in Jarvis.py)
2. Open code (You may need to edit path in Jarvis.py)
3. Open anaconda (You may need to edit path in Jarvis.py)

### Search

1. Youtube "anything you want" (opens in default browser)
2. Google "anything you want" (opens in default browser)

### StartingAssistant Shortcuts-

#### There are no voice commands in this script

"l_shift + l_alt + l_ctrl" (starts listening for the voice command)

## System Tray Icons

Black icon means Starting Assistant is running
