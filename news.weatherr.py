import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup
import requests
import datetime
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def greetings():                                    # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk('Good Morning')

    elif hour>12 and hour<18:
        talk('Good Afternoon')

    else:
        talk('Good Evening')

    talk('Hello I am your BuddyBot, your Artificial intelligence assistant. Please tell me how may I help you')

def news():
 news_url="https://news.google.com/news/rss"
 Client=urlopen(news_url)
 xml_page=Client.read()
 Client.close()

 soup_page=soup(xml_page,"xml")
 news_list=soup_page.findAll("item")
 # Print news title, url and publish date
 for news in news_list:
   talk(news.title.text)
   
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
 city = city.replace(" ", "+")
 res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
 print("Searching...\n")
 soup = BeautifulSoup(res.text, 'html.parser')
 location = soup.select('#wob_loc')[0].getText().strip()
 time = soup.select('#wob_dts')[0].getText().strip()
 info = soup.select('#wob_dc')[0].getText().strip()
 weather = soup.select('#wob_tm')[0].getText().strip()
 talk(location)
 talk(time)
 talk(info)
 talk(weather+"°F")

def run_alexa():
  greetings()
  while True:
    command = take_command()
    print(command)
    if 'weather' in command:
            talk('Please Tell me the City Name')
            city = take_command()
            city = city+" weather"
            weather(city)
            talk("Have a great day:)")
    elif 'news' in command:
        talk('Top News Headlines are:')
        news()
