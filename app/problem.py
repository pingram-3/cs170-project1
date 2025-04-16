class Problem:

    #Constant goal state
    GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, '*'))

    #grid: list of lists describing current state
    def __init__(self, grid):
        self.initial_state = grid

    #Return a copy of initial_state with directional swap applied to initial_state[i][j]
    def apply_swap(self, i, j, dir):
        newi, newj = i + dir[0], j + dir[1]
        is_valid = lambda i, j: True if i >= 0 and i < 3 and j >= 0 and j < 3 else False

        if is_valid(newi, newj):
            copy_state = [row[:] for row in self.initial_state]
            copy_state[i][j], copy_state[newi][newj] = copy_state[newi][
                newj], copy_state[i][j]
            return copy_state
