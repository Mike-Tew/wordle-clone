import pickle
import tkinter as tk
from random import choice
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self, word):
        super().__init__()

        self.title("Wordle Clone")
        self.geometry("+900+300")


if __name__ == "__main__":
    with open("word_list.pkl", "rb") as open_file:
        data = pickle.load(open_file)

    word = choice(data)
    print(word)

    gui = Gui(word)
    gui.mainloop()
