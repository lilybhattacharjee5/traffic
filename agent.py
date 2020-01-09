import math

class Agent:
    def __init__(self, start_x, start_y, size, canvas):
        self.x = start_x
        self.y = start_y
        self.size = size
        self.canvas = canvas
        self.obj = canvas.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill = 'blue', outline = 'blue')

    def move(self, mag, dir):
        self.canvas.move(self.obj, mag, 0)
