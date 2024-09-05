import pyttsx3
import time
engine = pyttsx3.init() # object creation
# for i in range(10):
#     engine.say(i)
#     print(i)
# engine.runAndWait()
i=1
while i<10:
    engine.say(i)
    time.sleep(1)
    print(i)
    i=i+1
    engine.runAndWait()