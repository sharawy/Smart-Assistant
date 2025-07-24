# Smart Assistant

## Overview
Smart Assistant is a Python-based desktop application designed to simplify everyday tasks. It provides functionalities such as web searches, system control (brightness and volume adjustments), screenshot capturing, and integration with Google's Gemini LLM for advanced queries.

## Features
- **Google Search**: Perform quick searches directly from the app.
- **YouTube Search**: Find videos on YouTube with ease.
- **Screenshot Functionality**: Capture and save screenshots instantly.
- **Adjust Screen Brightness**: Increase or decrease screen brightness.
- **Control System Volume**: Adjust system volume levels.
- **Open Microsoft Word**: Launch Microsoft Word directly from the app.
- **Music Download Simulation**: Simulate music downloads.
- **Gemini LLM Integration**: Get responses to complex queries using Google's Gemini LLM.

## Installation

### Prerequisites
- Python 3.8 or higher
- Pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-assistant.git
   cd smart-assistant
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure you have a Gemini API key:
   - Open `config.py` and replace the value of `GEMINI_API_KEY` with your Gemini API key from Google AI Studio.
4. Configuring Microsoft Word Path

    If the default path to Microsoft Word (`C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE`) is incorrect, you can update it in the `config.py` file.

   1. Locate the `config.py` file in the project directory.
   2. Find the line:
      ```python
      WORD_PATH = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
      ```

### Usage
- Run the application:
  ```bash
  python main.py
  ```
- Use the GUI to enter commands such as:
  - search google for Python tutorials
  - find YouTube videos about AI
  - take a screenshot
  - increase brightness
  - lower volume
  - open Microsoft Word
  - ask any question for Gemini LLM to answer

## Project Structure

- `main.py` - Entry point for the application
- `config.py` - Configuration (API keys, paths, etc.)
- `logic/`
  - `handler.py` - Main handler class for routing user input
  - `user_intent.py` - Detects user intent and removes trigger words
  - `command_executor.py` - Executes system and search commands
  - `llm_query.py` - Handles Gemini LLM queries
- `gui/`
  - `main_window.py` - GUI implementation