# Smart Assistant

## Overview
Smart Assistant is a Python-based desktop application designed to simplify everyday tasks. It provides functionalities such as web searches, system control (brightness and volume adjustments), screenshot capturing, and integration with OpenAI's GPT-4 for advanced queries.

## Features
- **Google Search**: Perform quick searches directly from the app.
- **YouTube Search**: Find videos on YouTube with ease.
- **Screenshot Functionality**: Capture and save screenshots instantly.
- **Adjust Screen Brightness**: Increase or decrease screen brightness.
- **Control System Volume**: Adjust system volume levels.
- **Open Microsoft Word**: Launch Microsoft Word directly from the app.
- **Music Download Simulation**: Simulate music downloads.
- **OpenAI GPT-4 Integration**: Get responses to complex queries using OpenAI's GPT-4.

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
3. Ensure you have the OpenAI API key set up in your environment variables:
   - Open config.py and replace your-openai-api-key with your OpenAI API key
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