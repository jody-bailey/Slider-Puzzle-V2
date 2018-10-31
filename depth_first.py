"""Module needs comments"""
from node import Node


class DepthSearch:
    """Needs comments"""
    counter = 0
    node = {}
    stack = []
    visited = {}
    path = {}

    def __init__(self, node):
        self.counter = 0
        self.node = node
        self.visited = {node.state_string: node.state_string}
        self.stack = [node]
        self.path = {node: [node.state_string]}

    def create_node(self, state_array, state_string, depth, heuristic, parent):
        """Needs comments"""
        node = Node(state_array, state_string, depth, heuristic, parent)

        return node

    @staticmethod
    def create_array(state_string):
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

    @staticmethod
    def create_state_string(array):
        state = ''
        for i in range(3):
            for j in range(3):
                state += str(array[i][j])
        return state

    def complete(self, node):
        """Needs comments"""
        # path = ''.join(str(elem) for row in node for elem in row)
        return node.state_string == '123456780'

    def count_up(self):
        """needs comments"""
        self.counter += 1

    def set_state_string(self):
        """Needs comments"""
        self.node['state_string'] = ''.join(str(elem) for row in self.node for elem in row)

    def get_state_string(self, node):
        """Needs comments"""
        return ''.join(str(elem) for row in node for elem in row)

    def check_visited(self, state):
        """Needs comments"""
        return state in self.visited

    @staticmethod
    def locate_hole(node):
        """Needs comments"""
        array = node
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
        test_node = node
        test_node[location[0]][location[1]], test_node[new_loc[0]][new_loc[1]] = \
            test_node[new_loc[0]][new_loc[1]], test_node[location[0]][location[1]]
        return test_node

    def add_moves_to_stack(self, moves, parent):
        """Needs comments"""
        for move in moves:
            if not self.check_visited(move):
                array = self.create_array(move)
                self.count_up()
                # self.node.traveled_path.update({self.counter + 1: move})
                # path = self.node.traveled_path
                node = self.create_node(array, move, 0, 0, parent)
                try:
                    this_parent = self.node.parent
                    self.path[node] = this_parent.path
                    self.path[node].append(node.state_string)
                except AttributeError:
                    '''do nothing'''
                self.stack.append(node)
                self.visited.update({move: move})
            # if move not in self.visited:

    def make_move(self, node):
        """Needs comments"""
        self.count_up()
        self.node = self.stack.pop()

    def check_moves(self, location):
        """Needs comments"""
        possible_moves = []

        # check left
        new_loc = location[0], location[1] - 1
        if self.check_bounds(new_loc):
            test_node = self.create_array(self.node.state_string)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        # check down
        new_loc = location[0] + 1, location[1]
        if self.check_bounds(new_loc):
            test_node = self.create_array(self.node.state_string)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        # check right
        new_loc = location[0], location[1] + 1
        if self.check_bounds(new_loc):
            test_node = self.create_array(self.node.state_string)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        # check up
        new_loc = location[0] - 1, location[1]
        if self.check_bounds(new_loc):
            test_node = self.create_array(self.node.state_string)
            test_node = self.swap_locations(test_node, location, new_loc)
            possible_moves.append(self.get_state_string(test_node))

        return possible_moves

    def print_array(self, array):
        """Needs comments"""
        for row in array:
            print(' '.join(str(elem) for elem in row))

    def get_path(self, node):
        path = []
        while node:
            path.append(node.state_string)
            node = node.parent
        return path

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
        print('Running Depth First Search...')
        while len(self.stack) > 0:
            self.node = self.stack.pop()
            if not self.complete(self.node):
                if self.counter % 1000 == 0:
                    print('{}'.format(self.counter))
                location = self.locate_hole(self.node.state_array)
                moves = self.check_moves(location)
                self.add_moves_to_stack(moves, self.node)
                if len(self.stack) == 0:
                    print('empty stack')
                    print(self.counter)
                    return
            else:
                self.print_array(self.node.state_array)
                print()
                print(self.counter)
                print()
                final_path = self.get_path(self.node)
                final_path.reverse()
                print(' '.join(str(elem) for elem in final_path))
                print(len(final_path))
                print(' '.join(str(elem) for elem in self.path[self.node.parent]))
                # for node in self.node.path:
                #     final_path.append(node.state_string)
                # print(final_path)
                return

        my_array = self.node.state_array
        print(''.join(str(elem) for row in my_array for elem in row))