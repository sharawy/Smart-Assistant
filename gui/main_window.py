import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
from threading import Thread
from config import APP_TITLE, WINDOW_SIZE
from logic.app_logic import handle_input

class SmartAssistantApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(APP_TITLE)
        self.window.geometry(WINDOW_SIZE)

        self.input_field = tk.Entry(self.window, width=80)
        self.input_field.pack(pady=10)
        self.input_field.bind("<Return>", lambda event: self.process_input())

        self.submit_button = tk.Button(self.window, text="Submit", command=self.process_input)
        self.submit_button.pack(pady=5)

        self.output_area = scrolledtext.ScrolledText(self.window, height=15, width=85, state='disabled')
        self.output_area.pack(pady=10)

        self.log_area = scrolledtext.ScrolledText(self.window, height=10, width=85, state='disabled')
        self.log_area.pack(pady=10)

        self.status_label = tk.Label(self.window, text="Ready", fg="green")
        self.status_label.pack()

    def append_to_output(self, user_input, response):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        self.output_area.configure(state='normal')
        self.output_area.insert(tk.END, f"{timestamp}\nYou: {user_input}\nAssistant: {response}\n\n")
        self.output_area.configure(state='disabled')
        self.output_area.see(tk.END)

    def log_action(self, message):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, f"{timestamp} {message}\n")
        self.log_area.configure(state='disabled')
        self.log_area.see(tk.END)

    def run_llm_threaded(self, user_input):
        try:
            self.status_label.config(text="Processing...")
            response, action = handle_input(user_input)
            self.append_to_output(user_input, response)
            self.log_action(f"Action taken: {action}")
            self.status_label.config(text=f"Done: {action}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.log_action(f"Error: {str(e)}")
            self.status_label.config(text="Error")

    def process_input(self):
        user_input = self.input_field.get().strip()
        if not user_input:
            messagebox.showwarning("Empty Input", "Please enter a command.")
            return

        self.input_field.delete(0, tk.END)
        thread = Thread(target=self.run_llm_threaded, args=(user_input,))
        thread.start()

    def run(self):
        self.window.mainloop()