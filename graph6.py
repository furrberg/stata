import main
import tkinter as tk
#import graph1, graph2, graph3, graph4, graph5

tk.set_appearance_mode("system")
tk.set_default_color_theme("dark-blue")

root = tk.Tk()

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


frame = tk.Frame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tk.Label(master=frame, text="Stat project", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = tk.Entry(master=frame, placeholder_text="Username")

entry1.pack(pady=12, padx=10)

button = tk.Button(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

root.mainloop()
