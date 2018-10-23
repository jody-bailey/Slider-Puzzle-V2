"""Module needs comments"""
from _collections import deque

class BreadthSearch:
    """Needs comments"""
    counter = 0
    visited = {}
    node = {}
    queue = deque([])

    def __init__(self, node):
        self.counter = 0
        self.visited = {'{}'.format(self.counter): node['state_string']}
        self.node = node
        self.queue = deque([node])

    def complete(self, node):
        """Needs comments"""
        path = ''.join(str(elem) for row in node for elem in row)
        if path == '123456780':
            print(path)
            return True
        else:
            print(path)
            return False

    def count_up(self):
        """needs comments"""
        self.counter += 1

    def set_state_string(self):
        """Needs comments"""
        self.node['state_string'] = ''.join(str(elem) for row in self.node for elem in row)

    def add_to_visited(self, node):
        """Needs comments"""
        self.visited.update({'{}'.format(self.counter): node['state_string']})

    def check_visited(self):
        """Needs comments"""
        self.visited.fromkeys(print(value) for value in self.visited)

    def locate_hole(self):
        """Needs comments"""
        for i in range(3):
            for j in range(3):
                if self.node[i][j] == '0':
                    return i, j

    def check_bounds(self, location):
        """Needs comments"""
        if location[0] > 2:
            return False
        if location[0] < 0:
            return False
        if location[1] > 2:
            return False
        if location[1] < 0:
            return False

    def check_moves(self, location):
        # check left
        location = location[0] - 1, location[1]

    def run(self):
        """Needs comments"""
        while len(self.queue) > 0:
            if not self.complete(self.queue.popleft()):
                location = self.locate_hole()


