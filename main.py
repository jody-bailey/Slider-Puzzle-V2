# Jody Bailey
# Intro to AI
# 10/31/2018
# The purpose of this program is to have the user enter a starting state
# or choose random generation and the program will create a sliding puzzle
# board. The program will then perform the searches that the user specifies
# and outputs the final result. It will also print the amount of time that
# the program took to execute.
"""Main Class"""

from breadth_first import BreadthSearch
from depth_first import DepthSearch
from generator import Generator
from node import Node
import time


class Main:
    """The purpose of this class is to perform all of the actions needed for the program to execute"""

    state_array = []
    state_string = ''

    # Constructor
    def __init__(self, state_string=None):
        self.state_array = [0] * 3
        for i in range(3):
            self.state_array[i] = [0] * 3
        self.state_string = state_string

    # Method to set the class level variable called 'state_array'
    def set_array(self):
        index = 0
        for i in range(3):
            for j in range(3):
                self.state_array[i][j] = int(self.state_string[index])
                index += 1

    # Method to print the array
    def print_array(self):
        for row in self.state_array:
            print(' '.join(str(elem) for elem in row))

    # Method to create a new node
    @staticmethod
    def create_node(state_array, state_string):
        path = [state_string]
        node = Node(state_array, state_string, path)

        return node

    # Method to check the user input for the state.
    # Makes sure the user input a valid starting state.
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

    # Method to display the menu to the user and return the user's
    # selections to the run() method.
    def display_menu(self):
        answers = {}
        print('Please select from the following menu options:\n')
        print('[1] Enter starting positions')
        print('[2] Randomly generate starting positions')
        answer = input()
        print()
        while answer != '1' and answer != '2':
            answer = input('Please enter either \'1\' or \'2\'\n')

        if answer == '1':
            state = input('Please enter the starting positions.\n'
                          '(Numbers between 0-8 with no numbers repeated)\n')
            while not self.check_state(state):
                state = input('Not a valid starting state. Try again!!\n')

            answers['state'] = state
            answers['array'] = None
        elif answer == '2':
            generator = Generator()
            generator.set_array()
            generator.randomize()

            answers['array'] = generator.get_array()
            answers['state'] = None

        answer2 = input('Please select which search you would like to perform: \n'
                        '[1] Breadth First Search\n'
                        '[2] Depth First Search\n'
                        '[3] Both\n')
        while answer2 != '1' and answer2 != '2' and answer2 != '3':
            answer2 = input('Invalid answer. Please try again!')
        print()
        if answer2 == '1':
            answers['search'] = 'breadth'
        elif answer2 == '2':
            answers['search'] = 'depth'
        elif answer2 == '3':
            answers['search'] = 'both'

        return answers

    # The main method of this class. It brings together all of the
    # functionality from the other functions to run the program.
    def run(self):
        """Needs comments"""
        answers = self.display_menu()
        start = time.time()
        array = []
        if answers['array'] is None:
            self.state_string = answers['state']
            self.set_array()
            array = self.state_array
            # array = BreadthSearch.create_array(answers['state'])
        elif answers['state'] is None:
            array = answers['array']
            self.state_array = array
            answers['state'] = BreadthSearch.create_state_string(array)
        print('Starting Array:')
        self.print_array()
        print()
        if answers['search'] == 'breadth':
            node = self.create_node(array, answers['state'])
            breadth = BreadthSearch(node)
            breadth.run()
        elif answers['search'] == 'depth':
            node = self.create_node(array, answers['state'])
            depth = DepthSearch(node)
            depth.run()
        elif answers['search'] == 'both':
            node1 = self.create_node(array, answers['state'])
            node2 = self.create_node(array, answers['state'])
            breadth = BreadthSearch(node1)
            breadth.run()
            depth = DepthSearch(node2)
            depth.run()
        end = time.time()
        print('Search(es) completed in {} seconds.'.format(end - start))


if __name__ == '__main__':
    RUN = Main()
    RUN.run()
