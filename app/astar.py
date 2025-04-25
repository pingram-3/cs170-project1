import heapq
from .heuristics import *
from .helpers import *
from .node import *


def A_star(grid, heuristic):
    # frontier list is a min heap
    frontier = []

    # initialize visited nodes list
    visited = set()

    # add initial grid to frontier
    initial_state = Node(heuristic(grid), 0, grid, None)
    heapq.heappush(frontier, initial_state)

    # counts the number nodes expanded during search
    num_expanded = 0

    goal_state = generate_goal(len(grid))

    max_frontier_size = 0

    while frontier:
        max_frontier_size = max(len(frontier), max_frontier_size)
        current = heapq.heappop(frontier)
        current_grid_tuple = grid_to_tuple(
            current.grid)  # converted to tuple so we can hash it

        if current_grid_tuple in visited:
            continue
        visited.add(current_grid_tuple)
        num_expanded += 1

        # trace algorithm running
        print(
            f"The best state to expand with g(n) = {current.g} and h(n) = {heuristic(current.grid)} is..."
        )
        for row in current.grid:
            print(row)
        print("Expanding this node...\n")

        # found goal state, so backtrack to find the path and print it out
        if current.grid == goal_state:
            path = []
            curr_parent = current
            # backtracking
            while curr_parent is not None:
                path.append(curr_parent.grid)
                curr_parent = curr_parent.parent
            path.reverse()
            # printing path
            print("The optimal path is: ")
            for grid in path:
                for row in grid:
                    print(row)
                print()
            print(f"Nodes Expanded: {num_expanded}")
            print(f"Number of steps in optimal solution: {len(path) - 1}")
            print(f"Max frontier size: {max_frontier_size}")
            return

        # finds the coordinates of the empty space in the tiles
        blank_coords = find_blank(current.grid)

        # branch out, checking new possibilities
        for move in Swap:
            try:
                new_grid = apply_swap(current.grid, blank_coords[0],
                                      blank_coords[1], move.value)

                if grid_to_tuple(new_grid) not in visited:
                    g = current.g + 1
                    f = heuristic(new_grid) + g
                    child = Node(f, g, new_grid, current)
                    heapq.heappush(frontier, child)
            except:
                pass
