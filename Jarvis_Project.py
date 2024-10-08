import speech_recognition as sr
import pyttsx3
import webbrowser
import Musiclibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "api key"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def ProcessCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = Musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in  c.lower():
        r = requests.get("")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])
                

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        
        
        print("Recogizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yes sir")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5,phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    ProcessCommand(command)

        except Exception as e:
            print("Error {0}".format(e))


