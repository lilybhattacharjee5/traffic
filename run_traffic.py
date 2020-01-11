import tkinter as tk
import sys
from agent import *
from city import *
from display_utils import *

cell_width = int(sys.argv[1])
num_agents = int(sys.argv[2])

window_width, window_height = 1000, 1000
possible_x_coords = possible_coords(0, window_width, cell_width)
possible_y_coords = possible_coords(0, window_height, cell_width)

agent_pos = [(random.choice(possible_x_coords), random.choice(possible_y_coords)) for _ in range(num_agents)]
destination_pos = [(random.choice(possible_x_coords), random.choice(possible_y_coords)) for _ in range(num_agents)]

window = tk.Tk()
window.title("Simulating Traffic")

canvas = tk.Canvas(window, height = window_height, width = window_height, bg = 'white', cursor = 'crosshair')
city = City(canvas, window_width, window_height, cell_width)

header = tk.Frame(window)
header_widget_h, header_widget_w = 1, 50

pos = tk.Text(window, height = header_widget_h, width = header_widget_w, name = "pos")
pos.insert(tk.INSERT, "Position: ?")

score = tk.Text(window, height = header_widget_h, width = header_widget_w, name = "score")
score.insert(tk.INSERT, "Score: ?")

pos.pack(in_ = header, side = 'left')
score.pack(in_ = header, side = 'left')

header.pack(side = 'top', anchor = 'w')

city.create_destinations(destination_pos)

agents = [Agent(window, canvas, city, agent_pos[i][0], agent_pos[i][1], destination_pos[i][0], destination_pos[i][1], cell_width, window_width, window_height, 'yellow') for i in range(len(agent_pos))]

city.create_obstacles()

canvas.pack(fill = tk.BOTH, expand = True)
canvas.bind('<Configure>', config_grid(canvas, window_width, window_height, cell_width))

config_move_agents(canvas, agents, cell_width)
window.mainloop()
