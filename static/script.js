async function sendMessage() {
    const input = document.getElementById("chat-input");
    const message = input.value.trim();
    if (message === "") return;

    appendMessage("user", message);
    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });
    const data = await response.json();
    appendMessage("bot", data.response);
}

async function clearSession() {
    const response = await fetch("/clear", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    });
    if (response.ok) {
        alert("Session cleared successfully");
    } else {
        alert("Failed to clear session");
    }
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.className = `message ${sender}`;
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
