# 🧠 Cognia – A Mental Health ChatBot

**Cognia** is an AI-powered mental health chatbot designed to provide a supportive space for individuals to express their feelings and thoughts. It facilitates basic mental health conversations using natural language processing in a simple, user-friendly web interface. Cognia is not a substitute for professional therapy but aims to encourage self-expression and reduce the stigma around mental health.

---

![Chatbot Screenshot](Screenshot(441).png)

## 🌟 Features

* 💬 **Conversational Interface**: Natural chat-like interaction between the user and the bot.
* 📁 **Chat History**: Stores conversation logs in a local SQLite database.
* 🌐 **Web-Based UI**: Clean, responsive interface for accessibility and ease of use.
* ⚙️ **Simple Deployment**: Run locally with minimal setup.
* 🧠 **Empathetic Responses**: Provides supportive and non-judgmental responses to user input.

---

## 🧰 Tech Stack

| Layer    | Technology                                  |
| -------- | ------------------------------------------- |
| Frontend | HTML, CSS, JavaScript (vanilla)             |
| Backend  | Python (Flask)                              |
| Database | SQLite                                      |
| Server   | Flask development server                    |

---

## 🚀 Getting Started

Follow these steps to run Cognia on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/MS12code/MentalHealthChatBot.git
cd MentalHealthChatBot
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install Flask or other required libraries (you may need to manually add requirements.txt):

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to start chatting with Cognia.

---

## 💡 Why Use Cognia?

* **Mental Health Awareness**: Provides a digital outlet to talk about feelings in a stigma-free space.
* **Easy to Use**: No accounts, no sign-ups—just start chatting.
* **Educational Tool**: A great base project for students learning Flask, web development, and AI integration.
* **Customizable**: You can easily enhance its NLP capabilities or integrate with more advanced models (e.g., GPT).

---

## 📂 Project Structure

```
MentalHealthChatBot/
│
├── app.py                  # Main Flask application
├── history.sqlite          # SQLite database storing chat history
├── templates/
│   └── index.html          # Main HTML page
│
├── static/
│   ├── css/
│   │   └── style.css       # Styles for chatbot interface
│   ├── js/
│   │   ├── chat.js         # Handles frontend AJAX requests
│   │   └── script.js       # Additional JS logic (optional)
│
└── README.md               # Project description (you are here)
```

---

## 📌 Disclaimer

Cognia is not a licensed therapist or medical professional. This chatbot is for educational and preliminary mental wellness support purposes only. For any mental health concerns, consult a qualified mental health practitioner.

---

