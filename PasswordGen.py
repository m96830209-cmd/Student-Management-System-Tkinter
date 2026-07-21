import tkinter as tk
import random
import string

def generate_password():
    length = slider.get()

    characters = ""

    upper = var_upper.get()
    lower = var_lower.get()
    digits = var_digits.get()
    symbols = var_symbols.get()

    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if characters == "":
        output_box.delete(0, tk.END)
        output_box.insert(0, "Select at least one option!")
        strength_label.config(text="Strength: -")
        return

    password = ""

    for i in range(length):
        password += random.choice(characters)

    output_box.delete(0, tk.END)
    output_box.insert(0, password)

    score = upper + lower + digits + symbols

    if length < 8 or score <= 2:
        strength_label.config(text="Strength: Weak 🔴", fg="red")
    elif length < 12 or score == 3:
        strength_label.config(text="Strength: Medium 🟡", fg="orange")
    else:
        strength_label.config(text="Strength: Strong 🟢", fg="green")


def copy_password():
    password = output_box.get()
    window.clipboard_clear()
    window.clipboard_append(password)
    copy_btn.config(text="Copied ✓")
    window.after(1500, lambda: copy_btn.config(text="Copy"))


window = tk.Tk()
window.title("Password Generator")
window.geometry("450x500")
window.resizable(False, False)
window.config(bg="#2C3E50")

title = tk.Label( window, text="Password Generator", font=("Arial", 18, "bold"),
bg="#2C3E50", fg="white")
title.pack(pady=10)

tk.Label(window, text="Password Length", bg="#2C3E50", fg="white").pack()

slider = tk.Scale(window, from_=4, to=32, orient="horizontal")
slider.set(12)
slider.pack()

var_upper = tk.IntVar(value=1)
var_lower = tk.IntVar(value=1)
var_digits = tk.IntVar(value=1)
var_symbols = tk.IntVar(value=0)

frame = tk.Frame(window, bg="#2C3E50")
frame.pack(pady=10)

tk.Checkbutton(frame, text="Uppercase", variable=var_upper, bg="#2C3E50", fg="white").grid(row=0, column=0)
tk.Checkbutton(frame, text="Lowercase", variable=var_lower, bg="#2C3E50", fg="white").grid(row=0, column=1)
tk.Checkbutton(frame, text="Numbers", variable=var_digits, bg="#2C3E50", fg="white").grid(row=1, column=0)
tk.Checkbutton(frame, text="Symbols", variable=var_symbols, bg="#2C3E50", fg="white").grid(row=1, column=1)
tk.Button(window, text="Generate Password", command=generate_password, bg="#1ABC9C",
fg="white",font=("Arial", 12, "bold")).pack(pady=10)

output_box = tk.Entry(window, font=("Arial", 14), justify="center", width=30)
output_box.pack(pady=10)

copy_btn = tk.Button( window,text="Copy",command=copy_password,bg="#3498DB",fg="white")
copy_btn.pack(pady=5)

strength_label = tk.Label(window, text="Strength: -", bg="#2C3E50", fg="white")
strength_label.pack(pady=10)



window.mainloop()

