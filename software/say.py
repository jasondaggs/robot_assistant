import speech_recognition as sr
import pyttsx3 as tx

r = sr.Recognizer()
engine = tx.init()

with sr.Microphone() as source:
    print('Say something')
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    engine.say(voice_data)
    engine.runAndWait()
    
    print(voice_data)


