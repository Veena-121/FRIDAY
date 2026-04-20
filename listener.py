import speech_recognition as sr

def listen(silent =False):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if not silent:
            print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        
    try:
        if not silent:
            print("Recognizing")
        command = recognizer.recognize_google(audio)
        return command.lower()

    except Exception as e:
        if not silent:
            print("Sorry, I didn't catch that.")
        return ""
