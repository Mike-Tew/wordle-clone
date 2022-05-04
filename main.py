import pickle
import tkinter as tk
from random import choice
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self, word):
        super().__init__()

        self.title("Wordle Clone")
        self.geometry("+900+300")

        self.guesses = [["a" for _ in range(5)] for _ in range(6)]
        print(self.guesses)

        self.prev_guess_frame = ttk.LabelFrame(self, text="Guesses")
        self.prev_guess_frame.pack()

        self.display_board()

        self.btn = ttk.Button(self.prev_guess_frame, text="Test")
        self.btn.pack()

    def display_board(self):
        for row in self.guesses:
            row_frame = ttk.Frame(self.prev_guess_frame)
            row_frame.pack()
            for char in row:
                ttk.Label(row_frame, text=char, font="Helvetica 30").pack(side="left")


if __name__ == "__main__":
    with open("word_list.pkl", "rb") as open_file:
        data = pickle.load(open_file)

    word = choice(data)
    print(word)

    gui = Gui(word)
    gui.mainloop()
