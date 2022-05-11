import pickle
import tkinter as tk
from random import choice
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self, word):
        super().__init__()

        self.NUM_GUESSES = 6

        self.title("Wordle Clone")
        self.geometry("+900+300")

        self.board = [["-" for _ in range(5)] for _ in range(self.NUM_GUESSES)]
        print(self.board)

        self.prev_guess_frame = ttk.LabelFrame(self, text="Guesses")
        self.prev_guess_frame.pack()

        self.display_board()

        self.guess_entry = tk.Entry(self.prev_guess_frame, font="Helvetica 15")
        self.guess_entry.pack(side="left", padx=20, pady=20)
        self.guess_button = ttk.Button(
            self.prev_guess_frame, text="Guess", width=20, command=self.make_guess
        )
        self.guess_button.pack(side="right", padx=[0, 20])

    def display_board(self):
        for row in self.board:
            row_frame = ttk.Frame(self.prev_guess_frame)
            row_frame.pack()
            for char in row:
                ttk.Label(row_frame, text=char, font="Helvetica 30").pack(
                    side="left", padx=10
                )

    def make_guess(self):
        guess = self.guess_entry.get()
        print(guess)


if __name__ == "__main__":
    with open("word_list.pkl", "rb") as open_file:
        data = pickle.load(open_file)

    word = choice(data)
    print(word)

    gui = Gui(word)
    gui.mainloop()
