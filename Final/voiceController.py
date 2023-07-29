import speech_recognition as sr
import sys


class VoiceController:

    def __init__(self):
        #self.robot = robot
        self.voice = 0

    def voice_listener(self):
        listen = True
        while listen == True:
            with sr.Microphone() as source:
                speech_recognizer = sr.Recognizer()
                speech_recognizer.adjust_for_ambient_noise(source)
                speech_recognizer.dyanmic_energythreshhold = 3000
                try:
                    print("Listening Mode Engaged")
                    command = speech_recognizer.listen(source)
                    print("Understood")
                    self.voice = speech_recognizer.recognize_google(command)
                    print("Current Task: ", self.voice)
                    return self.voice
                except sr.UnknownValueError:
                    print("Could not understand command")


# Create robot
#robot = Tangobot()
# Create Controller and give control over to robot
controller = VoiceController()
controller.voice_listener()
