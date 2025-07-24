import re

class UserIntent:
    @staticmethod
    def detect(user_input):
        text = user_input.lower()
        if re.search(r"\bgoogle\b", text):
            return "googleSearch"
        elif re.search(r"\byoutube\b", text):
            return "youtubeSearch"
        elif re.search(r"\bscreenshot|screen shot\b", text):
            return "screenShot"
        elif re.search(r"\b(brightness up|increase brightness| increase the brightness)\b", text):
            return "higherBrightness"
        elif re.search(r"\b(brightness down|lower brightness|lower the brightness|decrease brightness|decrease the brightness)\b", text):
            return "lowerBrightness"
        elif re.search(r"\b(volume up|high volume|increase volume|increase the volume)\b", text):
            return "highVolume"
        elif re.search(r"\b(volume down|low volume|decrease volume|decrease the volume)\b", text):
            return "lowVolume"
        elif re.search(r"\b(word|microsoft word)\b", text):
            return "startWordProject"
        elif re.search(r"\b(download music|music download)\b", text):
            return "downloadMusic"
        return "llmQuery"

    @staticmethod
    def remove_trigger(user_input):
        pattern = r"^(search( on)? (google|youtube)|find( on)? (google|youtube)|search|find|google|youtube)\s*"
        query = re.sub(pattern, "", user_input, flags=re.IGNORECASE)
        return query.strip() 