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

class Handler:
    def __init__(self):
        self.llm = LLMQuery()

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

# GUI does not need to know about the handle_input module-level function
_handler_instance = Handler()
def handle_input(user_input):
    return _handler_instance.handle_input(user_input)
