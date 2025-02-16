# JARVIS - A Desktop Voice Assistant

JARVIS is a simple desktop voice assistant built using Python. It can perform various tasks like telling the time and date, searching Wikipedia, opening websites, playing music, taking screenshots, and more.

## Features
- Greets the user based on the time of the day
- Tells the current time and date
- Searches Wikipedia for information
- Opens commonly used websites (YouTube, Google, Stack Overflow, etc.)
- Plays a random song from the user's music directory
- Opens Google Chrome and performs searches
- Remembers user inputs and recalls them later
- Takes screenshots and saves them
- Listens to voice commands and responds accordingly

## Technologies Used
- Python 3.8
- SpeechRecognition
- pyttsx3 (Text-to-Speech)
- Wikipedia API
- Webbrowser
- OS Module
- pyautogui (for screenshots)
- Random Module

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/jarvis-assistant.git
   ```
2. Navigate to the project folder:
   ```bash
   cd jarvis-assistant
   ```
3. Install the required dependencies:
   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia pyautogui
   ```

## Usage
1. Run the script:
   ```bash
   python jarvis.py
   ```
2. Speak commands like:
   - "What is the time?"
   - "What is the date?"
   - "Search Wikipedia for Python programming"
   - "Open YouTube"
   - "Play music"
   - "Take a screenshot"
   - "Go offline" (to exit)

## Notes
- Ensure you have a working microphone for voice input.
- Modify the file paths accordingly for music, Chrome, and screenshot locations.
- This assistant is designed for Windows, and some features might not work on other OS.

## Future Enhancements
- Add more voice commands and functionalities
- Improve error handling and recognition accuracy
- Integrate AI-powered responses
- Enhance UI with a graphical interface

## Contributing
If you have suggestions for improvements, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

---
Developed by Wasif Sohail

