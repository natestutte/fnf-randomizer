#! /usr/bin/env python

import tkinter as tk
from tkinter import filedialog
from fnf_randomizer import startRandomize

def activate():
    startRandomize(fnf_path.get(), bool(notes.get()), bool(chars.get()), bool(order.get()))

def browsePath():
    filename = filedialog.askdirectory()
    fnf_path.set(filename)

root = tk.Tk()

root.geometry("300x400")

frame = tk.Frame(root)
frame.pack()

fnf_path = tk.StringVar()
path_label = tk.Label(frame, textvariable=fnf_path)
path_label.pack(padx=5, pady=5)

submitBttn = tk.Button(frame, text="Set FNF Path", command=browsePath)
submitBttn.pack(padx=5, pady=5)

notes = tk.IntVar()
chars = tk.IntVar()
order = tk.IntVar()

notesBttn = tk.Checkbutton(frame, text="Randomize Notes", width=15, variable=notes)
notesBttn.pack(padx=5, pady=5)
charsBttn = tk.Checkbutton(frame, text="Randomize Characters", width=15, variable=chars)
charsBttn.pack(padx=5, pady=5)
orderBttn = tk.Checkbutton(frame, text="Randomize Order", width=15, variable=order)
orderBttn.pack(padx=5, pady=5)

submitBttn = tk.Button(frame, text="Randomize", command=activate)
submitBttn.pack(padx=5, pady=5)

root.mainloop()