import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from search import a_star_search
from sudoku import Sudoku

class SudokuBoard:
    def __init__(self):
        self.master = root
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.make_board()
    
    def make_board(self):
        """
        Displays a sudoku board where cell values can be entered
        """
        self.frame = tk.Frame(self.master, bg='black')
        self.frame.pack(fill='both', expand=True)
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = tk.Entry(self.frame, font=('Arial', 20), justify='center', width=3)
                cell.grid(row=i, column=j, padx=2, pady=2)
                row.append(cell)
            self.cells.append(row)
        
        solve_button = ttk.Button(self.master, text='Solve', command=self.solve)
        solve_button.pack(side=tk.LEFT)
        
        clear_button = ttk.Button(self.master, text='Clear', command=self.clear)
        clear_button.pack(side=tk.LEFT)
    
    def solve(self):
        for i in range(9):
            for j in range(9):
                value = self.cells[i][j].get()
                if value.isdigit():
                    self.board[i][j] = int(value)
                else:
                    self.board[i][j] = 0


        if Sudoku(self.board).is_puzzle_valid() == False:
            messagebox.showerror('Error', 'Please enter a valid solvable puzzle')
        else:
            if self.solve_board():
                for i in range(9):
                    for j in range(9):
                        self.cells[i][j].delete(0, tk.END)
                        self.cells[i][j].insert(0, str(self.board[i][j]))
            else:
                messagebox.showerror('Error', 'Cannot solve Sudoku board')
    
    def solve_board(self):
        return a_star_search(self.board)
    
    def clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.board[i][j] = 0

root = tk.Tk()
root.geometry('500x450')
root.title('Sudoku Puzzle Solver')
sudoku_board = SudokuBoard()
root.mainloop()
