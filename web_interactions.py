import webbrowser as wb
from speech_handler import speak, takecommand

def search_and_play_song(query: str) -> None:
    """Search for a term on YouTube."""
    search_query = query.replace(" ", "+")
    youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
    speak(f"Searching for {query} on YouTube.")
    wb.open(youtube_url)
    speak("Opening YouTube with the search results.")

def open_youtube() -> None:
    """Open YouTube in the browser."""
    wb.open("youtube.com")
    speak("Opening YouTube.")

def open_google() -> None:
    """Open Google in the browser."""
    wb.open("google.com")
    speak("Opening Google.")

def search_on_browser() -> None:
    """Search a term on Google."""
    speak("What should I search for?")
    search_term = takecommand()
    wb.open(f"https://www.google.com/search?q={search_term.replace(' ', '+')}")
    speak(f"Searching for {search_term} on Google.")