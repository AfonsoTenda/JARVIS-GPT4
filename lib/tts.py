import pyttsx3

#TTS Text to speech wich makes JARVIS talk to you

engine = pyttsx3.init("espeak")
engine.setProperty('rate', 150)

def say(text):
    engine.say(text)
    engine.runAndWait()