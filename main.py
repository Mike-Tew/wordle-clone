import tkinter as tk
from random import choice
from tkinter import ttk
from turtle import width

from all_words import all_words
from word_list import word_list


class Gui(tk.Tk):
    def __init__(self, word_list, all_words):
        super().__init__()

        self.title("Wordle Clone")
        self.geometry("500x670+900+200")
        self.NUM_GUESSES = 6
        self.word_list = word_list
        self.all_words = all_words
        self.config(bg="#121213", padx=30, pady=30)

        self.board_frame = tk.Frame(self)
        guess_frame = tk.Frame(self, bg="#121213")
        guess_frame.grid(row=1, column=0)

        vcmd = (self.register(self.validate), "%P")
        self.guess_entry = tk.Entry(
            guess_frame,
            width=6,
            font="Courier 20 bold",
            validate="key",
            validatecommand=vcmd,
        )
        self.guess_entry.pack(side="left", padx=20, pady=20)
        self.guess_button = tk.Button(
            guess_frame,
            text="Guess",
            font="Helvetica 12 bold",
            width=10,
            command=self.make_guess,
        )
        self.guess_button.pack(side="left", padx=[0, 20])
        self.bind("<Return>", lambda x=None: self.guess_button.invoke())

        new_word_button = ttk.Button(
            guess_frame, text="New Word", width=10, command=self.game_setup
        )
        new_word_button.pack(side="left")

        self.keyboard_frame = ttk.Frame(self)
        self.green_keys = []
        self.yellow_keys = []
        self.black_keys = []

        self.game_setup()

    def validate(self, value):
        if value.lower() in self.all_words:
            self.guess_button.config(bg="#538D4E", state="normal")
            return True
        if len(value) <= 5:
            self.guess_button.config(bg="SystemButtonFace", state="disabled")
            return True
        return False

    def display_board(self):
        self.board_frame.destroy()
        self.board_frame = tk.Frame(self, background="#121213")
        self.board_frame.grid(row=0, column=0)

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
                ).pack(ipadx=10, padx=3, pady=3)

                color = "#3A3A3C" if char[0] == " " else color
                border_color.config(bg=color)

    def get_color(self, char):
        self.black_keys.append(char[0])
        if char[0] == char[1]:
            self.green_keys.append(char[0])
            return "#538D4E"
        elif char[0] in self.word:
            self.yellow_keys.append(char[0])
            return "#B59F3B"
        elif char[0] == " ":
            return "#121213"
        else:
            return "#3A3A3C"

    def make_guess(self):
        if not self.validate:
            return

        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, "end")

        self.board[self.guess_number] = list(guess)
        self.guess_number += 1
        self.display_board()

        for key in self.key_buttons:
            if key["text"] in self.green_keys:
                key.config(bg="#538D4E")
            elif key["text"] in self.yellow_keys:
                key.config(bg="#B59F3B")
            elif key["text"] in self.black_keys:
                key.config(bg="#3A3A3C")

        if guess == self.word or self.guess_number >= self.NUM_GUESSES:
            self.game_end()

    def game_end(self):
        self.word_label = tk.Label(
            self,
            bg="#1A1A1A",
            fg="#FFFFFF",
            width=12,
            anchor="center",
            font="Helvetica 30",
            pady=20,
        )
        self.word_label.place(x=85, y=20)
        self.word_label.config(text=self.word)

    def game_setup(self):
        self.guess_entry.focus()
        self.guess_button.config(state="disabled")
        self.guess_number = 0
        self.word = choice(self.word_list).upper()
        self.board = [[" " for _ in range(5)] for _ in range(self.NUM_GUESSES)]
        self.display_board()

        keys = [
            "Q",
            "W",
            "E",
            "R",
            "T",
            "Y",
            "U",
            "I",
            "O",
            "P",
            "A",
            "S",
            "D",
            "F",
            "G",
            "H",
            "J",
            "K",
            "L",
            "ENT",
            "Z",
            "X",
            "C",
            "V",
            "B",
            "N",
            "M",
            "<-",
        ]
        self.green_keys = []
        self.yellow_keys = []
        self.black_keys = []
        self.keyboard_frame = tk.Frame(self, width=10, bg="#121213")
        self.keyboard_frame.grid(row=2, column=0)
        self.key_row_1 = tk.Frame(self.keyboard_frame, bg="#121213")
        self.key_row_1.pack()
        self.key_row_2 = tk.Frame(self.keyboard_frame, bg="#121213")
        self.key_row_2.pack()
        self.key_row_3 = tk.Frame(self.keyboard_frame, bg="#121213")
        self.key_row_3.pack()

        self.key_buttons = [self.create_key(key) for key in keys]

        print(self.word)

    def create_key(self, key):
        frame = self.key_row_3
        if key in "QWERTYUIOP":
            frame = self.key_row_1
        elif key in "ASDFGHJKL":
            frame = self.key_row_2

        key_button = tk.Button(
            frame,
            text=key,
            font="Courier 12",
            fg="#FFFFFF",
            bg="#818384",
            command=lambda: self.send_keypress(key),
            takefocus=0,
        )
        key_button.pack(side="left", padx=3, pady=3, ipadx=7, ipady=7)
        return key_button

    def send_keypress(self, key):
        print(key)
        if key == "ENT":
            self.guess_button.invoke()
            return
        if key == "<-":
            self.guess_entry.delete(self.guess_entry.index("end") - 1)
            return
        self.guess_entry.insert(tk.END, key)


if __name__ == "__main__":
    gui = Gui(word_list, all_words)
    gui.mainloop()
