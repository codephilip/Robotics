from gtts import gTTS
import pyglet
import os
from time import sleep


def text_to_speech(string):
    voice = gTTS(text=string)
    voice.save('AudioOutput.mp3')
    music = pyglet.media.load('AudioOutput.mp3', streaming=False)
    music.play()
    sleep(music.duration)
    os.remove('AudioOutput.mp3')


text_to_speech("Die Motherfudger!")
text_to_speech("Ouch")
text_to_speech("Ouch")
text_to_speech("Take That")
text_to_speech("Oof")
