import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
from config import apiKey
import random

chatStr = ""
def chat(query):
    global chatStr
    openai.api_key = apiKey
    chatStr += f"Deep: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside of a try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    # with open(f"OpenAI/prompt- {random.randint(1, 23443334434)}", "w") as  f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def ai(prompt):
    openai.api_key = apiKey
    text = f"OpenAI response for Prompt: {prompt} \n *********************** \n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #todo: wrap this inside of a try catch block
    print(response ["choices"][0]["text"])
    text += response ["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    #with open(f"OpenAI/prompt- {random.randint(1, 23443334434)}", "w") as  f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)
def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, I'm having trouble accessing Google Speech Recognition."
if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand().lower()
    # todo Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
               say(f"Opening {site[0]} mam...")
               webbrowser.open(site[1])
    # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath ="/Users/deepshikha/Downloads/tvari-hawaii-vacation-159069.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath ="/Users/deepshikha/Downloads/tvari-hawaii-vacation-159069.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Maam the time is {hour} and {min} minutes")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "jarvis Quit" .lower() in query.lower():
            exit()

        elif "reset chat" .lower() in query.lower():
            chatStr = ""
        else:
            print("Chatting...")
            chat(query)
        #say(text)
