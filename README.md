# Chatbot with Flask and DialoGPT

This repository contains a simple chatbot web application built using **Flask**, **Transformers (DialoGPT)**, and **JavaScript**. The chatbot provides conversational responses using a pre-trained AI model.

## Features
- Interactive chatbot powered by **Microsoft DialoGPT**
- Session-based conversation history management
- Simple **Flask backend** to handle chat requests
- **Frontend UI** with a chatbox, input field, and session clear button
- Hosted static files (HTML, CSS, JS) for a user-friendly interface

## Installation & Setup
### Clone the Repository
```bash
git clone https://github.com/your-username/chatbot-app.git
cd chatbot-app
```

### Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python app.py
```
The chatbot will be accessible at **http://127.0.0.1:5000/**.

## API Endpoints
| Method | Endpoint  | Description |
|--------|----------|-------------|
| `GET`  | `/`      | Serves the chatbot UI |
| `POST` | `/chat`  | Handles chat input and returns AI response |
| `POST` | `/clear` | Clears the session history |
| `GET`  | `/history` | Retrieves conversation history |

## Requirements
- Python 3.7+
- Flask
- Transformers (Hugging Face)
- JavaScript (Frontend)

To install the dependencies manually, use:
```bash
pip install flask transformers
```

## How It Works
1. The **Flask backend** loads a pre-trained **DialoGPT** model.
2. When a user sends a message, the input is passed to the **generate_response()** function.
3. The chatbot responds based on the conversation history.
4. The frontend updates the chatbox with real-time responses.
5. Users can clear the session history anytime.





