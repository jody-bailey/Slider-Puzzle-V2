from node import Node


class Interface:

    # Method used to create a node from the Node class.
    @staticmethod
    def create_node(state_array, state_string, depth, heuristic, parent):
        node = Node(state_array, state_string, depth, heuristic, parent=parent)

        return node

    # Method used to create the array when given the state_string
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

    # Method used to create the state string when you pass it an array.
    @staticmethod
    def create_state_string(array):
        state = ''
        for i in range(3):
            for j in range(3):
                state += str(array[i][j])
        return state

    # Method to determine if the node passed in is the goal state.
    @staticmethod
    def complete(node):
        # path = ''.join(str(elem) for row in node for elem in row)
        return node.state_string == '123456780'

    # Method used to get the state string from an array
    @staticmethod
    def get_state_string(node):
        return ''.join(str(elem) for row in node for elem in row)

    # Method to find the position of 0.
    @staticmethod
    def locate_hole(node):
        array = node
        for i in range(3):
            for j in range(3):
                if array[i][j] == 0:
                    return i, j

    # Method to check if the new location would be out of bounds.
    @staticmethod
    def check_bounds(location):
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
    @staticmethod
    def swap_locations(node, location, new_loc):
        test_node = node
        test_node[location[0]][location[1]], test_node[new_loc[0]][new_loc[1]] = \
            test_node[new_loc[0]][new_loc[1]], test_node[location[0]][location[1]]
        return test_node

    # Method to print an array
    @staticmethod
    def print_array(array):
        for row in array:
            print(' '.join(str(elem) for elem in row))
