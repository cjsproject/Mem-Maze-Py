from Game import MazeBoard
from GUI.CreateGrid import create_c_grid

import tkinter as tk
from time import sleep


class GUI:  # turn the GUI into a class
    x = MazeBoard.BoardGame()
    root = tk.Tk()
    root.title("Memory Maze")

    length = 500
    step = length // x.getDim()

    c = tk.Canvas(root, height=length, width=length, bg='#fdffb4')
    tk.Label(root, text="c grid").pack()  # packs in order of compilation, label first, then grid

    create_c_grid(c, x, step)

    c.pack(fill=tk.BOTH, expand=True)

    root.resizable(0, 0)
    root.mainloop()

    # define canvas bindings here def fcn(self, widget, signal, event)
