from enum import Enum
from queue import PriorityQueue
from .problem import *


#For applying moves to the problem class
class Swap(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


# usage notes:
#
# node = [  [1 2 3],
#           [4,5,6],
#           [7,8,9] ]
#
# tree = Tree(node)


class Node:

    def __init__(self, problem, parent=None, cost=0):
        self.problem = problem  # state will be a NxN grid
        self.parent = parent  # store where we came from
        self.cost = cost  # cost it takes to get to the current node
        self.children = [
        ]  # store what problem states we can visit from current problem state

    # appends a child
    def append_child(self, new_node):
        new_node.parent = self
        new_node.cost = self.cost + 1
        self.children.append(new_node)

    # backtracks to find path it took to get to current node
    def get_path(self):
        path = []
        current = self
        while current.parent is not None:
            path.append(current.state)
            current = current.parent
        return path[::-1]  # From root to current node

    def expand(self):
        for move in Swap:
            new_state = Problem.apply_swap(self.problem, move)
            child = Node(Problem(new_state))
            self.append_child(child)


class Tree:

    def __init__(self, initial_state):
        self.root = Node(initial_state)

    def a_star(self, heuristic):
        frontier = PriorityQueue()
        explored = set()
        frontier.put((0, self.root))

        while not frontier.empty():
            current_state = frontier.get()[1]
