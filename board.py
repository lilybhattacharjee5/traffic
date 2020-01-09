import tkinter as tk
import sys
from agent import *

cell_width = int(sys.argv[1])
start_x = int(sys.argv[2])
start_y = int(sys.argv[3])

m = tk.Tk()

m.title("Simulating Traffic")

def create_grid(event = None, cell_width = 10):
    w = c.winfo_width() # current width of canvas
    h = c.winfo_height() # current height of canvas
    c.delete('grid_line') # will only remove the grid lines

    # Creates all vertical lines at intervals of cell_width
    for i in range(0, w, cell_width):
        c.create_line([(i, 0), (i, h)], tag = 'grid_line', fill = 'white')

    # Creates all horizontal lines at intervals of cell_width
    for i in range(0, h, cell_width):
        c.create_line([(0, i), (w, i)], tag = 'grid_line', fill = 'white')

def config_grid(event = None):
    return create_grid(event, cell_width = cell_width)

c = tk.Canvas(m, height = 1000, width = 1000, bg = 'black')
agent = Agent(start_x, start_y, cell_width, c)

c.pack(fill = tk.BOTH, expand = True)

c.bind('<Configure>', config_grid)

def move_agent():
    agent.move(5, 5, "diag_lu")
    c.after(100, move_agent)
move_agent()
m.mainloop()
