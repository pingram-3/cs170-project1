import heapq
from .heuristics import *
from .helpers import *
from .node import *


def A_star(grid, heuristic):
    # initialize min heap, make the heap sort by (heuristic value) + (distance (number of moves) from starting grid)
    frontier = []
    heapq.heapify(frontier)

    # initialize visited nodes list
    visited = []

    # stores a grid as the key, and its parent as the value
    # so we can find the path in the end
    backtrack = {grid_to_tuple(grid): None}

    # add initial grid to frontier
    heapq.heappush(frontier, (heuristic(grid), 0, grid))

    # counts the number nodes expanded during search
    num_expanded = 0

    goal_state = generate_goal(len(grid))

    while (len(frontier) != 0):
        current = heapq.heappop(frontier)

        if current[2] in visited:
            continue
        visited.append(current[2])
        num_expanded += 1

        # found goal state, so backtrack to find the path and print it out
        if current[2] == goal_state:
            path = [current[2]]
            curr_parent = backtrack[grid_to_tuple(current[2])]
            while curr_parent != None:
                path.append(curr_parent)
                curr_parent = backtrack[grid_to_tuple(curr_parent)]

            path.reverse()
            for grid in path:
                for row in grid:
                    print(row)
                print()

            print(f"Nodes Expanded: {num_expanded}")
            print(f"Number of steps: {len(path)}")

            return

        blank_coords = find_blank(current[2])

        # branch out, checking new possibilities
        for move in Swap:
            try:
                child = (heuristic(current[2]) + current[0], current[0] + 1,
                         apply_swap(current[2], blank_coords[0],
                                    blank_coords[1], move.value))

                if child[2] not in visited:
                    heapq.heappush(frontier, child)
                    backtrack[grid_to_tuple(child[2])] = current[2]

            except:
                pass
