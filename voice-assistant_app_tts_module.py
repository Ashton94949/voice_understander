from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    with open("response.mp3", "rb") as audio_file:
        audio_data = audio_file.read()
    os.remove("response.mp3")
    return audio_data