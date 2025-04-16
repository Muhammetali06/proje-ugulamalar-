from cProfile import run
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
import webbrowser
from pydub import AudioSegment

r = sr.Recognizer()

def speeding():
    in_path = 'answer.mp3'
    ex_path = 'speed.mp3'
    if os.path.exists(in_path):  # Ensure the file exists
        sound = AudioSegment.from_file(in_path)
        slower_sound = speed_swifter(sound, 1.1)
        slower_sound.export(ex_path, format="mp3")

def speed_swifter(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice

def response(voice):
    if "merhaba" in voice:
        speak("sana da merhaba genç")
    elif "selam" in voice:
        speak("sana 2 kere selam olsun")
    elif "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")
    elif "görüşürüz" in voice:
        speak("görüşürüz canım")
        return 
    elif "hangi gündeyiz" in voice:  # Fixed this line
        today = time.strftime("%A")
        today.capitalize()
        days = {
            "Monday": "Pazartesi",
            "Tuesday": "Salı",
            "Wednesday": "Çarşamba",
            "Thursday": "Perşembe",
            "Friday": "Cuma",
            "Saturday": "Cumartesi",
            "Sunday": "Pazar"
        }
        speak(days.get(today, today))

    elif "saat kaç" in voice:
        speak(random.choice(["Saat şu an: ", "Hemen bakıyorum: "]) + datetime.now().strftime("%H:%M"))

    elif "google'da ara" in voice or "google da ara" in voice:  # Fixed this line
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))

    elif "uygulama aç" in voice:
        speak("Hangi uygulamayı açmamı istiyorsun?")
        runApp = record()
        runApp = runApp.lower()
        if "valorant" in runApp:
            os.startfile("D:\\Riot Games\\Riot Client\\RiotClientServices.exe")
            speak("İstediğin uygulamayı çalıştırıyorum.")
        elif "life is strange" in runApp:
            os.startfile("steam://rungameid/319630")
            speak("İstediğin uygulamayı çalıştırıyorum.")
        else:
            speak("İstediğin uygulama çalıştırma listemde yok.")

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    speeding()
    playsound(file)
    os.remove(file)
    os.remove("speed.mp3")

def test(wake):
    if "Jarvis" in wake:  
        speak("SİZİ DİNLİYORUM")
        wake = record()
        if wake != '':
            voice = wake.lower()
            response(voice)

speak("merhaba ben jarvis size nasıl yardımcı olabilirim")
while True:
    wake = record()
    if wake != '':
        wake = wake.lower()
        print(wake.capitalize())
        test(wake)
