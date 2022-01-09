import pyttsx3

text_speech = pyttsx3.init()

def speech(source):
    answer = source

    text_speech.say(answer)
    text_speech.runAndWait()

