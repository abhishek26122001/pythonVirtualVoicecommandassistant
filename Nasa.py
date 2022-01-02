import requests
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')                   # Voice Engine
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)         # Convert text to audio
    print(audio)
    engine.runAndWait()

Api_key = "v1DgqdtReQbbaDsffcz2yyjhsREH975pja5NRFHT"

def NasaNews(Date):

    speak("Extracting Data from NASA Sir, Please wait")

    url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)

    Params = {'date': str(Date)}

    r = requests.get(url,params= Params)

    Data = r.json()

    info = Data['explanation']

    Title = Data['title']

 

    speak(f"The Title is: {Title}")
    speak(f"According to NASA: {info}")

def Astro(start_date,end_date):

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_key}"

    r =requests.get(url)
    Data = r.json()

    Total_Astro = Data['element_count']   

    neo = Data['near_earth_objects']

    speak(f"Total Astroids between {start_date} and {end_date} are: {Total_Astro}")
    speak("Sir the data is printed below: ")

    for body in neo[start_date]:
        id = body['id']

        name = body['name']

        absolute = body['absolute_magnitude_h']

        print("Id: ", id  , "Name: ", name  , "Magnitude: ", absolute)
        

if __name__ == '__main__':

    NasaNews('2020-08-25')
    Astro('2021-01-25','2021-01-26')

  
