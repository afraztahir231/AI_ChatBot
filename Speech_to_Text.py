import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("5 Second Silence.")
    r.adjust_for_ambient_noise(source, duration = 5)

    print ("Speak Anything.")
    audio = r.listen(source)

    text = r.recognize_google(audio)
    print("You Said: {}".format(text))


