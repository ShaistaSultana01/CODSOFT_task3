import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    use_upper = var_upper.get()
    use_lower = var_lower.get()
    use_digits = var_digits.get()
    use_symbols = var_symbols.get()

    if not (use_upper or use_lower or use_digits or use_symbols):
        messagebox.showwarning("Selection Error", "Please select at least one character type.")
        return

    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def clear_fields():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x370")
root.resizable(0,0)


tk.Label(root, text="Password Generator", font=("lucida",16, "bold")).pack(pady=10)


tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)


var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor='w', padx=40)


tk.Button(root, text="Generate Password", command=generate_password, bg="black", fg="white").pack(pady=10)


password_entry = tk.Entry(root, font=("lucida",14), justify="center")
password_entry.pack(pady=5)


tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)


root.mainloop()
