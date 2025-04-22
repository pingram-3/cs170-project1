class InvalidMoveError(Exception):
    pass

class Problem:
    GOAL_STATE = None

    #grid: list of lists describing current state
    def __init__(self, grid):
        self.state = grid
        if Problem.GOAL_STATE is None:
            Problem.GOAL_STATE = self.generate_goal(len(grid[0]))

    #Generalized function for generating the goal_state
    def generate_goal(self, n):
        goal_state = []
        num = 1
        for i in range(0, n):
            row = []
            for _ in range(0, n if i < n - 1 else n - 1):
                row += [num]
                num += 1
            goal_state += [row]
        goal_state[n - 1].append('*')

        return goal_state

    #Return a copy of state with directional swap applied to state[i][j]
    def apply_swap(self, i, j, dir):
        newi, newj = i + dir[0], j + dir[1]
        is_valid = lambda i, j: True if i >= 0 and i < 3 and j >= 0 and j < 3 else False

        if is_valid(newi, newj):
            copy_state = [row[:] for row in self.state]
            copy_state[i][j], copy_state[newi][newj] = copy_state[newi][
                newj], copy_state[i][j]
            return copy_state

        raise InvalidMoveError(f"Error: [{newi}][{newj}] out of bounds")
    
    def is_goal(self):
        return True if self.state == self.GOAL_STATE else False
