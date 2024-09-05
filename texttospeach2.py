#import pyttsx3
# engine = pyttsx3.init() # object creation
# engine.say("Hello how are you")
# engine.runAndWait()

import pyttsx3
engine = pyttsx3.init() # object creation
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 120)

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',0.9)
print(volume)

"""VOICE"""
voices = engine.getProperty('voices')

#getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #ch
engine.say("PHP, as a scripting language, is popular among web developers because of its ability to interact with database systems including Oracle and MySQL. Website designing, where the design of an entire website can be changed using a couple of PHP scripts, instead of changing and uploading each web page.")
engine.runAndWait()
