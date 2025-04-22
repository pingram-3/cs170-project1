import heapq
from .problem import *
from .tree import *
from .heuristics import *

# returns the index of the blank space
def find_blank(grid):
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 0:
                return (r, c)
    raise InvalidMoveError("Cannot find blank space")

#Return a copy of state with directional swap applied to state[i][j]
def apply_swap(grid, i, j, dir):
    newi, newj = i + dir[0], j + dir[1]
    is_valid = lambda i, j: True if i >= 0 and i < 3 and j >= 0 and j < 3 else False
    if is_valid(newi, newj):
        copy_state = [row[:] for row in grid]
        copy_state[i][j], copy_state[newi][newj] = copy_state[newi][
            newj], copy_state[i][j]
        return copy_state
    raise InvalidMoveError(f"Error: [{newi}][{newj}] out of bounds")

def is_goal(grid):
        return True if grid == generate_goal(len(grid[0])) else False

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


def A_star(grid, heuristic):
    # initialize min heap, make the heap sort by (heuristic value) + (distance (number of moves) from starting grid)
    frontier = []
    heapq.heapify(frontier)

    # initialize visited nodes list
    visited = []

    # add initial grid to frontier
    heapq.heappush(frontier, (heuristic(grid), 0, grid))

    while (len(frontier) != 0):
        # current = pop node off heap
        current = heapq.heappop(frontier)

        # TODO REMOVE THIS
        for row in current[2]:
            print(row)
        print()

        if is_goal(current[2]):
            # now that we found the goal state, we just backtrack to find the path from start to finish
            print("Goal Found")
            for row in current:
                print(row)
            return

        # generate four new grids based on current node (in the same way as earlier)
        blank_coords = find_blank(current[2])
        
        for move in Swap:
            try:
                # if a new grid already exists in the graph (check the heap or something), just update the distance. otherwise, store it in the heap if it is not in the visited list
                child =  (heuristic(current[2]) + current[0], 
                        current[0] + 1, 
                        apply_swap(current[2], blank_coords[0], blank_coords[1], move.value))

                # TODO update tentative distances to children
                for i in range(len(frontier)):
                    if frontier[i][2] == child[2]:
                        if frontier[i][1] > child[1]:
                            frontier[i][0], frontier[i][1] = child[0], child[1]

                if child[2] not in visited:
                    heapq.heappush(frontier, child)
                # add current node to visited list
                visited.append(current[2])
            except:
                pass
        
        # if the goal state enters the visited list, break out of the while loop
        # if is_goal(current[2]):
        #     # now that we found the goal state, we just backtrack to find the path from start to finish
        #     print("Goal Found")
        #     for row in current:
        #         print(row)
        #     return
             

