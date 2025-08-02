import re
import webbrowser
import pyautogui
import screen_brightness_control as sbc
from config import WORD_PATH, GEMINI_API_KEY
from datetime import datetime
import google.generativeai as genai
from logic.user_intent import UserIntent
from logic.command_executor import CommandExecutor
from logic.llm_query import LLMQuery

# Handles user input by detecting intent and routing to the appropriate command or LLM
class Handler:

    # Initialize with an LLM query interface
    def __init__(self):
        self.llm = LLMQuery()

    # Detect user intent and execute corresponding command or LLM query
    def handle_input(self, user_input):
        intent = UserIntent.detect(user_input)
        if intent == "googleSearch":
            query = UserIntent.remove_trigger(user_input)
            return CommandExecutor.google_search(query), intent
        elif intent == "youtubeSearch":
            query = UserIntent.remove_trigger(user_input)
            return CommandExecutor.youtube_search(query), intent
        elif intent == "screenShot":
            return CommandExecutor.take_screenshot(), intent
        elif intent == "higherBrightness":
            return CommandExecutor.adjust_brightness(10), intent
        elif intent == "lowerBrightness":
            return CommandExecutor.adjust_brightness(-10), intent
        elif intent == "highVolume":
            return CommandExecutor.adjust_volume("volumeup"), intent
        elif intent == "lowVolume":
            return CommandExecutor.adjust_volume("volumedown"), intent
        elif intent == "startWordProject":
            return CommandExecutor.open_word(), intent
        elif intent == "downloadMusic":
            return CommandExecutor.download_music(), intent
        else:
            return self.llm.ask(user_input), intent

# Module-level interface for handling input, used by GUI without needing direct class access
_handler_instance = Handler()

# Proxy function to route input handling through the Handler instance
def handle_input(user_input):
    return _handler_instance.handle_input(user_input)
