function sendMessage() {
    const message = document.getElementById('userInput').value;
    displayMessage(message, 'user');
    
    // Send message to Flask backend
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'message': message }),
    })
    .then(response => response.json())
    .then(data => {
        // Display bot's response
        displayMessage(data.message, 'bot');
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    document.getElementById('userInput').value = '';  // Clear the input
}

function startDictation() {
    if (window.hasOwnProperty('webkitSpeechRecognition')) {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = "en-US";  // Change based on user's language
        recognition.start();

        recognition.onresult = function (e) {
            const capturedAudio = e.results[0][0].transcript;
            fetch('/transcribe', {
                method: 'POST',
                body: capturedAudio
            })
            .then(response => response.json())
            .then(data => {
                const transcribedText = data.transcript;
                document.getElementById('userInput').value = transcribedText;
                sendMessage();
            })
            .catch(error => {
                console.error("Error sending audio to backend:", error);
            });
        };

        recognition.onerror = function (e) {
            recognition.stop();
        }
    }
}
