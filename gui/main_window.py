import tkinter as tk
from tkinter import scrolledtext  # (Note: This is imported but not used)

# Simulated function to search on Google
def google_search(query):
    return f"Opening browser and searching for: {query}"

# Simulated function to take a screenshot
def take_screenshot():
    return "Screenshot taken (simulated)"

# Simulated function to open Microsoft Word
def start_word():
    return "Microsoft Word opened (simulated)"

# Simulated function to adjust volume
def adjust_volume(level):
    return f"Volume set to: {level}"

# Function to process user input and generate assistant's response
def assistant_response(command):
    command = command.lower()  # Convert input to lowercase for easier comparison
    
    # Check for keywords and decide what response to return
    if "google" in command or "search" in command:
        return google_search(command)
    elif "screenshot" in command:
        return take_screenshot()
    elif "word" in command:
        return start_word()
    elif "volume" in command:
        if "high" in command:
            return adjust_volume("high")
        elif "low" in command:
            return adjust_volume("low")
        else:
            return "I didn't understand the volume level you want."
    else:
        # Default response for general questions
        return f"General question: {command}\nResponse: This is a reply from the Large Language Model (LLM)"

# Function called when the user clicks "Submit" or presses Enter
def on_submit():
    command = entry.get()  # Get user input from the text field
    
    if command.lower() == "exit":  # Exit the program if user types 'exit'
        root.destroy()
    elif command.strip() == "":  # If input is empty, show warning in status log
        status_log_insert("Empty command. Please type something.")
    else:
        # Show the user's command and assistant's response in the chat window
        output_text_insert(f"> You: {command}")
        response = assistant_response(command)
        output_text_insert(f"Assistant: {response}")
        
        # Log the executed command
        status_log_insert(f"Executed command: {command}")
    
    # Clear the input field after submitting
    entry.delete(0, tk.END)

# Function to clear the chat history
def clear_output():
    output_text.configure(state='normal')
    output_text.delete('1.0', tk.END)
    output_text.configure(state='disabled')
    status_log_insert("Chat cleared.")

# Helper function to display messages in the chat area
def output_text_insert(text):
    output_text.configure(state='normal')
    output_text.insert(tk.END, text + "\n\n")
    output_text.see(tk.END)  # Automatically scroll to the bottom
    output_text.configure(state='disabled')

# Helper function to display messages in the status log
def status_log_insert(text):
    status_log.configure(state='normal')
    status_log.insert(tk.END, text + "\n")
    status_log.see(tk.END)
    status_log.configure(state='disabled')

# -------------------- GUI Layout --------------------

# Create the main application window
root = tk.Tk()
root.title("Smart Personal Assistant")  # Window title
root.geometry("700x600")  # Window size in pixels (width x height)

# Title label at the top of the window
title = tk.Label(root, text="Smart Personal Assistant", font=("Helvetica", 18, "bold"))
title.pack(pady=10)  # Add padding below the title

# Frame to contain the chat output (conversation)
output_frame = tk.Frame(root)
output_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Text widget to display conversation with the assistant
output_text = tk.Text(output_frame, height=15, wrap=tk.WORD, state='disabled', font=("Courier", 14))
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for the chat output
output_scroll = tk.Scrollbar(output_frame, command=output_text.yview)
output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
output_text['yscrollcommand'] = output_scroll.set

# Frame to contain the status log
status_frame = tk.Frame(root)
status_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Label for status log section
status_label = tk.Label(status_frame, text="Status Log:", font=("Helvetica", 12, "bold"))
status_label.pack(anchor='w')  # Align to the left

# Text widget for status messages (e.g., executed commands, errors)
status_log = tk.Text(
    status_frame,
    height=7,
    wrap=tk.WORD,
    state='disabled',
    font=("Courier", 14, "bold"),  # Bold font
    bg="#d0e7f9",                  # Light blue background
    fg="#003366"                   # Dark blue text color
)
status_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for the status log
status_scroll = tk.Scrollbar(status_frame, command=status_log.yview)
status_scroll.pack(side=tk.RIGHT, fill=tk.Y)
status_log['yscrollcommand'] = status_scroll.set

# Frame to contain the input field and buttons
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10, fill=tk.X)

# Entry widget where the user types commands
entry = tk.Entry(input_frame, font=("Helvetica", 14))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,10))
entry.focus()  # Focus the cursor here when app starts

# Button to submit the typed command
submit_button = tk.Button(input_frame, text="Submit", command=on_submit, font=("Helvetica", 12))
submit_button.pack(side=tk.LEFT)

# Button to clear the chat history
clear_button = tk.Button(input_frame, text="Clear Chat", command=clear_output, font=("Helvetica", 12))
clear_button.pack(side=tk.LEFT, padx=(10,0))

# Allow pressing the Enter key to also submit the command
def enter_pressed(event):
    on_submit()
entry.bind('<Return>', enter_pressed)

# Show a welcome message in the status log when the app starts
status_log_insert("Welcome! Type your command and press Submit.")

# Start the GUI application loop
root.mainloop()
