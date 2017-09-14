import speech_recognition as sr
from gtts import gTTS
from time import ctime
import time
import os


def speak(prompt):
    print(prompt)
    tts = gTTS(text=prompt, lang='en')
    tts.save("hello_prompt.mp3")
    os.system("mpg321 hello_prompt.mp3")

