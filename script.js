function getTimeBasedGreeting() {
    // Create a new Date object with IST timezone (UTC+5:30)
    const options = { timeZone: 'Asia/Kolkata', hour: '2-digit', minute: '2-digit' };
    const timeInIST = new Intl.DateTimeFormat('en-GB', options).format(new Date());
    const hour = parseInt(timeInIST.split(':')[0]);

    if (hour >= 5 && hour < 12) {
        return "Good Morning!";
    } else if (hour >= 12 && hour < 17) {
        return "Good Afternoon!";
    } else {
        return "Good Evening!";
    }
}

// Display greeting when the page loads
window.onload = function() {
    let chatbox = document.getElementById('chatbox');
    let greetingMessage = document.createElement('div');
    greetingMessage.classList.add('chat-message');
    greetingMessage.textContent = getTimeBasedGreeting() + " How can I assist you today?";
    chatbox.appendChild(greetingMessage);
};

document.getElementById('user_input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault();  // Prevent form submission if inside a form
      sendMessage();
    }
});

function sendMessage() {
  let userInput = document.getElementById('user_input').value;
  if (userInput.trim() === "") {
      return;
  }

  let chatbox = document.getElementById('chatbox');

  // Display user message
  let userMessage = document.createElement('div');
  userMessage.classList.add('chat-message');
  userMessage.textContent = "You: " + userInput;
  chatbox.appendChild(userMessage);

  document.getElementById('user_input').value = "";

  // Create and display loading animation
  let loadingMessage = document.createElement('div');
  loadingMessage.classList.add('chat-message');
  loadingMessage.textContent = "Bot: .";
  chatbox.appendChild(loadingMessage);
  chatbox.scrollTop = chatbox.scrollHeight;

  // Animate dots
  let dotCount = 1;
  const typingInterval = setInterval(() => {
      dotCount = (dotCount % 5) + 1;
      loadingMessage.textContent = "Bot: " + ".".repeat(dotCount);
  }, 300);

  // Send user input to backend
  fetch('/get_response', {
      method: 'POST',
      body: new URLSearchParams({ 'user_input': userInput }),
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
      }
  })
  .then(response => response.json())
  .then(data => {
      // Wait 2 seconds then show actual response
      setTimeout(() => {
          clearInterval(typingInterval);
          loadingMessage.textContent = "Bot: " + data.response;
          chatbox.scrollTop = chatbox.scrollHeight;
      }, 2500);
  })
  .catch(error => {
      clearInterval(typingInterval);
      console.error('Error:', error);
      loadingMessage.textContent = "Bot: Sorry, something went wrong.";
  });
}
