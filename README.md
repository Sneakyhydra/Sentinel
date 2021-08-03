# JARVIS #
## Voice Assistant ##
This is a simple voice assistant made with python 3 using conditional statements.
This is just a fun project.

It uses Microsoft's SAPI5 and the male voice that comes with windows to speak.  
It uses Google speech recognition to convert speech to text.   
It requires Internet connection to recognize speech.     
It understands English-India only 

## Setup ##
1. Install Latest Version of Python 3 and add to path
2. Open cmd-here.exe
3. Type pip install -r requirements.txt
4. Type pipwin install pyaudio
5. Create a Desktop Shortcut of "Jarvis.pyw" and "WishMe.pyw".
6. Move both shortcuts to the startup folder  
  (1) Press win + r  
  (2) Type shell:startup  
  (3) Move Both the shortcuts to the startup folder  
7. Edit the "path" Variable in Jarvis.pyw on line 19
- Refer to the Editing Scripts Section to learn how to edit the scripts 
8. Restart your pc

## Commands ##
### Open urls ###
1. open youtube
2. open stack
3. open udemy
4. open gmail

### Launch apps ###
1. open chrome(May need to edit path in Jarvis.pyw)
2. open code(You need to edit path in Jarvis.pyw)
3. open anaconda(You need to edit path in Jarvis.pyw)

### Search ###
1. search youtube for "anything you want" (opens in default browser)
2. search google for "anything you want" (opens in default browser)

### Talk ###
1. the time
2. who are you
3. thank you
4. 
### System Commands- ###
1. shutdown
- yes(will shutdown your computer or laptop)
- no(will do nothing)
2. restart
- yes(will restart your computer or laptop)
- no(will do nothing)

### Close Jarvis ###
1. go to sleep (closes jarvis and runs wakeupjarvis script)
2. close(closes jarvis and runs startingassistant script)

### WakeUpJarvis Commands- ###
1. "wake up" or "jarvis" (closes wakeupjarvis and runs jarvis script)
2. close (closes wakeupjarvis and runs startingassistant script)

### StartingAssistant Shortcuts- ###
#### There are no voice commands in this script ####
1. "left shift + j" (closes startingassistant and runs jarvis script)

## Editing Scripts ##
To edit the scripts simply open the files in text editors or IDEs

To edit Voice Commands, Edit Jarvis.pyw  
To edit Wish on Login, Edit WishMe.pyw  
To edit Shortcut to open Jarvis, Edit StartingAssistant.pyw

## System Tray Icons ##
Green icon means Jarvis.pyw is listening  
Yellow icon means Jarvis.pyw is recognising  
Red icon means Jarvis.pyw didn't understand what you said

Blue icon means WakeUpJarvis.pyw is running

Black icon with stars means StartingAssistant.pyw is running
