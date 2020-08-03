from Game import MazeBoard

import tkinter as tk

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intervals of 100
    for i in range(0, w, 50):
        c.create_line([(i, 0), (i, h)], tag='grid_line')
        c.create_line([(0, i), (w, i)], tag='grid_line')

    # Inserts Circles for Maze
    for i in range(0, w, 50):
        for j in range(0, w, 50):
            c.create_oval([(j, i+50), (50+j, i)])
    #   c.create_oval([(0, i+50), (i, 50)])

root = tk.Tk()


c = tk.Canvas(root, height=500, width=500, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)

root.mainloop()
