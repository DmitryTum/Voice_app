import speech_recognition as sr
import os
import sys
import webbrowser
#import pyaudio


def talk(words):
    print(words)
    os.system('say ' + words)


def command():
    r = sr.Recognizer()

    with sr.Microphone() as sourse:
        print('Say')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(sourse, duration=1)
        audio = r.listen(sourse)
    try:
        command = r.recognize_google(audio).lower()
        print('You say: ' + command)
    except sr.UnknownValueError():
        print('What?')
        zadanie = command()
    return zadanie


def makeSomething(zadanie):
    if 'open'.lower() in zadanie:
        print('OK')
        url = 'google.com'
        webbrowser.open(url)
    elif 'stop' in zadanie:
        talk('Ok, no problem')
        sys.exit()

while True:
    makeSomething(command())




talk('Hi, how are you?')
