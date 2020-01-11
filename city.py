import random
import math
from block import *

class City:
    def __init__(self, canvas, width, height, cell_width):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.possible_x_coords = [i for i in range(0, width, cell_width)]
        self.possible_y_coords = [i for i in range(0, height, cell_width)]
        self.destinations = []
        self.obstacles = []
        self.grid = [["empty" for _ in range(len(self.possible_x_coords))] for _ in range(len(self.possible_y_coords))]

    def create_destinations(self, destination_pos, mode = "random"):
        if mode == "random":
            for d in range(len(destination_pos)):
                end_x, end_y = destination_pos[d]
                cell_x, cell_y = math.floor(end_x / self.cell_width), math.floor(end_y / self.cell_width)
                new_dest = Block(self.canvas, 1, end_x, end_y, self.cell_width, 'blue')
                self.destinations.append(new_dest)
                self.grid[cell_y][cell_x] = "dest"

    def create_obstacles(self, obstacle_pos = [], mode = "random"):
        if mode == "random":
            num_cells = int(math.floor(self.width / self.cell_width) * math.floor(self.height / self.cell_width))
            num_obstacles = random.randint(0, num_cells)
            for _ in range(num_obstacles):
                new_x, new_y = random.choice(self.possible_x_coords), random.choice(self.possible_y_coords)
                cell_x, cell_y = math.floor(new_x / self.cell_width), math.floor(new_y / self.cell_width)
                new_obstacle = Block(self.canvas, 0, new_x, new_y, self.cell_width, 'brown')
                self.obstacles.append(new_obstacle)
                self.grid[cell_y][cell_x] = "obst"

    def cell_type(self, x, y):
        cell_x, cell_y = math.floor(x / self.cell_width), math.floor(y / self.cell_width)
        return self.grid[cell_y][cell_x]
