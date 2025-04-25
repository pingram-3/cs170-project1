class Node:

    def __init__(self, f, g, grid, parent):
        self.f = f  # g + h
        self.g = g  # distance from starting node
        self.grid = grid  # NxN array
        self.parent = parent

    # overloading comparison operator so that the frontier can sort based on f
    def __lt__(self, other):
        return self.f < other.f
