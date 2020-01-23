# add random block comment

class Block:
    def __init__(self, canvas, value, x, y, size, color):
        self.value = value
        self.x = x
        self.y = y
        self.dest_obj = canvas.create_rectangle(self.x, self.y, x + size, y + size, fill = color, outline = color)
