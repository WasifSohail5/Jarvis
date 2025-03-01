import pyautogui
import psutil
import os
import time

def control_volume(action: str) -> None:
    """Control system volume."""
    if "mute" in action:
        pyautogui.hotkey("volumemute")
        speak("Volume muted.")
    elif "increase" in action or "up" in action:
        pyautogui.hotkey("volumeup")
        pyautogui.hotkey("volumeup")
        speak("Volume increased.")
    elif "decrease" in action or "down" in action:
        pyautogui.hotkey("volumedown")
        pyautogui.hotkey("volumedown")
        speak("Volume decreased.")

def check_battery() -> None:
    """Check and report battery status."""
    battery = psutil.sensors_battery()
    if battery is None:
        speak("Battery status is not available. This might not be a laptop.")
    else:
        percent = battery.percent
        plugged = "plugged in" if battery.power_plugged else "not plugged in"
        speak(f"Your battery is at {percent} percent and is {plugged}.")

def shutdown_restart(query: str) -> None:
    """Shutdown or restart the system."""
    if "shutdown" in query:
        speak("Shutting down the system in 10 seconds. Goodbye, sir.")
        time.sleep(10)
        os.system("shutdown /s /t 1")
    elif "restart" in query:
        speak("Restarting the system in 10 seconds.")
        time.sleep(10)
        os.system("shutdown /r /t 1")

# New Feature: Screen Brightness Control
def control_brightness(action: str) -> None:
    """Adjust screen brightness using keyboard shortcuts."""
    if "increase" in action:
        pyautogui.hotkey("fn", "f6")  # Adjust based on your system
        speak("Brightness increased.")
    elif "decrease" in action:
        pyautogui.hotkey("fn", "f5")  # Adjust based on your system
        speak("Brightness decreased.")

# New Feature: System Resource Monitoring
def check_system_resources() -> None:
    """Report CPU and RAM usage."""
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    speak(f"Your CPU usage is at {cpu_usage} percent, and RAM usage is at {ram_usage} percent.")