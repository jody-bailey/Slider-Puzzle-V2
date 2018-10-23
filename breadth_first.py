"""Module needs comments"""
from _collections import deque
from copy import deepcopy


class BreadthSearch:
    """Needs comments"""
    counter = 0
    state_array = []
    visited = {}
    node = {}
    queue = deque([])

    def __init__(self, node):
        self.counter = 0
        self.state_array = node['state_array']
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

    def get_state_string(self, node):
        """Needs comments"""
        return ''.join(str(elem) for row in node for elem in row)

    def add_to_visited(self, node):
        """Needs comments"""
        self.visited.update({'{}'.format(self.counter): node['state_string']})

    def check_visited(self):
        """Needs comments"""
        self.visited.fromkeys(print(value) for value in self.visited)

    def locate_hole(self):
        """Needs comments"""
        array = self.node['state_array']
        for i in range(3):
            for j in range(3):
                if array[i][j] == 0:
                    return i, j

    def check_bounds(self, location):
        """Needs comments"""
        if location[0] > 2:
            return False
        elif location[0] < 0:
            return False
        elif location[1] > 2:
            return False
        elif location[1] < 0:
            return False
        else:
            return True

    def swap_locations(self, node, location, new_loc):
        test_node = node
        test_node[location[0]][location[1]], test_node[new_loc[0]][new_loc[1]] = \
            test_node[new_loc[0]][new_loc[1]], test_node[location[0]][location[1]]
        return test_node

    def check_moves(self, location):
        possible_moves = []
        # check left
        new_loc = location[0] - 1, location[1]
        if self.check_bounds(new_loc):
            test_node = deepcopy(self.state_array)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        # check right
        new_loc = location[0] + 1, location[1]
        if self.check_bounds(new_loc):
            test_node = deepcopy(self.state_array)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        # check up
        new_loc = location[0], location[1] - 1
        if self.check_bounds(new_loc):
            test_node = deepcopy(self.state_array)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        # check down
        new_loc = location[0], location[1] + 1
        if self.check_bounds(new_loc):
            test_node = deepcopy(self.state_array)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        return possible_moves

    def run(self):
        """Needs comments"""
        while len(self.queue) > 0:
            this_node = self.queue.popleft()
            if not self.complete(this_node['state_array']):
                location = self.locate_hole()
                moves = self.check_moves(location)
                print(moves)
