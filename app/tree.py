# usage notes:
# 
# node = [  [1 2 3],
#           [4,5,6],
#           [7,8,9] ]
# 
# tree = Tree(node)


class Node:
    def __init__(self, state, cost):
        self.state = state # state will be a NxN grid
        self.children = [] # I'm assuming we are not using a binary tree, so we can have unlimited children
        self.parent = None
        self.cost = cost # cost it takes to get to the current node

    # appends a child
    def append_child(self, new_node):
        new_node.parent = self
        self.children.append(new_node)

    # backtracks to find path it took to get to current node
    def get_path(self):
        path = []
        current = self
        while current.parent is not None:
            path.append(current.state)
            current = current.parent
        return path[::-1]  # From root to current node

class Tree:
    def __init__(self, initial_state):
        self.root = Node(initial_state)
