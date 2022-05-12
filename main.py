import pickle
import tkinter as tk
from random import choice
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self, word):
        super().__init__()

        self.word = word
        self.NUM_GUESSES = 6
        self.guess_number = 0

        self.title("Wordle Clone")
        self.geometry("630x450+900+300")

        self.board = [["__" for _ in range(5)] for _ in range(self.NUM_GUESSES)]
        print(self.board)
        self.board_frame = ttk.LabelFrame(self)
        self.display_board()

        guess_frame = tk.Frame(self)
        guess_frame.place(x=20, y=350)
        self.guess_entry = tk.Entry(guess_frame, font="Helvetica 15")
        self.guess_entry.pack(side="left", padx=20, pady=20)
        self.guess_button = ttk.Button(
            guess_frame, text="Guess", width=20, command=self.make_guess
        )
        self.guess_button.pack(side="right", padx=[0, 20])

    def display_board(self):
        self.board_frame.destroy()
        self.board_frame = ttk.LabelFrame(self, text="Guesses")
        self.board_frame.place(x=100, y=10)

        for row in self.board:
            row_frame = ttk.Frame(self.board_frame)
            row_frame.pack()
            for char in zip(row, self.word):
                color = self.get_color(char)
                # print(char, char[0] == char[1])
                ttk.Label(
                    row_frame,
                    text=char[0],
                    foreground="white",
                    background=color,
                    font="Helvetica 30",
                    anchor="center",
                ).pack(side="left", ipadx=20)

    def get_color(self, char):
        if char[0] == char[1]:
            return "green"
        elif char[0] in self.word:
            return "yellow"
        else:
            return "black"

    def make_guess(self):
        guess = list(self.guess_entry.get().upper())
        print(guess)
        self.board[self.guess_number] = guess
        self.guess_number += 1
        self.display_board()


if __name__ == "__main__":
    with open("word_list.pkl", "rb") as open_file:
        data = pickle.load(open_file)

    word = choice(data).upper()
    print(word)

    gui = Gui(word)
    gui.mainloop()
