import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import datetime
import openai
import os
from config import apikey

chatStr = ""


# https://youtu.be/Z3ZAJoi4x6Q
def chat(quera):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Mayur: {quera}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]





def ai(prompt, letter):
    openai.api_key = apikey

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=letter,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if letter == 200:
        text = f"\n******* Here is your result for prompt: {prompt} ****** \n"
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{prompt.split('intelligence')[1:]}.txt", "w") as f:
            f.write(text)

    return response["choices"][0]["text"]


machine = pyttsx3.init()


def speak(texts):
    print(texts)
    machine.say(texts)
    machine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        # r.pause_threshold = 1
        audio = r.listen(source)
       
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Some error occurred"


speak("Hello sir I am JARVIS AI your artificial assisstant")
while True:

    query = takeCommand()

    sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
             ["google", "https://google.com"], ["chrome", "https://google.com"],
             ["portfolio", "https://mayurpatel01.netlify.app/"]]
    for site in sites:

        if f"{site[0]}" in query.lower():
            speak(f"Opening{site[0]}sir")
            webbrowser.open(f"{site[1]}")
            break
    if "stop" in query.lower():
        speak("I am shutting down, see you soon")
        break
    if "music" in query.lower():
        songPath = "/Users/321pa/Downloads/mmmm.mp3"
        speak("Opening music player")
        os.system(songPath)
        break
    if "play" in query.lower():
        song = query.replace("play", "")
        speak("playing" + song)
        pywhatkit.playonyt(song)
        break

    if "time" in query.lower():
        time = datetime.datetime.now().strftime("%Ihour%Mminute%p")
        speak("Current time is" + time)

    if "telegram" in query.lower():
        telePath = "C:/Users/321pa/Desktop/Telegram.lnk"
        speak("opening telegram")
        os.system(f"{telePath}")
        break

    if "what is" in query.lower():
        responses = ai(query, 25)
        speak(responses)

    if "write" in query.lower():
        responses = ai(query, 200)
        speak("Created")

    else:
        print("Chatting...")
        chat(query)
