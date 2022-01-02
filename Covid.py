import bs4
import requests
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')                   # Voice Engine
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)         # Convert text to audio
    print(audio)
    engine.runAndWait()

def Coronavirus(country):

    countries = str(country).replace(" "," ")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"
    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text, 'lxml')

    corona = soups.find_all('div', class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    Cases, Deaths, Recovered = Data
    speak(f"Total Cases of COVID 19 are: {Cases}")
    speak(f"Population Recovered till now is: {Recovered}")
    speak(f"Total Deaths due to COVID 19 are : {Deaths}")

if __name__ == "__main__":
    Coronavirus('India')  
         