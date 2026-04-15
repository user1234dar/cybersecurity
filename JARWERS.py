import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import sys

# Ses çykaryjy
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Ses diňlemek
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Diňleýärin...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="tr-TR")
        print("👉 Sen diýdiň:", command)
        return command.lower()
    except:
        return ""

# Esasy funksiýa
def jarwers():
    speak("Jarwers taýýar")
    while True:
        cmd = listen()

        if cmd == "":
            continue

        # ÝAPMAK
        if "jarwers ýap" in cmd or "stop" in cmd or "ýap" in cmd:
            speak("Sag bol")
            sys.exit()

        # WEB
        elif "youtube aç " in cmd:
            speak("YouTube açýaryn")
            webbrowser.open("https://youtube.com")

        elif "google aç" in cmd:
            speak("Google açýaryn")
            webbrowser.open("https://google.com")

        # PROGRAMMA
        elif "chrome aç" in cmd:
            speak("Chrome açýaryn")
            os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")

        elif "notepad aç" in cmd:
            speak("Notepad açýaryn")
            os.startfile("C:/Windows/System32/notepad.exe")

        # SAGAT
        elif "sagat näçe" in cmd:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sagat {time}")


        else:
            speak("Düşünmedim")

# Işlet
jarwers()
