# Jody Bailey
# Intro to AI
# 10/31/2018
# This class is used as the template for creating nodes. The nodes
# created from this class will build a tree if implemented properly.

from anytree import NodeMixin
from _collections import deque


class Node:
    # Variables for my Nodes
    state_array = []
    state_string = ''
    path = deque([])
    depth = 0
    heuristic = 0

    # Constructor
    def __init__(self, state_array, state_string, path=None, depth=None, heuristic=None, parent=None):
        super(Node, self).__init__()
        self.state_array = state_array
        self.state_string = state_string
        # self.traveled_path = path
        self.depth = depth
        self.path = path
        self.heuristic = heuristic
        self.parent = parent

    def __lt__(self, other):
        return self.heuristic < other.heuristic
