from bardapi import Bard
import os
import json
import gtts
import speech_recognition as sr
import pyttsx3
from playsound import playsound
from dotenv import load_dotenv
load_dotenv()

def loadWithJson():
    file = open("settings.json")
    replacements = json.load(file)
    return replacements

replacements = loadWithJson()

def invokeaudiototext():
    driver = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        inp = driver.listen(source)
        text = driver.recognize_google(inp)
        # print(text)
    return text

def ttsReverb(text):
    Machine = pyttsx3.init()
    Machine.say(text)
    Machine.runAndWait()
    
def playandremove(temp):
    obs = gtts.gTTS(text=temp, lang='en', slow=False)
    obs.save(replacements["file_name"])
    audio_file = os.path.dirname(__file__) + '\Temp.mp3'
    playsound(audio_file)
    os.remove(replacements["file_name"])
    print(audio_file)

print("Loading...")
Tusher = input("Hey! What do you want me to call you?\n= ")
print("Setting Environment.. This may take some time!\n")
API_key = os.environ.get("API_KEY")
ai = Bard(token=API_key)
test = ai.get_answer(replacements["name"]+Tusher+replacements["friday"] + replacements["limit"])
while True:
    Query = invokeaudiototext()
    if(Query == 'exit'):
        break
    received = ai.get_answer(Query)
    parse = received['content']
    print(parse)
    ttsReverb(parse) 