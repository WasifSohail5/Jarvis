import datetime
import threading
import random
from speech_handler import speak, takecommand

def time() -> None:
    """Tell the current time."""
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"The current time is {Time}")

def date() -> None:
    """Tell the current date."""
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak(f"The current date is {day} {month} {year}")

def set_reminder() -> None:
    """Set a reminder."""
    speak("What should I remind you about?")
    reminder = takecommand()
    speak("In how many minutes should I remind you?")
    minutes = takecommand()
    try:
        minutes = int(minutes)
        speak(f"I’ll remind you about {reminder} in {minutes} minutes.")
        threading.Timer(minutes * 60, lambda: speak(f"Reminder: {reminder}")).start()
    except ValueError:
        speak("Please provide a valid number of minutes.")

def help_menu() -> None:
    """Provide a list of available commands."""
    speak("I can help you with various tasks. Here are some things I can do:")
    speak("1. Open applications like Notepad by saying 'open [app name]'.")
    speak("2. Control volume: 'mute volume', 'increase volume', 'decrease volume'.")
    speak("3. Check battery: 'check battery'.")
    speak("4. Shutdown or restart: 'shutdown system', 'restart system'.")
    speak("5. Take notes: 'take notes'.")
    speak("6. Send emails: 'send email'.")
    speak("7. Set reminders: 'set reminder'.")
    speak("8. Create files: 'create file'.")
    speak("9. Check time or date: 'time', 'date'.")
    speak("10. Open websites: 'open youtube', 'open google'.")
    speak("11. Search: 'search on browser', 'search for [term]'.")
    speak("12. System controls: 'hibernate system', 'lock system'.")
    speak("13. Get news: 'tell me the news'.")
    speak("14. Move mouse: 'move mouse up', 'down', 'left', 'right', or 'click'.")
    speak("15. Read files: 'read file [filename]'.")
    speak("16. Check weather: 'weather' (needs API key).")
    speak("17. Adjust brightness: 'increase brightness', 'decrease brightness'.")
    speak("18. Check resources: 'check system resources'.")
    speak("19. Hear a joke or fact: 'tell me a joke', 'share a fact'.")

# New Feature: Random Joke
def tell_joke() -> None:
    """Tell a random joke."""
    jokes = [
        "Why don’t skeletons fight each other? Because they don’t have the guts!",
        "What has 4 legs and 1 arm? A pitbull coming back from the park!",
        "Why don’t programmers prefer dark mode? The light attracts bugs!"
    ]
    speak(random.choice(jokes))

# New Feature: Random Fact
def share_fact() -> None:
    """Share a random fact."""
    facts = [
        "A group of flamingos is called a flamboyance.",
        "The shortest war in history lasted 38 minutes.",
        "Bananas are berries, but strawberries aren’t."
    ]
    speak(random.choice(facts))