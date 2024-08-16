from gtts import gTTS
from playsound import playsound
n=int(input("enter any number"))
i=2
while i<=n-1:
    if n%i==0:
        print("Not Prime")
        t=gTTS("Not Prime")
        t.save('b.mp3')
        playsound('b.mp3')
        break
    i = i + 1
else:
     print("Prime no")

