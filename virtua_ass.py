import pyttsx3
import datetime
import time
import speech_recognition as sr
#from requests import pyWhatkit as kit
import os
import os.path
import random
import requests
import smtplib
import webbrowser
import wikipedia
import sys
import smtplib
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QDate, QTime, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from vir import Ui_Form

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        speak(f" Good Morning ,its {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon,its {tt}")
    else:
        speak(f"Good Evenning,its {tt}")
    speak("hello harsha I am jarvis maam ,Please tell me how may i help you")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
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
        query = query.lower()
        return query

    def TaskExecution(self):
        wishme()
        while True:
            self.query = self.takecommand().lower()
            if 'wikipedia' in self.query:
                print("searching wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                result = wikipedia.summary(self.query, sentences=4)
                speak("according to wikipedia")
                print(result)
                speak(result)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'open facebook' in self.query:
                webbrowser.open("facebook.com")    

            elif 'open google' in self.query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in self.query:
                music = "C:\\Users\\harsh\\Music\\my fav"
                songs = os.listdir(music)
                print(songs)
                os.startfile(os.path.join(music, songs[0]))

            elif 'the time' in self.query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"maam,the time is {strtime}")

            elif 'open code' in self.query:
                codepath = "C:\\Users\\harsh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
                os.startfile(codepath)

            elif 'send message' in self.query:
                kit.sendwhatmsg("+919340184282","this is testing protocol",2,25)    

            elif 'email to harsha' in self.query:
                try:
                    speak("what should i say?")
                    content = takecommand.lower()
                    to = "harsha10thakur10@gmail.com"
                    sendEmail(to, content)
                    speak("email has been send to harsha")
                except Exception as e:
                    print(e)

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('thakurharsha707@gmail.com', 'thakurkomal10')
        server.sendmail('thakurharsha707@gmail.com', to, content)
        server.close()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../Gui/lib/iron.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../Gui/lib/UI.gif.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        # timer=QTime(self)
        # timer.timeout.connect(self.showTime)
        # timer.start(1000)
        startExecution.start()

#    def showTime(self):
    # current_time=QTime.currentTime()
    # current_date=QDate.currentDate()
    # label_time=current_time.toString('hh:mm:ss')
    # label_date=current_date.toString(Qt.ISODate)
    # self.ui.textBrowser.setText(label_date)
    # self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
JARVIS = Main()
JARVIS.show()
exit(app.exec_())

