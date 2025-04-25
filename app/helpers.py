from enum import Enum


class InvalidMoveError(Exception):
    pass


class Swap(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


# returns the index of the blank space
def find_blank(grid):
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 0:
                return (r, c)
    raise InvalidMoveError("Cannot find blank space")


# Return a copy of state with directional swap applied to state[i][j]
def apply_swap(grid, i, j, dir):
    n = len(grid)
    newi, newj = i + dir[0], j + dir[1]
    is_valid = lambda i, j: True if i >= 0 and i < n and j >= 0 and j < n else False
    if is_valid(newi, newj):
        copy_state = [row[:] for row in grid]
        copy_state[i][j], copy_state[newi][newj] = copy_state[newi][
            newj], copy_state[i][j]
        return copy_state
    raise InvalidMoveError(f"Error: [{newi}][{newj}] out of bounds")

# generates the goal state of the puzzle grid
def generate_goal(n):
    goal_state = []
    num = 1
    for i in range(0, n):
        row = []
        for _ in range(0, n if i < n - 1 else n - 1):
            row += [num]
            num += 1
        goal_state += [row]
    goal_state[n - 1].append(0)

    return goal_state


# converts grid to tuple because disctionaries can't hash lists
def grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)
