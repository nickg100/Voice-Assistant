import pyttsx3    #pip install pyttsx3
import speech_recognition as sr   #pip install speechRecogciser #pip install pipwin
import datetime
import wikipedia   # pip install wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am subot sir, Please tell me how may i help you?")

def take_command():
    """it take input from user and convert into string
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language ='en-in')
        print("User said: ",query)
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttis()
    server.login('myid@gmail.com','mypassword')
    server.sendmail('myid@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishme()
    while(1):

        query = take_command().lower()
    
        if "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")
    
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = 'C:\\Users\\nikhi\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,song[0]))

        elif "the time" in query:
            strtime = datetime.datetime.now().strtime("%H:%M:%S")
            speak("Sir, the time is (strtime)") 

        elif "open code" in query:
            codepath = "C:\\Users\\nikhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "email to nikhil" in query:
            try:
                speak("What should i say")
                content = take_command()
                to = "nikhil.agrawal.che17@iitbhu.ac.in"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry nikhil bhai! I am not able to send")

        elif "exit" in query:
            exit()
    
        elif "who are you" in query:
            speak("I am human bot named subot sir")

# Hello World
# Hello Wolrd 2
# Hello 3
# Hello 4
#hello 8

