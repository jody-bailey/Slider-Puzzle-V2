# Jody Bailey
# Intro to AI
# 10/31/2018
# This class is used to perform the depth first search.

from node import Node
from _collections import deque


class DepthSearch:
    counter = 0
    node = {}
    stack = deque([])
    visited = {}
    path = {}

    # Constructor
    def __init__(self, node):
        self.counter = 0
        self.node = node
        self.visited = {node.state_string: node.state_string}
        self.stack = deque([node])
        self.path = {node: deque([node.state_string])}

    # Method used to create a node from the Node class.
    def create_node(self, state_array, state_string, path, depth, heuristic, parent):
        node = Node(state_array, state_string, path, depth, heuristic, parent)

        return node

    # Method sued to create an array when it is passed a state string.
    @staticmethod
    def create_array(state_string):
        array = [0] * 3
        for i in range(3):
            array[i] = [0] * 3

        index = 0
        for i in range(3):
            for j in range(3):
                array[i][j] = int(state_string[index])
                index += 1

        return array

    # Method used to determine if a node is the goal state.
    def complete(self, node):
        # path = ''.join(str(elem) for row in node for elem in row)
        return node.state_string == '123456780'

    # Method to increment the counter
    def count_up(self):
        self.counter += 1

    # Method to get the state string by iterating through the array.
    def get_state_string(self, node):
        return ''.join(str(elem) for row in node for elem in row)

    # Method to check if the node in question has been visited.
    def check_visited(self, state):
        return state in self.visited

    # Method to check for the location of the 0 position
    @staticmethod
    def locate_hole(node):
        array = node
        for i in range(3):
            for j in range(3):
                if array[i][j] == 0:
                    return i, j

    # Method to check if the new location would be in bounds.
    def check_bounds(self, location):
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

    # Method used to swap the location of the 0 and the new location
    def swap_locations(self, node, location, new_loc):
        test_node = node
        test_node[location[0]][location[1]], test_node[new_loc[0]][new_loc[1]] = \
            test_node[new_loc[0]][new_loc[1]], test_node[location[0]][location[1]]
        return test_node

    # Method to add children to the stack
    def add_moves_to_stack(self, moves, parent):
        for move in moves:
            if not self.check_visited(move):
                array = self.create_array(move)
                self.count_up()
                # self.node.traveled_path.update({self.counter + 1: move})
                # path = self.node.traveled_path
                node = self.create_node(array, move, [], 0, 0, parent)
                try:
                    this_parent = self.node.parent
                    self.path[node] = this_parent.path
                    self.path[node].append(node.state_string)
                    node.path = self.path[node]
                except AttributeError:
                    '''do nothing'''
                self.stack.append(node)
                self.visited.update({move: move})

    # Method used to get all of the children of the current node.
    # It then returns those children back to the run() method.
    def check_moves(self, location):
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

    # Method used to print an array
    def print_array(self, array):
        for row in array:
            print(' '.join(str(elem) for elem in row))

    # Main method of the class. It brings together all of the functionality
    # from the other methods to perfom the search.
    def run(self):
        print('Running Depth First Search...')
        while len(self.stack) > 0:
            self.node = self.stack.pop()
            if not self.complete(self.node):
                # if self.counter % 1000 == 0:
                #     print('{}'.format(self.counter))
                location = self.locate_hole(self.node.state_array)
                moves = self.check_moves(location)
                for move in moves:
                    if not self.check_visited(move):
                        node = Node(self.create_array(move), move, None)

                        self.stack.append(node)
                        try:
                            self.path[node].append(node.state_string)
                        except KeyError:
                            self.path[node] = deque([node.state_string])
                        self.visited.update({move: move})
                        self.count_up()
                if len(self.stack) == 0:
                    print('empty stack')
                    print(self.counter)
                    return
            else:
                self.print_array(self.node.state_array)
                print()

                return
