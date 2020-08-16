from Game import MazeBoard

import tkinter as tk
from time import sleep


def create_d_grid(event=None):
    w = d.winfo_width() # Get current width of canvas
    h = d.winfo_height() # Get current height of canvas
    d.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intervals of 100
    for i in range(0, w, 35):
        d.create_line([(i, 0), (i, h)], tag='grid_line')
        d.create_line([(0, i), (w, i)], tag='grid_line')

    # Inserts Circles for Maze
    for i in range(0, w, 35):
        for j in range(0, w, 35):
            d.create_oval([(j, i+35), (35+j, i)], fill='blue')


def create_c_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line
    circles = []
    board = x.getBoard()
    mp = x.solution()

    # Creates all vertical lines at intervals of 100
    for i in range(0, w, 35):
        c.create_line([(i, 0), (i, h)], tag='grid_line')
        c.create_line([(0, i), (w, i)], tag='grid_line')

    # Inserts Circles for Maze, used list comprehension for simple access later
    circles = [[c.create_oval([(j, i+35), (35+j, i)]) for i in range(0, w, 35)] for j in range(0, w, 35)]
    horiz = 0
    vert = 0

    # color the circles green if they are inside of the solution points
    for i in board:
        horiz = 0
        for j in i:
            if j in mp:
                print("(", mp.index(j) + 1, ")", end='\t')
                c.itemconfigure(circles[horiz][vert], fill='green') # item configure the actual canvas object in circles list
            else:
                print(j, end='\t')
            horiz += 1
            c.update()
        vert += 1
        print()



x = MazeBoard.BoardGame()

print(x)

root = tk.Tk()
root.title("Memory Maze")

label1 = tk.Label(root, text="c grid")
label1.pack()#packs in order of compilation, label first, then grid


c = tk.Canvas(root, height=350, width=350, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_c_grid)

label2 = tk.Label(root, text="d grid")
label2.pack()
d = tk.Canvas(root, height=350, width=350, bg='white')
d.pack(fill=tk.BOTH, expand=True)

d.bind('<Configure>', create_d_grid)

root.resizable(0, 0)
root.mainloop()
