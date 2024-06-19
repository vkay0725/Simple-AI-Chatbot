from flask import Flask, request, jsonify, send_from_directory, session
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import session

app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = "1f2edfe7f16a4cbb8b0b6ad93880e8238"

checkpoint = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

model = AutoModelForCausalLM.from_pretrained(checkpoint)


def generate_response(user_input, conversation_history, max_length=1000, top_k=50, temperature=0.1):
    conversation_history.append(user_input)
    input_text = " ".join(conversation_history[-5:]) + tokenizer.eos_token
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    
    outputs = model.generate(inputs, max_length=max_length, pad_token_id=tokenizer.eos_token_id,
                             do_sample=True, top_k=top_k, temperature=temperature)
    
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    
    return response

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/clear',methods=["POST"])
def clear_session():
    session.clear()
    return "Session cleared successfully"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    
    conversation_history = session.get("conversation_history", [])
    
    # Generate response using context-aware method
    response = generate_response(user_input, conversation_history, top_k=50, temperature=0.1)
    
    # Append generated response to conversation history
    conversation_history.append(response)
    
    # Store updated conversation history in session
    session["conversation_history"] = conversation_history
    
    return jsonify({"response": response})

@app.route("/history", methods=["GET"])
def get_history():
   
    conversation_history = session.get("conversation_history", [])
    
    return jsonify({"history": conversation_history})

if __name__ == "__main__":
    app.run(debug=True)
