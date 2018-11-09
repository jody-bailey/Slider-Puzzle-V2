# Jody Bailey
# Intro to AI
# 10/31/2018
# This class is used to perform the breadth first search. It was designed
# to be able to function as a stand-alone class as long as it receives the
# required data to start.

from interface import Interface
from node import Node
from _collections import deque
from copy import deepcopy


class BreadthSearch(Interface):
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

    # Method to increment the counter
    def count_up(self):
        """needs comments"""
        self.counter += 1

    # Method used to check if a state has already been visited
    def check_visited(self, state):
        """Needs comments"""
        return state in self.visited

    # Method to add the moves found to the queue
    def add_moves_to_queue(self, moves, parent):
        """Needs comments"""
        for move in moves:
            if not self.check_visited(move):
                array = self.create_array(move)
                self.count_up()
                node = Node(array, move, parent=parent)
                try:
                    this_parent = parent
                    self.path[node] = deepcopy(this_parent.path)
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

    def print_final_path(self, node):
        my_list = self.path[node]
        my_array_list = []

        print('Final Path of Search:')

        for elem in my_list:
            my_array_list.append(self.create_array(elem))

        # print('\n'.join(str(elem) for elem2 in my_array_list for row in elem2 for elem in row), end=' -> ')

        for elem2 in my_array_list:
            for row in elem2:
                print(' '.join(str(elem) for elem in row))
            print()

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
                self.print_final_path(self.node)
                print()
                print(len(self.path[self.node]))

                return
