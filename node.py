"""Needs comments"""
from anytree import NodeMixin


class Node(NodeMixin):
    """Needs comments"""
    # Variables for my Nodes
    state_array = []
    state_string = ''
    path = {}
    depth = 0
    heuristic = 0

    # Constructor
    def __init__(self, state_array, state_string, path, depth=None, heuristic=None, parent=None):
        super(Node, self).__init__()
        self.state_array = state_array
        self.state_string = state_string
        self.path = path
        self.depth = depth
        self.heuristic = heuristic
        self.parent = parent
