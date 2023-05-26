from bardapi import Bard
import os
import gtts
import speech_recognition as sr
import pyttsx3
from playsound import playsound
from dotenv import load_dotenv
load_dotenv()

def invokeaudiototext():
    driver = sr.Recognizer()
    with sr.Microphone() as source:
        print("Command : ")
        inp = driver.listen(source)
        text = driver.recognize_google(inp)
        print(text)
    return text

def ttsReverb(text):
    Machine = pyttsx3.init()
    Machine.say(text)
    Machine.runAndWait()
    
def playandremove(temp):
    obs = gtts.gTTS(text=temp, lang='en', slow=False)
    obs.save('Temp.mp3')
    audio_file = os.path.dirname(__file__) + '\Temp.mp3'
    playsound(audio_file)
    os.remove('temp.mp3')
    print(audio_file)


print("Running...")
Tusher = input("Hey! What do you want me to call you?\n= ")
print("Setting Environment.. This may take some time!\n")
API_key = 'WQjKpCTP_jO7t417TQ7VfOWCuhopvEWXDoMQE0Acipw_8kA5g-cAkOFP--Zn6SFD_Udssw.'
ai = Bard(token=API_key)
test = ai.get_answer("My name is "+Tusher+" remember that! And I will call you Friday from now! I expect you to answer me as Friday.")
while True:
    Query = invokeaudiototext() + " reply me in not more than 100 words!"
    if(Query == 'exit reply me in not more than 100 words!'):
        break
    received = ai.get_answer(Query)
    parse = received['content']
    print(parse)
    ttsReverb(parse)