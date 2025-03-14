import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300  # Adjust for noisy environments
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Sorry, there was an error with the speech recognition service."
