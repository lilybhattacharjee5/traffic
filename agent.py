import math
import random
from heapq import *
from utils import *
from display_utils import *

class Agent:
    def __init__(self, window, canvas, city, start_x, start_y, dest_x, dest_y, size, city_width, city_height, color):
        self.canvas = canvas
        self.city = city
        self.x = start_x
        self.y = start_y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.size = size
        self.dist_traveled = 0
        self.heuristic_val = math.inf
        self.agent_obj = canvas.create_rectangle(start_x, start_y, start_x + size, start_y + size, fill = color, outline = color)

        pos = window.nametowidget("pos")
        score = window.nametowidget("score")
        self.canvas.tag_bind(self.agent_obj, '<Enter>', configAddHeaderText(self, pos, score))
        self.canvas.tag_bind(self.agent_obj, '<Leave>', configRemoveHeaderText(pos, score))

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
            "stay": (0, 0),
        }
        return dir_x_y[direction]

    def move(self, mag_x, mag_y, direction):
        x_move, y_move = self.calc_move(mag_x, mag_y, direction)
        if direction in simple_dirs:
            self.dist_traveled += abs(x_move) + abs(y_move)
        else:
            self.dist_traveled += distance_formula(self.x, self.y, self.x + x_move, self.y + y_move)
        self.x += x_move
        self.y += y_move
        self.canvas.move(self.agent_obj, x_move, y_move)

    def manhattan_heuristic(self, x, y):
        x_remain = abs(self.dest_x - x)
        y_remain = abs(self.dest_y - y)
        return x_remain + y_remain

    def distance_heuristic(self, x, y):
        return distance_formula(x, y, self.dest_x, self.dest_y)

    def find_child_states(self, curr_x, curr_y, mag_x, mag_y):
        child_states = []
        for d in dirs:
            x_offset, y_offset = self.calc_move(mag_x, mag_y, d)
            next_x, next_y = curr_x + x_offset, curr_y + y_offset
            if self.city.cell_type(next_x, next_y) != "o":
                child_states.append((next_x, next_y))
        return child_states

    def greedy_next_move(self, mag_x, mag_y, heuristic):
        min_cost = math.inf
        opt_dir = "right"
        for d in dirs:
            x_offset, y_offset = self.calc_move(mag_x, mag_y, d)
            next_x, next_y = self.x + x_offset, self.y + y_offset
            next_heuristic = heuristic(next_x, next_y)
            if next_heuristic + self.dist_traveled < min_cost:
                min_cost = next_heuristic + self.dist_traveled
                opt_dir = d
                self.heuristic_val = min_cost
        return opt_dir

    def astar_next_move(self, mag_x, mag_y, heuristic):
        curr_pos = (self.x, self.y)
        if curr_pos in self.astar_path_map:
            next_dir = self.astar_path_map[curr_pos]
            next_x, next_y = self.calc_move(mag_x, mag_y, next_dir)
            self.heuristic_val = heuristic(next_x, next_y)
            return next_dir
        else:
            return "stay"

    def reconstruct_path(self, path_tracker, end_state):
        path_map = {}
        curr_state = end_state
        while path_tracker[curr_state] != None:
            parent = path_tracker[curr_state]
            path_map[parent] = infer_dir(parent[0], parent[1], curr_state[0], curr_state[1])
            curr_state = parent
        return path_map

    def astar_search(self, mag_x, mag_y, heuristic):
        state_queue = [[math.inf, (self.x, self.y)]]
        path_tracker = {(self.x, self.y): None}
        goal_state = (self.dest_x, self.dest_y)

        gscore = {}
        for i in range(0, self.city.width + self.size, self.size):
            for j in range(0, self.city.height + self.size, self.size):
                gscore[(i, j)] = math.inf
        gscore[(self.x, self.y)] = 0

        heapify(state_queue)

        while state_queue != []:
            heapify(state_queue)
            curr_priority, curr_state = heappop(state_queue)
            curr_x, curr_y = curr_state
            if curr_state == goal_state:
                self.astar_path_map = self.reconstruct_path(path_tracker, curr_state)
                return
            next_children = self.find_child_states(curr_x, curr_y, mag_x, mag_y)
            for c in next_children:
                next_x, next_y = c
                tentative_gscore = gscore[curr_state] + distance_formula(curr_x, curr_y, next_x, next_y)
                curr_gscore = math.inf
                if c in gscore:
                    curr_gscore = gscore[c]
                if tentative_gscore < curr_gscore:
                    path_tracker[c] = curr_state
                    gscore[c] = tentative_gscore
                    new_priority = gscore[c] + heuristic(next_x, next_y)
                    replaced = False
                    for s in state_queue:
                        if s[1] == c:
                            s[0] = new_priority
                            replaced = True
                    if not replaced:
                        heappush(state_queue, [new_priority, c])
        self.astar_path_map = []

    def auto_move(self, mag_x, mag_y):
        # opt_dir = self.greedy_next_move(mag_x, mag_y, self.distance_heuristic)
        self.astar_search(self.size, self.size, self.manhattan_heuristic)
        opt_dir = self.astar_next_move(mag_x, mag_y, self.manhattan_heuristic)
        self.move(mag_x, mag_y, opt_dir)
