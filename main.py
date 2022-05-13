import pickle
import tkinter as tk
from random import choice
from tkinter import ttk


class Gui(tk.Tk):
    def __init__(self, word_list):
        super().__init__()

        self.title("Wordle Clone")
        self.geometry("630x600+900+300")
        self.NUM_GUESSES = 6
        self.word_list = word_list

        self.board_frame = tk.Frame(self)
        guess_frame = tk.Frame(self)
        guess_frame.grid(row=1, column=0)
        self.guess_entry = tk.Entry(guess_frame, font="Helvetica 15")
        self.guess_entry.pack(side="left", padx=20, pady=20)
        self.guess_button = ttk.Button(
            guess_frame, text="Guess", width=15, command=self.make_guess
        )
        self.guess_button.pack(side="left", padx=[0, 20])
        new_word_button = ttk.Button(
            guess_frame, text="New Word", width=15, command=self.game_setup
        )
        new_word_button.pack(side="left")

        self.word_label = ttk.Label(
            self, width=10, anchor="center", font="Helvetica 30"
        )
        self.word_label.grid()

        self.game_setup()

    def display_board(self):
        self.board_frame.destroy()
        self.board_frame = tk.Frame(self, background="#121213")
        self.board_frame.grid(row=0, column=0, ipadx=50, ipady=20)

        for row in self.board:
            row_frame = tk.Frame(self.board_frame, bg="#121213")
            row_frame.pack()

            for char in zip(row, self.word):
                border_color = tk.Frame(row_frame)
                border_color.pack(side="left", padx=3, pady=3)
                color = self.get_color(char)
                ttk.Label(
                    border_color,
                    text=char[0],
                    foreground="#FFFFFF",
                    background=color,
                    font="Courier 30 bold",
                    anchor="center",
                ).pack(ipadx=20, padx=3, pady=3)

                color = "#3A3A3C" if char[0] == " " else color
                border_color.config(bg=color)

    def get_color(self, char):
        if char[0] == char[1]:
            return "#538D4E"
        elif char[0] in self.word:
            return "#B59F3B"
        elif char[0] == " ":
            return "#121213"
        else:
            return "#3A3A3C"

    def make_guess(self):
        guess = self.guess_entry.get().upper()
        if not guess.isalpha() or len(guess) != 5:
            return

        self.board[self.guess_number] = list(guess)
        self.guess_number += 1
        self.display_board()

        if guess == self.word:
            self.on_win()
        elif self.guess_number >= self.NUM_GUESSES:
            self.on_lose()

    def on_win(self):
        print("Victory")
        self.guess_button.config(state="disabled")
        self.word_label.config(text=self.word)

    def on_lose(self):
        print("Lost")
        self.guess_button.config(state="disabled")
        self.word_label.config(text=self.word)

    def game_setup(self):
        self.guess_button.config(state="normal")
        self.word_label.config(text="")
        self.guess_number = 0
        self.word = choice(word_list).upper()
        self.board = [[" " for _ in range(5)] for _ in range(self.NUM_GUESSES)]
        self.display_board()
        print(self.word)


if __name__ == "__main__":
    with open("word_list.pkl", "rb") as open_file:
        word_list = pickle.load(open_file)

    gui = Gui(word_list)
    gui.mainloop()
