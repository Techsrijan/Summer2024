from gtts import gTTS
from playsound import playsound
text="Hello How are you tum zeet gye"
tts = gTTS(text)
tts.save('a.mp3')
playsound('a.mp3')
