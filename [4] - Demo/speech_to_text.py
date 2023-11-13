import speech_recognition as sr


def voice_listener():
    while True:
        with sr.Microphone() as source:
            speech_recognizer = sr.Recognizer()
            speech_recognizer.adjust_for_ambient_noise(source)
            speech_recognizer.dyanmic_energythreshhold = 3000
            try:
                print("Listening")
                command = speech_recognizer.listen(source)
                print("Processing")
                voice = speech_recognizer.recognize_google(command)
                print("Command Accepted")
                return voice
            except sr.UnknownValueError:
                print("Could not understand")
