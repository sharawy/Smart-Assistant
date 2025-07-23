import tkinter as tk
from tkinter import ttk
from logic.app_logic import say_hello

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill='both', expand=True)

        self.label = ttk.Label(self.frame, text="Welcome to Tkinter!")
        self.label.pack(pady=10)

        self.button = ttk.Button(self.frame, text="Say Hello", command=self.say_hello)
        self.button.pack()

    def say_hello(self):
        say_hello()
