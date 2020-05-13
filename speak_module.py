from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)  # saves the audio file
    playsound(filename)
    os.remove(filename)

