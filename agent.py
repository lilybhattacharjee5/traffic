import math

dirs = ["left", "right", "up", "down", "diag_ru", "diag_rd", "diag_lu", "diag_ld"]

class Agent:
    def __init__(self, start_x, start_y, dest_x, dest_y, size, canvas, color):
        self.x = start_x
        self.y = start_y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.size = size
        self.canvas = canvas
        self.obj = canvas.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill = color, outline = color)
        self.dist_traveled = 0

    def calc_move(self, mag_x, mag_y, direction):
        dir_x_y = {
            "left": (-mag_x, 0),
            "right": (mag_x, 0),
            "up": (0, -mag_y),
            "down": (0, mag_y),
            "diag_ru": (mag_x, -mag_y),
            "diag_rd": (mag_x, mag_y),
            "diag_lu": (-mag_x, -mag_y),
            "diag_ld": (-mag_x, mag_y),
        }
        return dir_x_y[direction]

    def move(self, mag_x, mag_y, direction):
        x_move, y_move = self.calc_move(mag_x, mag_y, direction)
        self.x += x_move
        self.y += y_move
        self.dist_traveled += abs(x_move) + abs(y_move)
        self.canvas.move(self.obj, x_move, y_move)

    def manhattan_heuristic(self, x, y):
        x_remain = abs(self.dest_x - x)
        y_remain = abs(self.dest_y - y)
        return x_remain + y_remain

    def distance_heuristic(self, x, y):
        x_remain = self.dest_x - x
        y_remain = self.dest_y - y
        return (x_remain**2 + y_remain**2)**0.5

    def next_move(self, mag_x, mag_y, heuristic):
        min_cost = math.inf
        opt_dir = "right"
        for d in dirs:
            x_offset, y_offset = self.calc_move(mag_x, mag_y, d)
            next_x, next_y = self.x + x_offset, self.y + y_offset
            next_heuristic = heuristic(next_x, next_y)
            if next_heuristic + self.dist_traveled < min_cost:
                min_cost = next_heuristic + self.dist_traveled
                opt_dir = d
        return opt_dir

    def auto_move(self, mag_x, mag_y):
        opt_dir = self.next_move(mag_x, mag_y, self.manhattan_heuristic)
        self.move(mag_x, mag_y, opt_dir)
