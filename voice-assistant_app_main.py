from flask import Flask, request, jsonify
from speech_recognition import recognize_speech
from nlp_module import process_query
from tts_module import text_to_speech

app = Flask(__name__)

@app.route('/voice-assistant', methods=['POST'])
def voice_assistant():
    audio_data = request.files['audio']
    text = recognize_speech(audio_data)
    response = process_query(text)
    audio_response = text_to_speech(response)
    return jsonify({'response': response, 'audio': audio_response})

if __name__ == '__main__':
    app.run(debug=True)