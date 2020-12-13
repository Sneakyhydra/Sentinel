# JARVIS #
## Voice Assistant ##
This is a simple voice assistant made with python 3.9 using conditional statements.
This is just a fun project.

It uses Microsoft's SAPI5 and the male voice that comes with windows to speak.  
It uses Google speech recognition to convert speech to text.   
It requires Internet connection to recognize speech.  

The offline alternative Pocket Sphinx is extremely inaccurate and needs to be trained. 

It can understand only English-India.

My dream is to make this project into -
- A fully offline speech recognizing assistant
- An AI Powered assistant

Recently added system tray icons to know the state of scripts

## Setup ##
1. Install Latest Version of Python and add to path
2. Open cmd
3. Type pip install pyttsx3
4. Type pip install SpeechRecognition
5. Type pip install pynput
6. Type pip install pipwin
7. Type pipwin install pyaudio
8. Create a Desktop Shortcut of "Jarvis.pyw" and "WishMe.pyw".
9. Move both shortcuts to the startup folder
- path = "C:\Users\username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
10. Just sign out and login to make your Jarvis do some basic stuff for you

## Commands and Shortcuts ##
### Commands that just open something- ###
1. open youtube
2. open chrome(May need to edit path in Jarvis.pyw)
3. open code(You need to edit path in Jarvis.pyw)
4. open stackoverflow
5. open anaconda(You need to edit path in Jarvis.pyw)
6. open udemy
7. open gmail

### Commands to search- ###
1. search youtube for "anything you want" (opens in default browser)
2. search google for "anything you want" (opens in default browser)

### Asking- ###
1. the time
2. who are you

### Thanking- ###
1. thank you

### System Commands- ###
1. shutdown
- yes(will shutdown your computer or laptop)
- no(will do nothing)
2. restart
- yes(will restart your computer or laptop)
- no(will do nothing)

### Closing Jarvis- ###
1. go to sleep (closes jarvis and runs wakeupjarvis script)
2. close(closes jarvis and runs startingassistant script)

### WakeUpJarvis Commands- ###
1. "wake up" or "jarvis" (closes wakeupjarvis and runs jarvis script)
2. close (closes wakeupjarvis and runs startingassistant script)

### StartingAssistant Shortcuts- ###
1. There are no voice commands in this script
2. "left shift + j" (closes startingassistant and runs wakeupjarvis script)

## Editing Scripts ##
To edit the scripts simply change the file extension from .pyw to .txt  
After editing scripts change the file extension back to .pyw

To edit Voice Commands, Edit Jarvis.pyw  
To edit Wish on Login, Edit WishMe.pyw  
To edit Shortcut to open Jarvis, Edit StartingAssistant.pyw

All scripts have instructions in them on what to edit and how to edit all the stuff

## Changing Extension ##
1. Press win key
2. Search for "File Explorer Options" and open it
3. Open View Tab in the window opened
4. Under Advanced Settings, untick "hide extensions for known file types"
5. Click on Apply
6. Click on OK

Now you will be able to change the extension from .pyw to .txt and vice versa
