# JARVIS #
## Voice Assistant ##
This is a simple voice assistant made with python 3 using conditional statements.  
This is just a fun project.  

It uses Microsoft's SAPI5 and the male voice that comes with windows to speak.  
It uses Google speech recognition to convert speech to text.  
It requires Internet connection to recognize speech.  
It understands English-India only.  

## Setup ##
1. Install Latest Version of Python 3 and add to path
2. Open cmd-here.exe
3. Type pip install -r requirements.txt
4. Type pipwin install pyaudio
5. Create a Desktop Shortcut of "StartingAssistant.pyw" and "WishMe.pyw".
6. Move both shortcuts to the startup folder  
  (1) Press win + r  
  (2) Type shell:startup  
  (3) Move Both the shortcuts to the startup folder
7. Edit the "path" Variable in Jarvis.pyw on line 14
8. Restart your pc

## Commands ##
### Open urls ###
1. Open youtube
2. Open stack
3. Open udemy
4. Open gmail

### Launch apps ###
1. Open chrome (May need to edit path in Jarvis.pyw)
2. Open code (You need to edit path in Jarvis.pyw)
3. Open anaconda (You need to edit path in Jarvis.pyw)

### Search ###
1. Youtube "anything you want" (opens in default browser)
2. Google "anything you want" (opens in default browser)

### Talk ###
1. Time
2. Who are you
3. Thank you

### System Commands- ###
1. Shutdown
- Yes (will shutdown your computer or laptop)
- Anything else (will do nothing)
2. Restart
- Yes (will restart your computer or laptop)
- Anything else (will do nothing)

### StartingAssistant Shortcuts- ###
#### There are no voice commands in this script ####
"Left shift + j" (runs jarvis if jarvis is not running and closes jarvis if jarvis is running)  

## System Tray Icons ##
Green icon means Jarvis is running  
Black icon means Jarvis is not running
