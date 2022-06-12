import pyttsx3
import datetime
import speech_recognition as sr
import os
import smtplib
import webbrowser
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(" hello harsha Good Morning ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evenning")
    speak("I am jarvis maam ,Please tell me how may i help you")


def takecommand():
    # take microphones input from user and return string command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:  {query}\n")
    except Exception as e:
        # print(e)
        print("say that again")
        return "none"
    return query


if __name__ == "__main__":
    speak("Hello Harsha")
    wishme()
    if 1:
        query = takecommand().lower()
        if 'wikipedia' in query:
            print("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif "tell me your name" in query:
            speak("I am Jarvis. Your deskstop Assistant")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music = "C:\\Users\\harsh\\Music\\my fav"
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"maam,the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\harsh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)
        elif "bye" in query:
            speak("Bye.have a nice day")
            exit()

