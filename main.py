# Entry point for launching the Smart Assistant GUI application
from gui.main_window import SmartAssistantApp

if __name__ == "__main__":
    # Create and run the main application window
    app = SmartAssistantApp()
    app.run()