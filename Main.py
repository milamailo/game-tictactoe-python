import tkinter as tk
from TicTacToe import TicTacToe

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
