"""Module needs comments"""
from copy import deepcopy
from node import Node
from _collections import deque


class BreadthSearch:
    """Needs comments"""
    counter = 0
    state_array = []
    path = {}
    node = {}
    queue = deque([])
    visited = []

    def __init__(self, node):
        self.counter = 0
        self.state_array = node.state_array
        self.path = node.path
        self.node = node
        self.visited = [node.state_string]
        self.queue = deque([node])

    def create_note(self, state_array, state_string, path):
        """Needs comments"""
        node = Node(state_array, state_string, path)

        return node

    def create_array(self, state_string):
        """Needs comments"""
        array = [0] * 3
        for i in range(3):
            array[i] = [0] * 3

        index = 0
        for i in range(3):
            for j in range(3):
                array[i][j] = int(state_string[index])
                index += 1

        return array

    def complete(self, node):
        """Needs comments"""
        path = ''.join(str(elem) for row in node for elem in row)
        if path == '123456780':
            # print(path)
            return True
        else:
            # print(path)
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
        self.path.update({'{}'.format(self.counter): node.state_string})

    def check_visited(self):
        """Needs comments"""
        self.path.fromkeys(print(value) for value in self.path)

    def locate_hole(self, node):
        """Needs comments"""
        array = node.state_array
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
        """Needs comments"""
        test_node = deepcopy(node)
        if self.check_positions(node, new_loc):
            test_node[location[0]][location[1]], test_node[new_loc[0]][new_loc[1]] = \
                test_node[new_loc[0]][new_loc[1]], test_node[location[0]][location[1]]
        return test_node

    def add_moves_to_queue(self, moves):
        """Needs comments"""
        for move in moves:
            if move not in self.visited:
                array = self.create_array(move)
                node = self.create_note(array, move, self.path)
                if node not in self.queue:
                    self.queue.append(node)
                if move not in self.visited:
                    self.visited.append(move)

    def make_move(self, node):
        """Needs comments"""
        self.count_up()
        self.node = deepcopy(node)
        self.path.update({'{}'.format(self.counter): self.get_state_string(node.state_array)})
        self.state_array = self.node.state_array

    def check_moves(self, location):
        """Needs comments"""
        possible_moves = []

        # check left
        new_loc = location[0], location[1] - 1
        if self.check_bounds(new_loc):
            test_node = deepcopy(self.state_array)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        # check down
        new_loc = location[0] + 1, location[1]
        if self.check_bounds(new_loc):
            test_node = deepcopy(self.state_array)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        # check right
        new_loc = location[0], location[1] + 1
        if self.check_bounds(new_loc):
            test_node = deepcopy(self.state_array)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        # check up
        new_loc = location[0] - 1, location[1]
        if self.check_bounds(new_loc):
            test_node = deepcopy(self.state_array)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        return possible_moves

    def print_array(self, array):
        """Needs comments"""
        for row in array:
            print(' '.join(str(elem) for elem in row))

    def check_positions(self, node, location):
        """Needs comments"""
        array = node

        if location == (0, 0) and array[location[0]][location[1]] == 1:
            return False
        elif location == (0, 1) and array[location[0]][location[1]] == 2:
            return False
        elif location == (0, 2) and array[location[0]][location[1]] == 3:
            return False
        elif location == (1, 0) and array[location[0]][location[1]] == 4:
            return False
        elif location == (1, 1) and array[location[0]][location[1]] == 5:
            return False
        elif location == (1, 2) and array[location[0]][location[1]] == 6:
            return False
        elif location == (2, 0) and array[location[0]][location[1]] == 7:
            return False
        elif location == (2, 1) and array[location[0]][location[1]] == 8:
            return False
        else:
            return True

    def run(self):
        """Needs comments"""
        print('Running Breadth First Search...')
        while len(self.queue) > 0:
            this_node = self.queue.popleft()
            if not self.complete(this_node.state_array):
                location = self.locate_hole(this_node)
                moves = self.check_moves(location)
                self.add_moves_to_queue(moves)
                try:
                    self.make_move(self.queue[0])
                    temp = self.queue[0]
                    array = temp.state_array
                    self.print_array(array)
                    print()
                except IndexError:
                    continue
                # print(moves)
            else:
                return

        my_array = self.node['state_array']
        print(''.join(str(elem) for row in my_array for elem in row))
