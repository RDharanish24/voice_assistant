import sys
import speech_recognition as sr
import pyttsx3
import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import time

speaker = pyttsx3.init('sapi5')  
speaker.setProperty('rate', 180)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)  

recognizer = sr.Recognizer()
todo_list = ['workout', 'eat']
is_awake=False
wake_word="hey jarvis"
sleeping_word="sleep jarvis"

def speak(text):
    print(f"Assistant says: {text}")
    speaker.say(text)
    speaker.runAndWait()
    time.sleep(0.3)  

with open("intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)["intents"]

x, y = [], []
responses = {}

for intent in intents:
    tag = intent["tag"]
    responses[tag] = intent["responses"]
    for pattern in intent["patterns"]:
        x.append(pattern)
        y.append(tag)

vectorizer = TfidfVectorizer()
x_train = vectorizer.fit_transform(x)

model = LogisticRegression(max_iter=1000)
model.fit(x_train, y)

def predict_intent(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]

def create_note():
    try:
        speak("What do you want to write in your note?")
        with sr.Microphone() as mic:
            audio = recognizer.listen(mic, timeout=5, phrase_time_limit=7)
            note = recognizer.recognize_google(audio)

        speak("Choose a file name")
        with sr.Microphone() as mic:
            audio = recognizer.listen(mic, timeout=5, phrase_time_limit=5)
            filename = recognizer.recognize_google(audio).replace(" ", "_")

        with open(f"{filename}.txt", "w", encoding="utf-8") as f:
            f.write(note)

        speak("Note written successfully")

    except sr.UnknownValueError:
        speak("Sorry, I could not understand what you said.")
    except sr.WaitTimeoutError:
        speak("Listening timed out, please try again.")
    except Exception as e:
        print(f"Error in create_note: {e}")
        speak("Sorry, something went wrong while creating the note.")

def add_todo():
    try:
        speak("What do you want to add to your todo list?")
        with sr.Microphone() as mic:
            audio = recognizer.listen(mic, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            print("Heard todo item:", text)
            todo_list.append(text)
        speak("Todo list updated")
    except sr.UnknownValueError:
        speak("I couldn't understand. Please try again.")
    except sr.WaitTimeoutError:
        speak("Listening timed out, please try again.")
    except Exception as e:
        print(f"Error in add_todo: {e}")
        speak("Sorry, something went wrong while updating your todo list.")

def show_todo():
    if len(todo_list) == 0:
        speak("Your todo list is empty.")
    else:
        speak("Here are the items in your todo list:")
        for item in todo_list:
            speak(item)

def quit_app():
    speak("Goodbye!")
    sys.exit(0)




actions = {
    "greeting": lambda: (speak(random.choice(responses.get("greeting", ["Hello!"])))),
    "name":lambda:(speak(random.choice(responses.get("name")))),
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todo": show_todo,
    "exit": quit_app
}

speak("Assistant started. How can I help you?")
with sr.Microphone() as mic:
            print("calibrating microphone")
            recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            print("calibration complete")
while True:
   
    try:
        print("awake" if is_awake else "sleeping" )
        with sr.Microphone() as mic:
            audio = recognizer.listen(mic, timeout=5, phrase_time_limit=7)
            message = recognizer.recognize_google(audio).lower()

        if not is_awake and wake_word in message:
                is_awake=True
                print("now running")
                speak("hey boss")
                continue
        if is_awake and sleeping_word in message:
                is_awake=False
                print("going to sleep")
                speak("see you boss")
                continue
        if  is_awake:
            print("You said:", message)
            intent = predict_intent(message)

            action = actions.get(intent)
            if action:
                try:
                    action()
                except Exception as e:
                    print(f"Error during action execution: {e}")
                    speak("Sorry, something went wrong during the action.")
            else:
                print(f"No action found for intent: {intent}")
                speak("I don't understand.")
        else:
            pass

    except sr.UnknownValueError:
        print("Speech not understood.")
        if is_awake:
         speak("Can you repeat that?")
    except sr.WaitTimeoutError:
        print("Listening timed out, no speech detected.")
        if is_awake:
            pass
    except Exception as e:
        print(f"Unexpected error: {e}")
        speak("Sorry, something unexpected happened.")
