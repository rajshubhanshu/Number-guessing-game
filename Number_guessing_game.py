import tkinter as tk
from tkinter import messagebox
import random

secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    try:
        guess = int(guess_var.get())
        attempts += 1
        if guess < secret_number:
            feedback.set("Too low! Try a higher number.")
        elif guess > secret_number:
            feedback.set("Too high! Try a lower number.")
        else:
            messagebox.showinfo("Congratulations!", f"Correct! You guessed it in {attempts} attempts.")
            root.destroy()
    except ValueError:
        feedback.set("Please select a number.")

root = tk.Tk()
root.title("Number Guessing Game")

tk.Label(root, text="Guess a number between 1 and 100:").pack(pady=10)

guess_var = tk.StringVar(value="1")
guess_options = [str(i) for i in range(1, 101)]
guess_menu = tk.OptionMenu(root, guess_var, *guess_options)
guess_menu.pack()

tk.Button(root, text="Submit Guess", command=check_guess).pack(pady=5)

feedback = tk.StringVar()
tk.Label(root, textvariable=feedback, fg="blue").pack(pady=5)

root.mainloop()
