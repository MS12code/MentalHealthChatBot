from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

# Initialize Flask app
app = Flask(__name__)

# Define a simple pair of user input and chatbot response
pairs = [
    (r"(?i)hi|hello|hey", ["How can I assist you today?"]),
    (r"(?i)how are you\??", ["I'm doing well, thank you for asking! How about you?"]),
    (r"(?i)i am sad", ["I'm really sorry to hear that. Would you like to talk about it?"]),
    (r"(?i)no", ["Oh! Please feel free to message me whenever you want!"]),
    (r"(?i)bye", ["Goodbye! Take care, and remember, I'm always here if you need me."]),
    (r"(?i)thank(s| you| u)?|ty|thx|thnx", ["You're very welcome! Let me know if there's anything else I can help with."]),
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
