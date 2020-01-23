simple_dirs = ["left", "right", "up", "down", "stay"]
complex_dirs = ["diag_ru", "diag_rd", "diag_lu", "diag_ld"]
dirs = simple_dirs + complex_dirs

dir_trans = {
    "left": (lambda x: x < 0, lambda y: y == 0),
    "right": (lambda x: x > 0, lambda y: y == 0),
    "up": (lambda x: x == 0, lambda y: y < 0),
    "down": (lambda x: x == 0, lambda y: y > 0),
    "diag_ru": (lambda x: x > 0, lambda y: y < 0),
    "diag_rd": (lambda x: x > 0, lambda y: y > 0),
    "diag_lu": (lambda x: x < 0, lambda y: y < 0),
    "diag_ld": (lambda x: x < 0, lambda y: y > 0),
    "stay": (lambda x: x == 0, lambda y: y == 0),
}

def distance_formula(x1, y1, x2, y2):
    x_exp = (x2 - x1)**2
    y_exp = (y2 - y1)**2
    return (x_exp + y_exp)**0.5

def infer_dir(x1, y1, x2, y2):
    x_trans = x2 - x1
    y_trans = y2 - y1
    for d, d_func in dir_trans.items():
        x_func, y_func = d_func
        if x_func(x_trans) and y_func(y_trans):
            return d
    return Error("direction could not be found")

def possible_coords(min_coord, max_coord, cell_width):
    all_coords = list(range(min_coord, max_coord, cell_width))
    return all_coords

def random_possible_coord(all_coords):
    return random.choice(all_coords)

def valid_move(city, curr_x, curr_y, x, y):
    return city.cell_type(x, y) in ["e", "d"] or (curr_x == x and curr_y == y)
