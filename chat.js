// api/chat.js

module.exports = (req, res) => {
    const userMessage = req.body.message || "";
  
    let botResponse = "I'm here to listen. Tell me more.";
  
    if (userMessage.toLowerCase().includes("sad")) {
      botResponse = "I'm sorry you're feeling sad. Do you want to talk about it?";
    } else if (userMessage.toLowerCase().includes("happy")) {
      botResponse = "That's great to hear! What made you feel happy?";
    } else if (userMessage.toLowerCase().includes("anxious")) {
      botResponse = "Anxiety can be tough. Would you like to do a quick breathing exercise?";
    }
  
    res.status(200).json({ reply: botResponse });
  };
  