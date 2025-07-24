import re
import webbrowser
import pyautogui
import screen_brightness_control as sbc
from config import OPENAI_API_KEY, WORD_PATH
from datetime import datetime

# Optional: OpenAI integration
import openai
openai.api_key = OPENAI_API_KEY

# Python
def detect_intent(user_input):
    text = user_input.lower()
    if re.search(r"\bgoogle\b", text):
        return "googleSearch"
    elif re.search(r"\byoutube\b", text):
        return "youtubeSearch"
    elif re.search(r"\bscreenshot|screen shot\b", text):
        return "screenShot"
    elif re.search(r"\b(brightness up|increase brightness)\b", text):
        return "higherBrightness"
    elif re.search(r"\b(brightness down|lower brightness)\b", text):
        return "lowerBrightness"
    elif re.search(r"\b(volume up|high volume)\b", text):
        return "highVolume"
    elif re.search(r"\b(volume down|low volume)\b", text):
        return "lowVolume"
    elif re.search(r"\b(word|microsoft word)\b", text):
        return "startWordProject"
    elif re.search(r"\b(download music|music download)\b", text):
        return "downloadMusic"
    return "llmQuery"

# Python
def google_search(user_input):
    query = user_input.replace("search", "").strip()
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for: {query}"

def youtube_search(user_input):
    query = user_input.replace("find", "").strip()
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    return f"Searching YouTube for: {query}"

def take_screenshot():
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    pyautogui.screenshot(filename)
    return f"Screenshot saved as {filename}"

def adjust_brightness(amount):
    try:
        current_brightness = sbc.get_brightness()[0]
        new_brightness = max(0, min(current_brightness + amount, 100))
        sbc.set_brightness(new_brightness)
        return f"Brightness adjusted to {new_brightness}%"
    except:
        return "Unable to adjust brightness"

def adjust_volume(action):
    presses = 5
    pyautogui.press(action, presses=presses)
    return f"Volume {'increased' if action == 'volumeup' else 'decreased'}"

def open_word():
    try:
        import os
        os.startfile(WORD_PATH)
        return "Microsoft Word opened"
    except Exception as e:
        return f"Could not open Word: {e}"

def download_music():
    return "Pretending to download music: Track XYZ by Artist ABC added to downloads!"

def handle_input(user_input):
    intent = detect_intent(user_input)

    if intent == "googleSearch":
        return google_search(user_input), intent
    elif intent == "youtubeSearch":
        return youtube_search(user_input), intent
    elif intent == "screenShot":
        return take_screenshot(), intent
    elif intent == "higherBrightness":
        return adjust_brightness(10), intent
    elif intent == "lowerBrightness":
        return adjust_brightness(-10), intent
    elif intent == "highVolume":
        return adjust_volume("volumeup"), intent
    elif intent == "lowVolume":
        return adjust_volume("volumedown"), intent
    elif intent == "startWordProject":
        return open_word(), intent
    elif intent == "downloadMusic":
        return download_music(), intent
    else:
        return ask_llm(user_input), intent
def ask_llm(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM Error: {e}"
