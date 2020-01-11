def config_grid(canvas, w, h, cell_width, event = None):
    def show_grid(event):
        canvas.delete('grid_line') # will only remove the grid lines

        # Creates all vertical lines at intervals of cell_width
        for i in range(0, w, cell_width):
            canvas.create_line([(i, 0), (i, h)], tag = 'grid_line', fill = 'black')

        # Creates all horizontal lines at intervals of cell_width
        for i in range(0, h, cell_width):
            canvas.create_line([(0, i), (w, i)], tag = 'grid_line', fill = 'black')
    return show_grid

def config_move_agents(canvas, agents, cell_width):
    def move_agents():
        for agent in agents:
            if agent.x != agent.dest_x or agent.y != agent.dest_y:
                agent.auto_move(mag_x = cell_width, mag_y = cell_width)

                # pos.delete(1.0, tk.INSERT)
                # pos.insert(tk.INSERT, "Position: (%d, %d)" % (agent.x, agent.y))
                #
                # score.delete(1.0, tk.INSERT)
                #
                # if type(agent.heuristic_val) == int:
                #     score_display = "Score: %d" % agent.heuristic_val
                # elif type(agent.heuristic_val) == float:
                #     score_display = "Score: %.02f" % agent.heuristic_val
                # else:
                #     score.insert(tk.INSERT, "Score: ?")
                # score.insert(tk.INSERT, score_display)

                canvas.after(1000, move_agents)
    move_agents()
