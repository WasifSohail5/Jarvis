import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(audio: str) -> None:
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def takecommand() -> str:
    """Capture voice input and convert to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print(e)
        speak("Please say that again")
        return "try again"