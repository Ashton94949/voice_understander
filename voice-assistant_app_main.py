from flask import Flask, request, jsonify
from speech_recognition import recognize_speech
from nlp_module import process_query
from tts_module import text_to_speech

app = Flask(__name__)

@app.route('/voice-assistant', methods=['POST'])
def voice_assistant():
    text = recognize_speech()
    response = process_query(text)
    text_to_speech(response)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
