import tkinter as tk
from tkinter import messagebox

class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player_symbol):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = player_symbol
            return True
        return False

    def check_winner(self):
        # Проверка строк, столбцов и диагоналей
        for row in range(3):
            if self.grid[row][0] == self.grid[row][1] == self.grid[row][2] != ' ':
                return self.grid[row][0]
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != ' ':
                return self.grid[0][col]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
            return self.grid[0][2]
        return None

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики")
        self.board = Board()
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=' ', font=('Arial', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.board.make_move(row, col, self.current_player):
            self.buttons[row][col].config(text=self.current_player)
            winner = self.board.check_winner()
            if winner:
                messagebox.showinfo("Поздравляем!", f"Игрок {winner} выиграл!")
                self.reset_game()
            elif all(cell != ' ' for row in self.board.grid for cell in row):
                messagebox.showinfo("Ничья", "Игра закончилась вничью!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.board = Board()
        self.current_player = 'X'
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
