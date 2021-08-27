import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say((audio))
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>5 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<16:
        speak("Good afternoon sir")

    elif hour>=16 and hour<20:
        speak("Good evening sir")

    speak("I am your personal assistant Jarvis, how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir="D:\MUSIC\Dilwale"
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak("Time is "+strTime)

    elif 'open code' in query:
        vspath = "C:\\Users\\ersay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vspath)

    elif 'open telegram' in query:
        telegram_path="D:\\Telegram Desktop\\Telegram.exe"
        os.startfile(telegram_path)