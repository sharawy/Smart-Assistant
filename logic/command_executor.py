import webbrowser
import pyautogui
import screen_brightness_control as sbc
from datetime import datetime
from config import WORD_PATH

class CommandExecutor:
    @staticmethod
    def google_search(query):
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for: {query}"

    @staticmethod
    def youtube_search(query):
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Searching YouTube for: {query}"

    @staticmethod
    def take_screenshot():
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot(filename)
        return f"Screenshot saved as {filename}"

    @staticmethod
    def adjust_brightness(amount):
        try:
            current_brightness = sbc.get_brightness()[0]
            new_brightness = max(0, min(current_brightness + amount, 100))
            sbc.set_brightness(new_brightness)
            return f"Brightness adjusted to {new_brightness}%"
        except:
            return "Unable to adjust brightness"

    @staticmethod
    def adjust_volume(action):
        presses = 5
        pyautogui.press(action, presses=presses)
        return f"Volume {'increased' if action == 'volumeup' else 'decreased'}"

    @staticmethod
    def open_word():
        try:
            import os
            os.startfile(WORD_PATH)
            return "Microsoft Word opened"
        except Exception as e:
            return f"Could not open Word: {e}"

    @staticmethod
    def download_music():
        return "Pretending to download music: Track XYZ by Artist ABC added to downloads!" 