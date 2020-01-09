import math

class Agent:
    def __init__(self, start_x, start_y, size, canvas):
        self.x = start_x
        self.y = start_y
        self.size = size
        self.canvas = canvas
        self.obj = canvas.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill = 'blue', outline = 'blue')

    def move(self, mag_x, mag_y, dir):
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
        x_move, y_move = dir_x_y[dir]
        self.canvas.move(self.obj, x_move, y_move)
