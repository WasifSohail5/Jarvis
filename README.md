# 🤖🚀 JARVIS - AI Voice Assistant

JARVIS is an advanced AI-powered voice assistant designed to make your life easier! With hands-free control over system operations, intelligent web interactions, smart file management, and LLM-powered responses, JARVIS listens, processes, and responds seamlessly, bringing futuristic automation to your fingertips.

---

## 🌟 Key Features

✨ **🎙️ Voice Commands** - Perform actions effortlessly using natural speech input.
✨ **📂 File Management** - Create, read, and organize files using voice commands.
✨ **🎛️ System Controls** - Adjust volume, brightness, and monitor system performance.
✨ **🌐 Smart Web Browsing** - Open Google, YouTube, and perform intelligent searches.
✨ **💡 AI-Powered Chat** - Get smart, context-aware responses via the Llama-3.3 model.
✨ **📧 Email Assistant** - Compose and send emails hands-free.
✨ **⏰ Reminders & News Updates** - Stay informed with reminders and real-time news.
✨ **🖱️ Mouse & Keyboard Automation** - Perform clicks, move the cursor, and open apps.

---

## 🛠 Installation Guide

### 🔹 Prerequisites
Ensure you have **Python 3.8+** installed, then install the required dependencies:
```bash
pip install pyttsx3 speechrecognition pyautogui psutil feedparser azure-core
```

### 🔹 Required APIs & Services
JARVIS integrates with multiple APIs for enhanced functionality:
- 🔹 **Azure OpenAI API** (for LLM-powered responses): [Azure AI Services](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/)
- 🔹 **Google Speech Recognition API** (for voice processing): [Google Speech API](https://cloud.google.com/speech-to-text)
- 🔹 **Feedparser API** (for fetching live news): [Feedparser Docs](https://pythonhosted.org/feedparser/)

#### 🔹 Setup Environment Variables:
```bash
export GITHUB_TOKEN='your_github_token_here'
```

---

## 📁 Project Structure

```
📂 JARVIS
├── 📜 main.py           # Core script to run the assistant
├── 📜 speech_handler.py # Handles speech recognition & text-to-speech
├── 📜 file_operations.py # File management via voice
├── 📜 system_controls.py # Volume, brightness, shutdown, restart, etc.
├── 📜 utilities.py       # Time, date, reminders, jokes, and fun facts
├── 📜 web_interactions.py # Open websites, perform searches
├── 📜 llm_integration.py # AI-powered responses via Llama-3.3 model
```

---

## 🚀 Getting Started
Launch JARVIS by running:
```bash
python main.py
```

### 🎤 Example Commands:
🗣️ **"Create a file named Notes."**  
🗣️ **"Open Google."**  
🗣️ **"Check my battery status."**  
🗣️ **"Tell me a joke."**  
🗣️ **"Send an email."**  
🗣️ **"What's the latest news?"**  

---

## 🎯 Future Enhancements
✔️ **📌 Graphical User Interface (GUI) for a better experience**  
✔️ **📌 Advanced AI-powered conversations**  
✔️ **📌 Home automation integration**  
✔️ **📌 Enhanced security features**  

---

## 💡 Contributing
We welcome contributions from developers! 🚀 Feel free to **fork** this repository, **submit pull requests**, and suggest enhancements.

---

## 📜 License
This project is open-source and available under the **MIT License**.

🚀 Happy Coding! Let JARVIS assist you like never before! 🤖🎙️
