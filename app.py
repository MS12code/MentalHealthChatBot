from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

# Initialize Flask app
app = Flask(__name__)

# Define a simple pair of user input and chatbot response
pairs = [
    (r"(?i)hi|hello|hey", ["Hello! I'm here for you. How are you feeling today?"]),
    (r"(?i)how are you\??", ["I'm here and ready to support you. How about you?"]),
    (r"(?i)i am (sad|upset|depressed|not okay)", [
        "I'm really sorry to hear that. Would you like to talk about what's been bothering you?",
        "You're not alone. I'm here to listen. What's on your mind?"
    ]),

    (r"(?i)i feel (lonely|alone|sad|depress)", [
        "It can be really tough feeling that way. Want to share more with me?",
        "I'm here with you now. You don’t have to go through this alone."
    ]),
    (r"(?i)i have (anxiety|panic attacks|fear|depression)", [
        "That sounds overwhelming. Would you like to try a calming exercise?",
        "Would you like to talk through what’s making you anxious?"
    ]),
    (r"(?i)i need (help|someone to talk to)", [
        "I'm here to support you. What's on your mind?",
        "You’re doing the right thing by reaching out. How can I support you today?"
    ]),
    (r"(?i)no", ["That's okay. I'm always here if you feel like talking later."]),
    (r"(?i)yes", ["Great! Please go ahead. I'm listening."]),
    (r"(?i)bye|goodbye|see you", [
        "Take care! Remember, you're not alone.",
        "Goodbye for now. Reach out anytime!"
    ]),
    (r"(?i)thank(s| you| u)?|ty|thx|thnx", [
        "You're very welcome. You're doing great by taking care of yourself.",
        "Glad I could help. Don’t hesitate to reach out again."
    ]),
    (r"(?i)i can’t (cope|handle this|go on)", [
        "I'm really sorry you're feeling this way. You're not alone — it might help to talk to a mental health professional.",
        "It sounds like you're going through a really hard time. Please consider reaching out to someone you trust or a professional."
    ]),
    (r"(?i)what should i do\??", [
        "I'm here to support you, but for deeper help, it’s best to speak to a mental health expert.",
        "That depends on your situation. Want to tell me a bit more about what's going on?"
    ]),
]


# Create the chatbot using the pairs defined above
chatbot = Chat(pairs, reflections)

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Define a route to get chatbot responses
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get('user_input', '').strip()
    
    if not user_input:
        return jsonify({'response': "I didn't catch that. Could you please repeat?"})
    
    response = chatbot.respond(user_input)
    
    if not response:
        response = "I'm not sure how to respond to that. Can you rephrase?"
    
    return jsonify({'response': response})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
