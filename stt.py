import speech_recognition as sr

r = sr.Recognizer()


def record():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 3)

        print ("Speak Anything.")
        audio = r.listen(source)

        text = r.recognize_google(audio)
        print("You Said: {}".format(text))

    return text