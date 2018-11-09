# Jody Bailey
# Intro to AI
# 10/31/2018
# This class is used to perform the A* Misplaced Tiles search. It was designed
# to be able to function as a stand-alone class as long as it receives the
# required data to start.

import heapq
from interface import Interface
from node import Node
from copy import deepcopy


class MisplacedTiles(Interface):

    def __init__(self, node):
        self.heap = []
        heapq.heappush(self.heap, (node.heuristic, 0, node))
        self.node = node
        self.visited = {node.state_string: node.state_string}
        self.path = {node: [node.state_string]}
        self.counter = 0

    # Method to increment the counter
    def count_up(self):
        """needs comments"""
        self.counter += 1

    @staticmethod
    def out_of_place_tiles(array):
        total = 0
        for i in range(3):
            for j in range(3):
                position = (i, j)
                if position == (0, 0):
                    if array[i][j] != 1:
                        total += 1
                elif position == (0, 1):
                    if array[i][j] != 2:
                        total += 1
                elif position == (0, 2):
                    if array[i][j] != 3:
                        total += 1
                elif position == (1, 0):
                    if array[i][j] != 4:
                        total += 1
                elif position == (1, 1):
                    if array[i][j] != 5:
                        total += 1
                elif position == (1, 2):
                    if array[i][j] != 6:
                        total += 1
                elif position == (2, 0):
                    if array[i][j] != 7:
                        total += 1
                elif position == (2, 1):
                    if array[i][j] != 8:
                        total += 1
                elif position == (2, 2):
                    if array[i][j] != 0:
                        total += 1
        return total

    # Method used to check if a state has already been visited
    def check_visited(self, state):
        """Needs comments"""
        return state in self.visited

    def get_depth(self, node):
        total = 0
        while node.parent is not None:
            node = node.parent
            total += 1
        return total

    # Method to add the moves found to the queue
    def add_moves_to_heap(self, moves, parent):
        """Needs comments"""
        for move in moves:
            if not self.check_visited(move):
                array = self.create_array(move)
                self.count_up()
                # node = self.create_node(array, move, parent=parent)
                heuristic = self.out_of_place_tiles(array)
                depth = self.get_depth(self.node)
                heuristic = heuristic * depth - 1
                node = Node(array, move, heuristic=heuristic, parent=parent)
                try:
                    this_parent = parent
                    self.path[node] = deepcopy(this_parent.path)
                    self.path[node].append(node.state_string)
                    node.path = self.path[node]
                    # node.heuristic = self.out_of_place_tiles(node.state_array)
                except AttributeError:
                    '''do nothing'''
                # self.heap.put((node.heuristic, node))
                heapq.heappush(self.heap, (heuristic, self.counter, node))
                heapq.heapify(self.heap)
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

    # Main method of this class. It brings together all of the functionality from
    # the other methods and runs the search.
    def run(self):
        """Needs comments"""
        print('Running A* Misplaced Tiles Search...')
        while len(self.heap) > 0:
            next_node = heapq.heappop(self.heap)
            self.node = next_node[2]
            if not self.complete(self.node):
                # if self.counter % 10000 == 0:
                #     print('{}'.format(self.counter))
                location = self.locate_hole(self.node.state_array)
                moves = self.check_moves(location)
                self.add_moves_to_heap(moves, self.node)
                if len(self.heap) == 0:
                    print('empty queue')
                    print(self.counter)
                    return
            else:
                self.print_array(self.node.state_array)
                print()
                print(' -> '.join(str(elem) for elem in self.path[self.node]))
                print()
                print(len(self.path[self.node]))

                return
