import speech_recognition as sr
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        voice = r.listen(source)
        try:
            command = r.recognize_google(voice)
            command = command.lower()
            print(f"🗨️ You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            command = ""
        except sr.RequestError:
            print("Speech recognition service unavailable.")
            command = ""
    return command