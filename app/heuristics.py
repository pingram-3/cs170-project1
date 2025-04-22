import math


# algorithm: compare the grid with the goal state, and count the number of tiles in the wrong place
def heuristic_misplaced_tile(grid):
    GOAL_STATE = [[1, 2, 3], [4, 5, 6], [
        7, 8, 0
    ]]  # hardcoding this until a general goal state function is made
    sum = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            curr_num = grid[r][c]
            if GOAL_STATE[r][c] != curr_num and curr_num > 0:
                sum += 1
    return sum


# algorithm: Compare the grid with the goal state. For each element in the wrong place, find its x and y offset, and add them to an overall sum.
def heuristic_euclidean_distance(grid):
    GOAL_STATE = [[1, 2, 3], [4, 5, 6], [
        7, 8, 0
    ]]  # hardcoding this until a general goal state function is made
    sum = 0
    n = len(grid)
    for r in range(n):
        for c in range(n):
            curr_num = grid[r][c]
            if GOAL_STATE[r][c] != curr_num and curr_num > 0:
                # These two goal offsets give the distance from where the current number currently is, and where it should be. I don't have a source for these because I just made them up.
                goal_offset_r = abs(math.ceil(curr_num / n - 1) - r)
                goal_offset_c = abs((curr_num - 1) % n - c)
                sum += goal_offset_c + goal_offset_r
    return sum
