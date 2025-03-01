import os
from speech_handler import speak, takecommand

def take_notes() -> None:
    """Append notes to a file or create a new one."""
    speak("What should I name the notes file?")
    filename = takecommand()
    file_path = os.path.join(os.path.expanduser("~\\Documents"), f"{filename}.txt")
    speak("What should I write in the notes?")
    content = takecommand()
    with open(file_path, "a") as f:
        f.write(f"{content}\n")
    speak(f"Notes added to {filename} in your Documents folder.")

def create_file() -> None:
    """Create a text file with voice input."""
    speak("What should I name the file?")
    filename = takecommand()
    speak("What should I write in the file?")
    content = takecommand()
    file_path = os.path.join(os.path.expanduser("~\\Documents"), f"{filename}.txt")
    with open(file_path, "w") as f:
        f.write(content)
    speak(f"File {filename} created in your Documents folder.")

def read_file(query: str) -> None:
    """Read the contents of a text file."""
    filename = query.replace("read file ", "").strip()
    file_path = os.path.join(os.path.expanduser("~\\Documents"), f"{filename}.txt")
    try:
        with open(file_path, "r") as f:
            content = f.read()
        speak(f"Reading the file {filename}.")
        speak(content)
    except Exception as e:
        speak(f"Sorry, I couldn't read the file {filename}.")