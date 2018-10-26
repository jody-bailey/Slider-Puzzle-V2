"""This module needs comments"""
from breadth_first import BreadthSearch
from node import Node
import time


class Main:
    """This class needs comments"""
    state_array = []
    state_string = ''

    def __init__(self, state_string=None):
        self.state_array = [0] * 3
        for i in range(3):
            self.state_array[i] = [0] * 3
        self.state_string = state_string

    def set_array(self):
        """Needs comments"""
        index = 0
        for i in range(3):
            for j in range(3):
                self.state_array[i][j] = int(self.state_string[index])
                index += 1

    def print_array(self):
        """Needs comments"""
        for row in self.state_array:
            print(' '.join(str(elem) for elem in row))

    @staticmethod
    def create_note(state_array, state_string):
        """Needs comments"""
        path = {0: state_string}
        node = Node(state_array, state_string, path)

        return node

    def check_state(self, state):
        if len(state) != 9:
            return False
        valid = True
        try:
            for i in range(8):
                if state.count(str(i)) > 1 or state.count(str(i)) == 0:
                    valid = False
                    return False
        except IndexError:
            valid = False
            return False
        finally:
            if valid:
                return True

    def display_menu(self):
        print('Please select from the following menu options:\n')
        print('[1] Enter starting positions')
        print('[2] Randomly generate starting positions')
        answer = input()
        while answer != '1' and answer != '2':
            answer = input('Please enter either \'1\' or \'2\'\n')

        if answer == '1':
            state = input('Please enter the starting positions.\n'
                          '(Numbers between 0-8 with no numbers repeated)\n')
            while not self.check_state(state):
                state = input('Enter the right numbers retard!\n')
            return state

    def run(self):
        """Needs comments"""
        state = self.display_menu()
        start = time.time()
        array = BreadthSearch.create_array(state)
        # self.set_array()
        node = self.create_note(array, state)
        search = BreadthSearch(node)
        if not search.complete(node):
            search.run()
        end = time.time()
        print(end - start)


if __name__ == '__main__':
    RUN = Main()
    RUN.run()
