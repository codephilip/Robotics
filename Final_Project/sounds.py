# Created By: Michael Roduin
# Date: 5/1/22

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


def deal_damage_sound():
    text_to_speech("Bam")


def recieve_damage_sound():
    text_to_speech("Ouch")


def enemy_death_sound():
    text_to_speech("Yay, we won!")


def self_death_sound():
    text_to_speech("Agh i'm dying.")


def win_sound():
    text_to_speech("Yay, We have escaped")


def hp_sound(user_hp, enemy_hp):
    text_to_speech("I have")
    text_to_speech(user_hp)
    text_to_speech("hit points left, the bad guys have")
    text_to_speech(enemy_hp)


def suggestions_sound(directions):
    text_to_speech("Which way would you like to go? Your options are")
    # if len(directions) == 1:
    # text_to_speech(directions[0])
    for i in directions:
        text_to_speech(i)


# deal_damage_sound()
# recieve_damage_sound()
# enemy_death_sound()
# self_death_sound()
