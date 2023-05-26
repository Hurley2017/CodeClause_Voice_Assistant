from bardapi import Bard
import os
import gtts
import speech_recognition as sr
import pyttsx3
from playsound import playsound
from dotenv import load_dotenv
load_dotenv()


def playandremove(temp):
    obs = gtts.gTTS(text=temp, lang='en', slow=False)
    obs.save('temp.mp3')
    playsound('temp.mp3')
    os.remove('temp.mp3')
    print("done!\n")


print("Running...")
Tusher = input("Hey! What do you want me to call you?\n= ")
print("Setting Environment.. This may take some time!\n")
API_key = os.getenv("API_Key")
ai = Bard(token=API_key)
test = ai.get_answer("My name is "+Tusher+" remember that!")
while True:
    Query = input("\nEnter text to AI [type exit to quit] : ")
    if(Query == 'exit'):
        break
    received = ai.get_answer(Query)
    parse = received['content']
    print(parse)
    playandremove(parse)