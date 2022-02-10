import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text Maker")

def cl():
    txt = a.get(1.0, "end-1c")
    with open("file.txt", 'w') as f:
        f.write(txt)

a = tk.Text(root)
b = ttk.Button(root, text='Make', command=cl)
a.pack()
b.pack()


root.mainloop()
