import tkinter as tk

root = tk.Tk()
root.title("Text Maker")

def cl():
    with open("file.txt", 'w') as f:
        f.write()

a = tk.Text(root)
b = tk.Text(root, text='Make', command=cl)
a.pack()
b.pack()


root.mainloop()
