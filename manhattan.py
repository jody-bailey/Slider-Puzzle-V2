# Jody Bailey
# Intro to AI
# 10/31/2018
# This class is used to perform the A* Manhattan Distance search. It was designed
# to be able to function as a stand-alone class as long as it receives the
# required data to start.

from interface import Interface
from node import Node
from copy import deepcopy
import heapq


class ManhattanDistance(Interface):

    # Constructor
    def __init__(self, node):
        self.heap = []
        heapq.heappush(self.heap, (node.heuristic, 0, node))
        heapq.heapify(self.heap)
        self.node = node
        self.visited = {node.state_string: node.state_string}
        self.path = {node: [node.state_string]}
        self.counter = 1
        self.starting_state = node.state_string
        self.solution_found = False

    # Method to increment the counter
    def count_up(self):
        self.counter += 1

    # Returns the starting state
    def get_starting_state(self):
        return self.starting_state

    # Returns whether a solution was found or not
    def get_solution_found(self):
        if self.solution_found:
            return 'Yes'
        else:
            return 'No'

    # Returns the path of the current node
    def get_path(self):
        return self.node.path

    # Returns the amount of nodes that have been explored
    def get_node_count(self):
        return len(self.visited)

    # This method is used to test if the numbers are in the right
    # place on the board
    @staticmethod
    def get_goal_position(num):
        if num == 1:
            return 0, 0
        elif num == 2:
            return 0, 1
        elif num == 3:
            return 0, 2
        elif num == 4:
            return 1, 0
        elif num == 5:
            return 1, 1
        elif num == 6:
            return 1, 2
        elif num == 7:
            return 2, 0
        elif num == 8:
            return 2, 1
        elif num == 0:
            return 2, 2

    # This method is used to find the Manhattan Distance for the heuristic
    @staticmethod
    def manhattan_distance(array):
        total = 0
        for i in range(3):
            for j in range(3):
                position = (i, j)
                num = ManhattanDistance.get_goal_position(array[i][j])
                total += abs(num[0] - position[0]) + abs(num[1] - position[1])
        return total

    # Method used to check if a state has already been visited
    def check_visited(self, state):
        return state in self.visited

    def get_depth(self, node):
        total = 0
        while node.parent is not None:
            node = node.parent
            total += 1
        return total

    def get_final_depth(self):
        return self.get_depth(self.node)

    # Method to add the moves found to the queue
    def add_moves_to_heap(self, moves, parent):
        for move in moves:
            if not self.check_visited(move):
                array = self.create_array(move)
                self.count_up()
                # node = self.create_node(array, move, parent=parent)
                heuristic = self.manhattan_distance(array)
                depth = self.get_depth(parent) + 1
                heuristic = heuristic + depth
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
                self.visited.update({move: move})

    # Method to check the current location for children and returns
    # those children to the run() method.
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

    # Method to ger the final path of the goal state.
    def print_final_path(self, node):
        my_list = self.path[node]
        my_array_list = []

        print('Final Path of Search:')

        for elem in my_list:
            my_array_list.append(self.create_array(elem))

        for elem2 in my_array_list:
            for row in elem2:
                print(' '.join(str(elem) for elem in row))
            print()

    # Main method of this class. It brings together all of the functionality from
    # the other methods and runs the search.
    def run(self):
        print('Running A* Manhattan Distance Search...')
        while self.heap:
            next_node = heapq.heappop(self.heap)
            self.node = next_node[2]
            if not self.complete(self.node):
                # if self.counter % 10000 == 0:
                #     print('{}'.format(self.counter))
                location = self.locate_hole(self.node.state_array)
                moves = self.check_moves(location)
                self.add_moves_to_heap(moves, self.node)
                if not self.heap:
                    print('empty queue')
                    print(self.counter)
                    return
            else:
                self.solution_found = True
                print()
                self.print_final_path(self.node)
                print()
                print('Depth of goal state: {}'.format(len(self.path[self.node])))
                print('Total nodes generated: {}'.format(self.counter))
                print()

                return
