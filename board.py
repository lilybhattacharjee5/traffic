import tkinter as tk
import sys
from agent import *

cell_width = int(sys.argv[1])
start_x, start_y = int(sys.argv[2]), int(sys.argv[3])
end_x, end_y = int(sys.argv[4]), int(sys.argv[5])

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

header = tk.Frame(m)
header_widget_h, header_widget_w = 1, 50

pos = tk.Text(m, height = header_widget_h, width = header_widget_w)
pos.insert(tk.INSERT, "Position: (%d, %d)" % (start_x, start_y))

score = tk.Text(m, height = header_widget_h, width = header_widget_w)
score.insert(tk.INSERT, "Score: ")

pos.pack(in_ = header, side = 'left')
score.pack(in_ = header, side = 'left')

header.pack(side = 'top', anchor = 'w')

destination = c.create_rectangle(end_x, end_y, end_x + cell_width, end_y + cell_width, fill = 'blue', outline = 'blue')
agent = Agent(start_x, start_y, end_x, end_y, cell_width, c, 'yellow')

c.pack(fill = tk.BOTH, expand = True)

c.bind('<Configure>', config_grid)

def move_agent():
    if agent.x != end_x:
        agent.auto_move(mag_x = cell_width, mag_y = cell_width)
        pos.delete(1.0, tk.INSERT)
        pos.insert(tk.INSERT, "Position: (%d, %d)" % (agent.x, agent.y))
        c.after(100, move_agent)

move_agent()
m.mainloop()
