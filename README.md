# 🎙️ Python Voice Assistant — Jarvis

A smart AI Voice Assistant built with Python that listens to your commands, understands intent via machine learning, and responds with natural speech.

---
## ✨ Features

- 🎤 Wake Word Detection: Activates on “hey jarvis” and sleeps on “sleep jarvis”

- 🧠 Intent Classification: TF-IDF vectorizer + Logistic Regression for understanding commands

- 📝 Voice Commands: Create notes, manage todo lists, greetings, and exit commands

- 🗣️ Text-to-Speech: Fluent speech responses with pyttsx3

- 🔄 Robust Error Handling: Polite prompts on misheard commands and timeouts

---
## 🛠️ Tech Stack

- Python 3.x

- SpeechRecognition

- pyttsx3

- scikit-learn

- PyAudio

- numpy

## 📁 Project Structure
```
voice_assistant/
│
├── intents.json        # Intent patterns and responses
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── main.py             # Main application script
└── venv/               # Virtual environment folder (optional)
```
--- 

## 🚀 Setup & Installation

1️⃣ Create and activate a virtual environment (recommended)
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
2️⃣ Install required packages
```
pip install -r requirements.txt
```
⚠️ Windows Users

If PyAudio fails to install with pip, download the matching .whl file from:
```
Unofficial PyAudio Binaries
```
Then install it with:
```
pip install path\to\PyAudio‑0.2.xx‑cp3x‑cp3x‑win_amd64.whl
```
## ▶️ Running the Assistant

Simply run:
```
python main.py
```

You will hear:
```
Assistant started. How can I help you?
```
### 🗣️ Example Commands
```
Command	         Description
"hey jarvis" |	Wake up the assistant
"sleep jarvis" | Put assistant to sleep
"hello", "hi", "hey"| Greeting
"add todo [item]"|	Add an item to the todo list
"show todo"	  |  Read your todo list
"create note"| Create a new text note
"exit"      |	Quit the assistant
```
## 🧠 How It Works

- Listen to voice input via microphone

- Convert speech to text using Google Speech Recognition API

- Transform text to vectors with TF-IDF

- Classify intent using Logistic Regression model

- Execute corresponding actions (notes, todo, etc.)

- Speak responses aloud with pyttsx3

## 📄 Sample Intent (intents.json)
```
{
  "tag": "greeting",
  "patterns": ["hi", "hello", "hey"],
  "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
}
```

Full intents file included in the repo for easy customization.

## 🎯 Future Improvements

- Persistent todo list storage (e.g., JSON, SQLite)

- Visual UI with awake/sleep indicators

- Convert to standalone executable for easy use

- More advanced NLP using transformer models

- Expand command set and natural conversation flow