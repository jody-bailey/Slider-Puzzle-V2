"""Module needs comments"""
from node import Node
from _collections import deque


class BreadthSearch:
    """Needs comments"""
    counter = 0
    node = {}
    queue = deque([])
    visited = {}

    def __init__(self, node):
        self.counter = 0
        self.node = node
        self.visited = {node.state_string: node.state_string}
        self.queue = deque([node])

    def create_note(self, state_array, state_string, path):
        """Needs comments"""
        node = Node(state_array, state_string, path)

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

    def add_to_visited(self, node):
        """Needs comments"""
        self.path.update({'{}'.format(self.counter): node.state_string})

    def check_visited(self, state):
        """Needs comments"""
        return state in self.visited

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
        test_node = node
        test_node[location[0]][location[1]], test_node[new_loc[0]][new_loc[1]] = \
            test_node[new_loc[0]][new_loc[1]], test_node[location[0]][location[1]]
        return test_node

    def swap_0_and_1(self):
        """Needs comments"""
        self.node.state_array[0][0], self.node.state_array[0][1] = \
            self.node.state_array[0][1], self.node.state_array[0][0]

    def swap_0_and_3(self):
        """Needs comments"""
        self.node.state_array[0][0], self.node.state_array[1][0] = \
            self.node.state_array[1][0], self.node.state_array[0][0]

    def swap_1_and_2(self):
        """Needs comments"""
        self.node.state_array[0][1], self.node.state_array[0][2] = \
            self.node.state_array[0][2], self.node.state_array[0][1]

    def swap_1_and_4(self):
        """Needs comments"""
        self.node.state_array[0][1], self.node.state_array[1][1] = \
            self.node.state_array[1][1], self.node.state_array[0][1]

    def swap_2_and_5(self):
        """Needs comments"""
        self.node.state_array[0][2], self.node.state_array[1][2] = \
            self.node.state_array[1][2], self.node.state_array[0][2]

    def swap_3_and_4(self):
        """Needs comments"""
        self.node.state_array[1][0], self.node.state_array[1][1] = \
            self.node.state_array[1][1], self.node.state_array[1][0]

    def swap_3_and_6(self):
        """Needs comments"""
        self.node.state_array[1][0], self.node.state_array[2][0] = \
            self.node.state_array[2][0], self.node.state_array[1][0]

    def swap_4_and_5(self):
        """Needs comments"""
        self.node.state_array[1][1], self.node.state_array[1][2] = \
            self.node.state_array[1][2], self.node.state_array[1][1]

    def swap_4_and_7(self):
        """Needs comments"""
        self.node.state_array[1][1], self.node.state_array[2][1] = \
            self.node.state_array[2][1], self.node.state_array[1][1]

    def swap_5_and_8(self):
        """Needs comments"""
        self.node.state_array[1][2], self.node.state_array[2][2] = \
            self.node.state_array[2][2], self.node.state_array[1][2]

    def swap_6_and_7(self):
        """Needs comments"""
        self.node.state_array[2][0], self.node.state_array[2][1] = \
            self.node.state_array[2][1], self.node.state_array[2][0]

    def swap_7_and_8(self):
        """Needs comments"""
        self.node.state_array[2][1], self.node.state_array[2][2] = \
            self.node.state_array[2][2], self.node.state_array[2][1]

    def add_moves_to_queue(self, moves):
        """Needs comments"""
        for move in moves:
            if not self.check_visited(move):
                array = self.create_array(move)
                path = self.node.path
                path.update({self.counter + 1: move})
                node = self.create_note(array, move, path)
                self.queue.append(node)
                self.visited.update({move: move})
            # if move not in self.visited:

    def make_move(self, node):
        """Needs comments"""
        self.count_up()
        self.node = node

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
            if not self.complete(this_node):
                # if self.counter % 1000 == 0:
                #     print('{}'.format(self.counter))
                location = self.locate_hole(this_node)
                moves = self.check_moves(location)
                self.add_moves_to_queue(moves)
                try:
                    self.make_move(self.queue[0])
                    temp = self.queue[0]
                    array = temp.state_array
                    # self.print_array(array)
                    # print()
                except IndexError:
                    print('queue empty')
                    continue
                # print(moves)
            else:
                self.print_array(self.node.state_array)
                print()
                print(self.counter)
                print()
                return

        my_array = self.node.state_array
        print(''.join(str(elem) for row in my_array for elem in row))
