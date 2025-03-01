import datetime
import os
import time
import pyautogui
import smtplib
from email.mime.text import MIMEText
from speech_handler import speak, takecommand
from system_controls import control_volume, check_battery, shutdown_restart, control_brightness, check_system_resources
from file_operations import take_notes, create_file, read_file
from web_interactions import search_and_play_song, open_youtube, open_google, search_on_browser
from utilities import time, date, set_reminder, help_menu, tell_joke, share_fact
from llm_integration import get_llm_response
import feedparser  # For news

def send_email() -> None:
    """Send an email via voice command."""
    speak("What is the recipient's email address?")
    to_email = takecommand()
    speak("What is the subject?")
    subject = takecommand()
    speak("What should I write in the email?")
    body = takecommand()

    from_email = "your_email@gmail.com"  # Replace with your email
    password = "your_app_password"  # Replace with your app password

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
        speak("Email sent successfully!")
    except Exception as e:
        speak("Sorry, I couldn't send the email.")

def get_news() -> None:
    """Fetch and read the latest news headlines."""
    try:
        feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
        speak("Here are the latest news headlines.")
        for entry in feed.entries[:5]:
            speak(entry.title)
    except Exception as e:
        speak("Sorry, I couldn't fetch the news right now.")

def wishme() -> None:
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    speak("Welcome back sir!")
    if 4 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir, See You Tomorrow!")
    speak("JARVIS at your service sir, please tell me how may I help you.")

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()
        if query == "try again":
            continue

        if "search for" in query or "play" in query:
            search_term = query.replace("search for", "").replace("play", "").strip()
            search_and_play_song(search_term)
        elif "volume" in query:
            control_volume(query)
        elif "battery" in query or "check battery" in query:
            check_battery()
        elif "shutdown system" in query or "restart system" in query:
            shutdown_restart(query)
        elif "take notes" in query or "add notes" in query:
            take_notes()
        elif "send email" in query or "email" in query:
            send_email()
        elif "remind me" in query or "set reminder" in query:
            set_reminder()
        elif "create file" in query or "make file" in query:
            create_file()
        elif "time" in query:
            time()
        elif "date" in query:
            date()
        elif "open youtube" in query:
            open_youtube()
        elif "open google" in query:
            open_google()
        elif "search on browser" in query:
            search_on_browser()
        elif query.startswith("open "):
            app_name = query.replace("open ", "").strip()
            try:
                os.startfile(app_name)
                speak(f"Opening {app_name}.")
            except Exception:
                speak(f"Sorry, I couldn't open {app_name}.")
        elif "hibernate system" in query:
            speak("Hibernating the system in 10 seconds.")
            time.sleep(10)
            os.system("shutdown /h")
        elif "lock system" in query:
            speak("Locking the system.")
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif "news" in query or "headlines" in query:
            get_news()
        elif "move mouse up" in query:
            pyautogui.moveRel(0, -50)
            speak("Mouse moved up.")
        elif "move mouse down" in query:
            pyautogui.moveRel(0, 50)
            speak("Mouse moved down.")
        elif "move mouse left" in query:
            pyautogui.moveRel(-50, 0)
            speak("Mouse moved left.")
        elif "move mouse right" in query:
            pyautogui.moveRel(50, 0)
            speak("Mouse moved right.")
        elif "click" in query:
            pyautogui.click()
            speak("Mouse clicked.")
        elif query.startswith("read file "):
            read_file(query)
        elif "help" in query or "what can you do" in query:
            help_menu()
        elif "brightness" in query:
            control_brightness(query)
        elif "system resources" in query or "how is my system" in query:
            check_system_resources()
        elif "joke" in query:
            tell_joke()
        elif "fact" in query:
            share_fact()
        elif "offline" in query or "exit" in query:
            speak("Goodbye, sir.")
            quit()
        else:
            response = get_llm_response(query)
            speak(response)
            print(response)