from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import datetime
import speech_recognition as sr
import os
import smtplib
import webbrowser
import wikipedia
from lsHotword import ls

flags = QtCore.Qt.WindowFlags(Qt.FramelessWindowHint)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 100)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(" Good Morning ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evenning")
    speak("I am jarvis maam ,Please tell me how may i help you")


class main(QThread):
    def __init__(self):
        super(mainT, self).__init__()

    @pyqtSlot
    def run(self):
        self.JARVIS()

    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
        # R.pause_threshold = 1
            audio = R.listen(source)
        try:
            print("recognizing")
            text = r.recognize_google(audio, language="en-in")
            print(">>", text)
        except Exception:
        # print(e)
            print("say that again")
            return "none"
        text = text.lower()
        return text

    def JARVIS(self):
        wishme()
        while True:
        Is.lsHotword_loop()
        self.query = self.STT()
        if 'wikipedia' in query:
            print("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("according to wikipedia")
            print(result)
            speak(result)

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


FROM_MAIN, _ = loadUiType(os.path.dirname(__file__), "./gui.ui"))

class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent = None):
        super(Main.self).__init__(parent)
        self.setuoUi(self)
        self.setFixedSize(1920, 1080)
        self.label_2=QLabel
        self.setWindowFlag(flags)
        Dspeak=main()
        self.label_2=QMovie(
            "C:/Users/harsh/Desktop/jarvis gui/lib/jarvisui.gif.gif", QByteArray(), self)
        self.label_2setCachmode(QMovie.CacheAll)
        self.lable.setMovie(self.label_2)
        self.label_2.start()
        self.ts=time.startfile("%A,%d %B")
        Dspeak.start()
        self.label.setpixmap(
            QPixmap("C:/Users/harsh/Desktop/jarvis gui/lib/BAR1.png"))

app=QtWidgets.QApplication(sys.argv)
main=Main()
main.show()
exit(app_exec_())
