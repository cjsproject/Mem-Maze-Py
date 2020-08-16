# Draws circles, populates with solution
def create_c_grid(c, x, step):
    w = step * x.getDim()  # Get current width of canvas
    h = step * x.getDim()  # Get current height of canvas
    c.delete('grid_line')  # Will only remove the grid_line
    c.delete('circle')  # Will remove circles
    circles = []
    board = x.getBoard()
    mp = x.solution()

    # Creates all vertical lines at intervals of 100
    for i in range(0, w, step):
        c.create_line([(i, 0), (i, h)], tag='grid_line')
        c.create_line([(0, i), (w, i)], tag='grid_line')

    # Inserts Circles for Maze, used list comprehension for simple access later
    circles = [[c.create_oval([(j, i + step), (step + j, i)], fill='#c3bbec', activeoutline='red', tag='circle')
                for i in range(0, w, step)] for j in range(0, w, step)]
    horiz = 0
    vert = 0

    # color the circles green if they are inside of the solution points
    for i in board:
        horiz = 0
        for j in i:
            if j in mp:
                print("(", mp.index(j) + 1, ")", end='\t')
                c.itemconfigure(circles[horiz][vert], fill='#0bcd74')  # item configure the actual canvas object in circles list, light green
                c.create_text(horiz * step + step // 2, vert * step + step // 2, text=str(mp.index(j) + 1))
            else:
                print(j, end='\t')
            horiz += 1
            # c.update()
        vert += 1
        print()
