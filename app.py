from flask import Flask, request, jsonify
import openai
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return "Voice Agent is running!"

@app.route('/webhook', methods=['POST'])
def handle_call():
    try:
        data = request.json
        print("Received webhook:", data)
        
        # Handle call initiated
        if data.get('data', {}).get('event_type') == 'call.initiated':
            response = {
                "commands": [
                    {
                        "command": "answer",
                        "payload": {}
                    },
                    {
                        "command": "speak",
                        "payload": {
                            "text": "Dzień dobry! Witamy w naszej firmie. Jak mogę pomóc?",
                            "language": "pl",
                            "voice": "nova",
                            "payload_type": "text"
                        }
                    }
                ]
            }
            return jsonify(response)
        
        return jsonify({"status": "handled"})
        
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
