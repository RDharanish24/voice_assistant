# 🎙️ Voice Assistant using Python

A simple AI-based Voice Assistant built using Python that can understand voice commands, classify user intent using Machine Learning, and respond using Text-to-Speech.

---

## ✨ Features

🎧 Speech recognition using microphone

🧠 Intent classification using TF-IDF + Logistic Regression

🗣️ Text-to-Speech responses

📝 Create notes using voice

✅ Manage a todo list

👋 Greeting & exit commands

## 🛠️ Tech Stack

Python 3.x

speechrecognition

pyttsx3

scikit-learn

pyaudio

numpy

## 📂 Project Structure
```
voice_assistant/
│
├── intents.json        # Intent patterns and responses
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
├── main.py             # main core of project
└── venv/               # Virtual environment (optional)

```
## 📦 Installation
#### 1️⃣ Create virtual environment (recommended)
```
python -m venv venv

venv\Scripts\activate
```
#### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

## ⚠️ Windows users:

If pyaudio fails to install, download the .whl file from:
```
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
```
and install it manually:
```
pip install PyAudio-0.2.xx-cp3x-cp3x-win_amd64.whl
```
#### ▶️ How to Run
```
python main.py
```

#### You should hear:

Assistant started. How can I help you?

##### 🗣️ Example Voice Commands
```
Command	Action
"hello"	Greeting
"add to do"	Add item to todo list
"show todo"	Read todo list
"create note"	Create a text note
"exit"	Close assistant
```
### 🧠 How It Works

Voice input captured via microphone

Speech converted to text using Google Speech API

Text converted into vectors using TF-IDF

Intent predicted using Logistic Regression

Corresponding action executed

Response spoken using pyttsx3

### 📄 Sample Intent (intents.json)
```
{
  "tag": "greeting",
  "patterns": ["hi", "hello", "hey"],
  "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
}
```


Intents.json is available in the repository also

---

### 🚀 Future Improvements

Wake word detection

Persistent todo storage

GUI interface

Convert to .exe

Improve intent accuracy with deep learning
