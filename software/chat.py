import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import speech_recognition as sr
import pyttsx3 as tx

r = sr.Recognizer()
engine = tx.init()

import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

with open("intents.json") as file:
    data = json.load(file)


def chat():
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
   # source = sr.Microphone()

    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        #inp = input()
        inp = ""

        print("listening...")
        with sr.Microphone() as source:
            audio = r.listen(source)
            voice_data = r.recognize_google(audio)
            inp = voice_data
        if inp.lower() == "quit":
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                             truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                choice = np.random.choice(i['responses'])
                print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , choice)
                engine.say(choice)
                engine.runAndWait()
        

        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))

print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
chat()

