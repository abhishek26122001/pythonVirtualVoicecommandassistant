from platform import system
from time import time
import pyttsx3
import datetime
import requests
import speech_recognition as sr
import pyaudio
import os
import cv2
import random
from requests import get
import wikipedia
import pywhatkit
import webbrowser
import smtplib
import sys
import pyjokes
from bs4 import BeautifulSoup
import pywikihow
import psutil
import speedtest
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)                    # Voice Engine
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)         # Convert text to audio
    print(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    strtime = datetime.datetime.now().strftime("%I:%M")
    if hour>=0 and hour<12:
        speak(f"Good Morning! Sir, the time is {strtime} AM")

    elif hour>=12 and hour<18:           # Wish Me 
        speak(f"Good Afternoon! Sir, the time is {strtime} PM")    
    else:
        speak(f"Good Evening! Sir, the time is {strtime} PM")    

    speak("I am your Command Assistant Jarvis, Please tell me what can i do for you")   

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)    # Command Taker function
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=7)

    try:
        print("Recognizing....")
        speak("working on your command sir")
        query = r.recognize_google(audio, language='en-in')
        print(f"Abhishek commanded: {query}\n") 

    except Exception as e:

        print("Say that again please....")
        speak("Sorry sir, i didnt get that please say it again")
        return "None"   
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('golusen.sen123@gmail.com', '5555566666@Abhi')
    server.sendmail('golusen.sen123@gmail.com',to, content)
    server.close()

def search_wikihow(query, max_results=10, lang="en"):
    return list(pywikihow.WikiHow.search(query,max_results, lang))

    
    

if __name__ == "__main__":
    wishme()
    while True:

        query = takecommand().lower()


        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "hello jarvis" in query:
            speak("jai siya ram sir! I am Ram Bhakth Jarvis and i am created by Abhishek")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloding speed and {up} bit per second uploading speed") 
            battery = psutil.sensors_battery()
            percentage = battery.percent 
            speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power sir")
            elif percentage>=40 and percentage<=75:
                speak("we should connect our system to charging point") 
            elif percentage<=15 and percentage<=30:
                speak("we don't have enough power sir, please plugin the charging port")
            elif percentage<=15:
                speak("we have very low power, please plugin your system or else it will shutdown very soon")           


        elif "open cmd" in query:
            os.system("start cmd")

        elif "volume up" in query:
            pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "mute"in query:
            pyautogui.press("volumemute")        
                

        elif "open camera" in query:
            speak("opening camera sir")
            vid = cv2.VideoCapture(0)
            while True:
                ret, img = vid.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(20) & 0xFF == ord("s"):
                    break;    
            vid.release()
            cv2.destroyAllWindows()

        elif "i want to listen my playlist" in query:
            music_dir = "C:\\englishsongs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "change the song" in query:
            music_dir = "C:\\englishsongs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))    

        elif "what is my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        elif "search about" in query:
            speak("searching wikipedia....")
            try:

                query = query.replace("search about", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("according to wikipedia")
                speak(results)
            except Exception as e:
                speak("Sorry sir I am unable to search, Please try Again")    

        elif "play" in query:
            play = query.replace("play", "")
            speak("on youtube playing" +play)
            pywhatkit.playonyt(play)  
                                                                      # All functions are to give command
        
        elif "open google" in query:
            speak("Sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "send email" in query:
            try:
                speak("what should i type sir?")
                content = takecommand().lower()
                to = "abhisaini.saini123@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to Abhishek")

            except Exception as e:
                print(e)
                speak("sorry sir i am unable to send the email") 
                

        elif "set alarm" in query:
            speak("sir please tell me the time to set alarm, for example, set alarm to 6:15 AM")
            try:

                tt = takecommand()
                tt = tt.replace("set alarm to ", "")
                tt = tt.replace(".", "")
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt) 

            except Exception as e:
                speak("Sorry sir! Alarm Aborted")    
     
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke) 
        
        elif "where we are" in query:
            speak("wait sir, let me check")
            try:
                url = 'https://ipinfo.io/'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['region']
                country = geo_data['country']
                speak(f"sir i am not sure , but i think we are in {city} city of {state} state in {country} India")
            except Exception as e:
                speak("Sorry sir , Due to network issue i am not able to find where we are.")
                pass    
        
        elif "open instagram profile" in query:
            speak("sir please enter the username correctly.")
            name = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")


        elif "current temperature" in query:

            search = "weather in Karnal"
            url = f"https://www.google.com/search?q={search}"
            d = requests.get(url)
            data = BeautifulSoup(d.text, "html.parser")
            temp = data.find("div", class_ ="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "activate how to do mode" in query:
            speak("How to do mode is activated")
            while True:
                speak("Please tell me what you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "clear" in how:
                        speak("okay sir, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir , i am not able to find this")
        
        elif "what is happening in space" in query:
            speak("Please enter the date sir, for data extraction")
            date = input("Enter Your Date Here, for example 2021-07-08: ")
            from Nasa import NasaNews
            NasaNews(date)

        elif "objects near earth" in query:
            from Nasa import Astro

            speak("Please Enter the Start Date sir: ")
            start = input("Enter the Starting Date, for ex 2021-07-12: ")
            speak("Please Enter the End Date sir")
            end = input("Please Enter the Ending Date, for ex 2021-07-15: ")
            Astro(start, end)

        elif " covid update" in query:
            from Covid import Coronavirus
            speak("Which countries update you want sir?")
            try:

                covid = takecommand()
                Coronavirus(covid)
            except Exception as e:
                speak("Sorry sir i am unable to fetch the data")    
            

 
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe") 

        elif "close cmd" in query:                            #closing command functions
            speak("okay sir, closing command prompt")
            os.system("taskkill /f /im cmd.exe")        
        
        elif "stop the music" in query:
            speak("okay sir, i hope you enjoyed the track")
            os.system("taskkill /f /im Music.UI.exe") 
     
        elif "sleep now" in query:
            speak("no problem! thank you for using your Jarvis sir, have a good day!")
            sys.exit()

        speak("Sir is there anything else i can do?")        
    
       