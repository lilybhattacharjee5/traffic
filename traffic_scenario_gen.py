import math
import random
from utils import *

possible_x_coords = lambda window_width, cell_width: possible_coords(0, window_width, cell_width)
possible_y_coords = lambda window_height, cell_width: possible_coords(0, window_height, cell_width)

# different block start positions
def random_pos(window_width, window_height, cell_width, num_agents):
    all_x = possible_x_coords(window_width, cell_width)
    all_y = possible_y_coords(window_height, cell_width)
    pos = [(random.choice(all_x), random.choice(all_y)) for _ in range(num_agents)]
    return pos

def col_pos(x, window_width, window_height, cell_width, num_agents):
    all_y = possible_y_coords(window_height, cell_width)
    pos = [(x, random.choice(all_y)) for _ in range(num_agents)]
    return pos

def color_pairs(num_agents):
    agent_colors = []
    dest_colors = []
    for i in range(num_agents):
        a = '#%02x%02x%02x' % (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        d = a
        agent_colors.append(a)
        dest_colors.append(d)
    return agent_colors, dest_colors
