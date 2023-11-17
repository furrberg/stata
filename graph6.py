import main
import tkinter as tk
import graph1, graph2, graph3, graph4, graph5

tk.set_appearance_mode("system")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()

root.geometry("800x500")

def login():
    print("Test")

def graph1f(x):
    return x

def graph2f(x):
    return x

def graph3f(x):
    return x

def graph4f(x):
    return x

def graph5f(x):
    return x

def graph6f(x):
    return x

def graph7f(x):
    return x

def graph8f(x):
    return x


frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tk.CTkLabel(master=frame, text="Stat project", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = tk.CTkEntry(master=frame, placeholder_text="Username")

entry1.pack(pady=12, padx=10)

button = tk.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

root.mainloop()
