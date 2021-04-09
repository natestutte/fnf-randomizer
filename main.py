#! /usr/bin/env python

from os import path
import tkinter as tk
from tkinter import filedialog
from fnf_randomizer import startRandomize

def activate():
    statusLabel.config(state=tk.NORMAL)
    statusLabel.delete(1.0, tk.END)
    statusLabel.config(state=tk.DISABLED)
    activate_status = startRandomize(fnf_path.get(), bool(notes.get()), bool(chars.get()), bool(order.get()), bool(single.get()))
    statusLabel.config(state=tk.NORMAL)
    statusLabel.insert(tk.END, activate_status)
    statusLabel.config(state=tk.DISABLED)

def browsePath():
    filename = filedialog.askdirectory()
    fnf_path.set(filename)

def switchOrder():
    if order.get() == 1:
        orderBttn.toggle()
    if orderBttn["state"] == tk.NORMAL:
        orderBttn["state"] = tk.DISABLED
    elif orderBttn["state"] == tk.DISABLED:
        orderBttn["state"] = tk.NORMAL

def main():
    root = tk.Tk()

    root.geometry("300x450")
    root.resizable(False, False)

    frame = tk.Frame(root)
    frame.pack()

    title_label = tk.Label(frame, font=("Helvetia 12 bold"), text="Friday Night Funkin' Randomizer\nBy Magfmur", wraplength=260)
    title_label.pack(padx=5, pady=5)

    fnf_path = tk.StringVar()
    fnf_path.set(path.abspath(__file__))
    path_label = tk.Label(frame, font=("Helvetia 10"), textvariable=fnf_path, relief="ridge", wraplength=260)
    path_label.pack(padx=5, pady=5)

    submitBttn = tk.Button(frame, font=("Helvetia 10"), text="Set FNF Path", command=browsePath)
    submitBttn.pack(padx=5, pady=5)

    notes = tk.IntVar()
    chars = tk.IntVar()
    order = tk.IntVar()
    single = tk.IntVar()

    notesBttn = tk.Checkbutton(frame, font=("Helvetia 10"), text="Randomize Notes", width=20, variable=notes)
    notesBttn.pack(padx=5, pady=2)
    charsBttn = tk.Checkbutton(frame, font=("Helvetia 10"), text="Randomize Characters", width=20, variable=chars)
    charsBttn.pack(padx=5, pady=2)
    orderBttn = tk.Checkbutton(frame, font=("Helvetia 10"), text="Randomize Order", width=20, variable=order)
    orderBttn.pack(padx=5, pady=2)
    singleBttn = tk.Checkbutton(frame, font=("Helvetia 10"), text="Solo Mode", width=20, variable=single, command=switchOrder)
    singleBttn.pack(padx=5, pady=2)

    submitBttn = tk.Button(frame, font=("Helvetia 14"), text="Randomize", command=activate)
    submitBttn.pack(padx=5, pady=5)

    scroll = tk.Scrollbar(frame, orient="vertical")
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    status = tk.StringVar()
    statusLabel = tk.Text(frame, font=("Helvetia 12"), state=tk.DISABLED, yscrollcommand=scroll.set)
    statusLabel.pack(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()