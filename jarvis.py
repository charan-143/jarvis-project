import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import pywhatkit as kit


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour= int(datetime.datetime.now().hour)
    minute=int(datetime.datetime.now().minute)
    if hour>=0 and hour<=11:
        speak('good morning')
        speak('the time is '+str(hour)+":"+str(minute)+ " AM")
    elif hour>=12 and hour<=18:
        if hour>12:
            hour = hour-12
        elif hour==12:
            hour = hour
        speak('good afternoon')
        speak('the time is '+str(hour)+":"+str(minute)+ " PM")
    else:
        if hour>12:
            hour = hour-12
        speak('good evening')
        speak('the time is '+str(hour)+":"+str(minute)+ " PM")
    speak('Iam Jarvis. what can i do for you sir.')



def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('listening')
        r.pause_threshold=1
        audio= r.listen(source)
        try:
            print("recognizing..")
            query = r.recognize_google(audio,language='en-in')
            print('user said:',query)
        except Exception as e:
            print('say that again...')
            print(e)
            return "none"
        return query.lower()



if __name__ == '__main__':
    wishme()
    

    while True:
        query = takecommand()
        
        if "open cmd" in query:
            os.system("start cmd") 

        elif "hello" in query:
            speak("Hello sir")
        
        elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "play on youtube" in query:
            query.replace("play on youtube","")
            kit.playonyt(query,open_video=True)
        elif "search on google" in query:
            query =query.replace("search on google", "")
            kit.search(query)
        elif "open notepad" in query:
            os.system("notepad")
        elif "open code" in query:
            path ="C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(path)