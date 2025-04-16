from datetime import datetime
import webbrowser
import speech_recognition as sr
import time
from gtts import gTTS as gt
from playsound import playsound as ps
import random
import os
import subprocess
catch = sr.Recognizer()

def record(ask = False):

    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = catch.listen(source)
        voice = ""
        try:
            voice = catch.recognize_google(audio , language="tr-TR")
        except sr.RequestError:
            speak("Bir hata oldu")
        except sr.UnknownValueError:
            speak("Bana bu kelimeyi öğretmediniz")
        return voice

def response(voice):
    if "Jarvis" or "jarvis" in voice:
        speak("sizi dinliyorum efendim") 
        
    elif "nasılsın" in voice:
        speak("hala mekaniğim siz nasılsınız")
    elif "Sen kimsin" in voice:
        speak("benim ismim jarvis bir ali projesiyim")
    elif "hayat nasıl gidiyor" in voice:
        speak("doğumumdan gecen sürede daha pek bir şey yaşıyamadım")
    elif "saat kaç" in voice:
        speak(datetime.now())
    elif "arama yap" in voice:
        search = record("ne arama yapmak istiyorsun")
        url = "https://google.com/search?q= " + search
        webbrowser.get().open(url)
        print(search + " için bulduklarım")
    elif "bilgi ver" in voice:
        speak("Ne hakkında bilgi vermemi istiyorsun")
    #if "açık kaynak kodlarını gösterir misin"
        #speak("Tabi ki")
        #subprocces.call(["cd Destkop/","cd bin/","./visualstudio.sh"])
    elif "jarvis kapan" in voice:
        speak("görüşürüz efendim")
        exit()

def speak(string):
    tts = gt(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    ps(file)
    os.remove(file)


speak("Nasıl Yardımcı Olabilirim")
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
    text = voice 


