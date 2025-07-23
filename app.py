import tkinter as tk
from gui.main_window import MainWindow

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Tkinter App")
        self.window = MainWindow(self.root)

    def run(self):
        self.root.mainloop()
