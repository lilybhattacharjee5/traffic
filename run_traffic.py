import tkinter as tk
import sys
from agent import *
from city import *
from display_utils import *

cell_width = int(sys.argv[1])
start_x, start_y = int(sys.argv[2]), int(sys.argv[3])
end_x, end_y = int(sys.argv[4]), int(sys.argv[5])

agent_pos = [(start_x, start_y)]
destination_pos = [(end_x, end_y)]

window_width, window_height = 1000, 1000
window = tk.Tk()
window.title("Simulating Traffic")

canvas = tk.Canvas(window, height = window_height, width = window_height, bg = 'white', cursor = 'crosshair')
city = City(canvas, window_width, window_height, cell_width)

city.create_destinations(destination_pos)
city.create_obstacles()

agents = [Agent(canvas, city, start_x, start_y, end_x, end_y, cell_width, window_width, window_height, 'yellow')]

header = tk.Frame(window)
header_widget_h, header_widget_w = 1, 50

pos = tk.Text(window, height = header_widget_h, width = header_widget_w)
pos.insert(tk.INSERT, "Position: (%d, %d)" % (start_x, start_y))

score = tk.Text(window, height = header_widget_h, width = header_widget_w)
score.insert(tk.INSERT, "Score: ")

pos.pack(in_ = header, side = 'left')
score.pack(in_ = header, side = 'left')

header.pack(side = 'top', anchor = 'w')

canvas.pack(fill = tk.BOTH, expand = True)
canvas.bind('<Configure>', config_grid(canvas, window_width, window_height, cell_width))

config_move_agents(canvas, agents, cell_width)
window.mainloop()
