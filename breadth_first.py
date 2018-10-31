# Jody Bailey
# Intro to AI
# 10/31/2018
# This class is used to perform the breadth first search. It was designed
# to be able to function as a stand-alone class as long as it receives the
# required data to start.

from node import Node
from _collections import deque


class BreadthSearch:
    """Breadth First Search Class"""
    counter = 0
    node = {}
    queue = deque([])
    visited = {}
    path = {}

    # Constructor
    def __init__(self, node):
        self.counter = 0
        self.node = node
        self.visited = {node.state_string: node.state_string}
        self.queue = deque([node])
        self.path = {node: [node.state_string]}

    # Method used to create a node from the Node class.
    def create_node(self, state_array, state_string, depth, heuristic, parent):
        """Needs comments"""
        node = Node(state_array, state_string, depth, heuristic, parent)

        return node

    # Method used to create the array when given the state_string
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

    # Method used to create the state string when you pass it an array.
    @staticmethod
    def create_state_string(array):
        state = ''
        for i in range(3):
            for j in range(3):
                state += str(array[i][j])
        return state

    # Method to determine if the node passed in is the goal state.
    def complete(self, node):
        """Needs comments"""
        # path = ''.join(str(elem) for row in node for elem in row)
        return node.state_string == '123456780'

    # Method to increment the counter
    def count_up(self):
        """needs comments"""
        self.counter += 1

    # Method used to get the state string from an array
    def get_state_string(self, node):
        """Needs comments"""
        return ''.join(str(elem) for row in node for elem in row)

    # Method used to check if a state has already been visited
    def check_visited(self, state):
        """Needs comments"""
        return state in self.visited

    # Method to find the position of 0.
    @staticmethod
    def locate_hole(node):
        """Needs comments"""
        array = node
        for i in range(3):
            for j in range(3):
                if array[i][j] == 0:
                    return i, j

    # Method to check if the new location would be out of bounds.
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

    # Method to swap the 0 and the new location.
    def swap_locations(self, node, location, new_loc):
        """Needs comments"""
        test_node = node
        test_node[location[0]][location[1]], test_node[new_loc[0]][new_loc[1]] = \
            test_node[new_loc[0]][new_loc[1]], test_node[location[0]][location[1]]
        return test_node

    # Method to add the moves found to the queue
    def add_moves_to_queue(self, moves, parent):
        """Needs comments"""
        for move in moves:
            if not self.check_visited(move):
                array = self.create_array(move)
                self.count_up()
                node = self.create_node(array, move, 0, 0, parent)
                try:
                    this_parent = self.node.parent
                    self.path[node] = this_parent.path
                    self.path[node].append(node.state_string)
                    node.path = self.path[node]
                except AttributeError:
                    '''do nothing'''
                self.queue.append(node)
                self.visited.update({move: move})

    # Method to check the current location for children and returns
    # those children to the run() method.
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

    # Method to print an array
    def print_array(self, array):
        """Needs comments"""
        for row in array:
            print(' '.join(str(elem) for elem in row))

    # Main method of this class. It brings together all of the functionality from
    # the other methods and runs the search.
    def run(self):
        """Needs comments"""
        print('Running Breadth First Search...')
        while len(self.queue) > 0:
            self.node = self.queue.popleft()
            if not self.complete(self.node):
                # if self.counter % 10000 == 0:
                #     print('{}'.format(self.counter))
                location = self.locate_hole(self.node.state_array)
                moves = self.check_moves(location)
                self.add_moves_to_queue(moves, self.node)
                if len(self.queue) == 0:
                    print('empty queue')
                    print(self.counter)
                    return
            else:
                self.print_array(self.node.state_array)
                print()

                return
