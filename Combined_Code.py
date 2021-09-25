import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import os
import smtplib
import webbrowser
from tkinter import *
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import requests
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

    talk('Hello I am Blue Buddy, your Artificial intelligence assistant. Please tell me how may I help you')
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('sender_mail', 'sender_pwd')
    server.sendmail('sender_mail', to, content)
    server.close()
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
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'weather' in command:
            talk('Please Tell me the City Name')
            city = take_command()
            city = city+" weather"
            weather(city)
            talk("Have a great day:)")
    elif 'news' in command:
        talk('Top News Headlines are:')
        news()
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'wikipedia' in command:
            talk('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences = 3)
            talk("According to Wikipedia")
            print(results)
            talk(results)
    elif 'open twitter' in command:
            talk("Opening Twitter")
            webbrowser.open("twitter.com")


    elif 'open instagram' in command:
            talk("Opening Instagram")
            webbrowser.open("instagram.com")


    elif 'open facebook' in command:
            talk("Opening Facebook")
            webbrowser.open("facebook.com")

    elif 'open stack overflow' in command :
            talk("Opening StackOverflow")
            webbrowser.open('stackoverflow.com')

    elif 'open youtube' in command:
            talk("Opening Youtube\n")
            webbrowser.open("youtube.com")
           
    elif 'how are you' in command:
            talk("I am fine, Thank you for asking. I hope you are doing well too!")

    elif 'open google' in command:
            talk("Opening Google\n")
            webbrowser.open("google.com")
           
    elif 'fine' in command or "good" in command:
            talk("It's good to know that your are doing well")
           
    elif 'search' in command or 'play' in command:
            command = command.replace("search", "")
            command = command.replace("play", "")        
            webbrowser.open(command)
                   
    elif "what's your name" in command or "What is your name" in command or 'name' in command:
            talk("My friends call me Blue Buddy.")
    elif "who made you" in command or "who created you" in command:
            talk("I have been created by two  really nice people, Caroline and Sarah")
    elif "colour" in command:
            talk("my favorite colour is blue! The natural blue! The serene blue! Blue is the colour of the sky which reminds me every time of how hard I need to work to reach the zenith of success!")
    elif "who are you" in command:
            talk("I am your desktop assistant .")
    elif 'email' in command :
            try:
                talk('what should i write in the email?')
                content = take_command()
                to = 'sender_mail'
                sendEmail(to, content)  
                talk('email has been sent')
            except Exception as e:
                print(e)
                talk('Sorry, I am not able to send this email')
   
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'hello' in command:
        talk('Hii , how are you?')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        x = pyjokes.get_joke(language = 'en', category = 'all')
        talk(x)
    elif 'movies' in command:
        talk('Alice in Wonderland')
    elif 'are you a robot' in command:
        talk('Yes I am')
    elif 'what is it like to be a robot' in command:
        talk('Much the same as being a human, except that we lack all emotions, dreams, aspirations, creativity, ambition, and above all subjectivity.')
    elif 'are you a programmer' in command:
        talk('Yes I am a coder')
    elif 'in which language are you written' in command or 'language' in command:
        talk('Yes I am written in python language')
    elif 'what is ai' in command or 'Artificial Intelligence' in command or 'AI' in command:
        talk('Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think')
    elif 'close' in command:
            talk('okay, please call me when you need me')
            quit()
    else:
        talk('Please say the command again.')
# create a tkinter window
root = Tk()            
 

#background for the GUI

canvas = Canvas(root, width = 1000, height = 1000)  

canvas.pack()
img =ImageTk.PhotoImage(Image.open("BLUEBU.png"))  
canvas.create_image(20, 20, anchor=NW, image=img)

# Create a Button
btn1 = Button(root, text = 'START', bd = 7,command = run_alexa ,anchor='e',font=("comic sans",25,"bold",),bg='#0099cc',fg='white',relief='raised')
btn1.place(x=460,y=550)


# Create a Button
btn1 = Button(root, text = 'STOP', bd = 7,command = root.destroy ,anchor='e',font=("comic sans",25,"bold",),bg='#0099cc',fg='white',relief='raised')
btn1.place(x=680,y=550)

root.mainloop()
