import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import operator

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("I am JARVIS,Sir,How may i help you?")

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('lahoti.naman@gmail.com','Panda@028')
    server.sendmail('lahoti.naman@gmail.com',to,content)
    server.close()
    
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        #Executing tasks based on query
        if 'quit' in query:
            exit()

        elif 'how are you' in query:
            print('Great Sir,Ready to help you')
            speak('Great Sir,Ready to help you')

        elif 'thank you' in query:
            print('Happy to help sir,')
            speak('Happy to help sir,')
            exit()

        elif 'good night' in query:
            print('Good Night sir,')
            speak('Good Night sir,')
            exit()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences =2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(F"Sir the time is {strTime}")
            speak(F"Sir the time is {strTime}")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.co.in")

        elif 'open vs code' in query:
            codepath="C:\\Users\\Naman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'play music' in query:
            music_dir='C:\\Users\\Naman\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'email to naman' in query:
            try:
                speak("What should i say?")
                print("What should i say?")
                content=takeCommand()
                to="lahoti.naman@yahoo.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry! I am unable to send this email")
                speak("Sorry! I am unable to send this email")
