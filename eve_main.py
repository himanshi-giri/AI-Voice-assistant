import pyttsx3  # for text to speech conversion
import speech_recognition  # speech to text conversion
import requests  # used to make HTTP requests, such as GET, POST, PUT, DELETE, etc
import pyautogui # used to programmatically control the mouse and keyboard, providing tools for automating tasks on your computer
from bs4 import BeautifulSoup       #FOR WEBSCRAPPING(API)k1
import datetime 
import os 
import keyboard
import speedtest

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

from intro import play_gif
play_gif

engine = pyttsx3.init("sapi5")   # here engine is an object , Microsoft Speech API version 5,an interface provided by Windows for (TTS) and speech recognition.
                                 
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening ma'am........")
        r.pause_threshold = 1 
        r.energy_threshold = 300    #voice cancellation

        audio = r.listen(source,0,4)     #4 second wait krega and will move forward

    try:
        print("understanding........")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said : {query}\n")
    except Exception as e:
        print("please say that again")
        return "none"
    return query



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe(query)

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok sir, wake up whenever you need my help")
                    break


                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")



                elif "hello" in query:
                    speak("hello ma'am , how are you ?")

                elif "i am fine" in query:
                    speak("great to hear that")

                elif "are you a robot" in query:
                    speak("Yes I am a robot, but I'm a good one. Let me prove it. How can I help you?")

                elif "how can you help me" in query:
                    speak("I can help you with many things such as Answering your questions and help you in your daily tasks easily ")

                elif "how are you" in query:
                    speak("great ma'am")

                elif "thank you" in query:
                    speak("my pleasure ma'am") 

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    wifi.get_best_server()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                
                elif "whatsapp" in query:
                    from WhatsApp import sendMessage
                    sendMessage()

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "pause" in query:
                     pyautogui.press("k")
                     speak("video paused")
                elif "play" in query:
                     pyautogui.press("k")
                     speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temprature in delhi is "
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "weather" in query:
                    search = "temprature in delhi is "
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "translate" in query:
                    from translator import translategl
                    query = query.replace("eve","")
                    query = query.replace("translate","")
                    translategl(query)


                elif "joke" in query:
                    joke=pyjokes.get_joke()
                    print(joke)
                    speak(joke)
            
                elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )

                elif "let's have a game" in query:
                    from game import game_play
                    game_play()

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")




                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                     speak("screenshot done")

                
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"ma'am, the time is {strTime}")

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")


                elif "restart the system" in query:
                    speak("Are You sure you want to restart")
                    shutdown = input("Do you wish to restart your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /r /t 1")


                    elif shutdown == "no":
                        break


                elif "finally sleep" in query:
                        speak("Going to sleep,ma'am")
                        exit()