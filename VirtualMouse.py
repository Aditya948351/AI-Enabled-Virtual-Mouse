import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import subprocess
import time
import re

# Predefined password
PASSWORD = "123"

# Function to start the virtual mouse program
def start_virtual_mouse():
    name = name_entry.get()
    password = password_entry.get()

    if not validate_name(name):
        messagebox.showwarning("Invalid Name", "Please input a valid name.")
        return

    if name.lower() == "aditya" and password == PASSWORD:
        result = messagebox.askquestion("Confirmation",
                                        "Welcome Sir, do you want to turn on the virtual mouse program?")
        if result == 'yes':
            countdown(3)
            subprocess.Popen(['python', 'AI Mousehand gesture.py'])
        else:
            feedback = simpledialog.askstring("Feedback", "Please provide feedback:")
            if feedback:
                messagebox.showinfo("Thank You", "Thank you for your feedback!")
            else:
                messagebox.showinfo("Information", "No feedback provided.")
            # Close the program after feedback prompt
            root.quit()
    else:
        messagebox.showwarning("Invalid User", "You are not authorized to use this program.")

# Function for countdown
def countdown(count):
    label.config(text=f"Starting in {count} seconds...")
    if count > 0:
        root.after(1000, countdown, count - 1)
    else:
        label.config(text="")
        root.update()

# Function to validate name
def validate_name(name):
    pattern = r'^[a-zA-Z ]+$'
    return bool(re.match(pattern, name))

# Function to exit the program
def exit_program():
    feedback = simpledialog.askstring("Feedback", "Please provide feedback:")
    if feedback:
        messagebox.showinfo("Thank You", "Thank you for your feedback!")
    else:
        messagebox.showinfo("Information", "No feedback provided.")
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Virtual Mouse Control")

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Resize the image to fit the window
bg_image = Image.open("Image 455.jpg")
bg_image = bg_image.resize((screen_width, screen_height), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Set window size to screen dimensions
root.geometry(f"{screen_width}x{screen_height}")

# Background label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Name entry
name_label = tk.Label(root, text="Name:")
name_label.pack(pady=(10, 0))
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Password entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=(0, 10))

# Start button
start_btn = tk.Button(root, text="Start Virtual Mouse", command=start_virtual_mouse)
start_btn.pack(pady=10)

# Exit button
exit_btn = tk.Button(root, text="Exit", command=exit_program)
exit_btn.pack(pady=10)

# Countdown label
label = tk.Label(root, text="")
label.pack()

root.mainloop()
