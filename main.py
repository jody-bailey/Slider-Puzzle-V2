# Jody Bailey
# Intro to AI
# 10/31/2018
# The purpose of this program is to have the user enter a starting state
# or choose random generation and the program will create a sliding puzzle
# board. The program will then perform the searches that the user specifies
# and outputs the final result. It will also print the amount of time that
# the program took to execute.
"""Main Class"""

import time
import os
from breadth_first import BreadthSearch
from depth_first import DepthSearch
from misplaced_tiles import MisplacedTiles
from manhattan import ManhattanDistance
from generator import Generator
from test_generator import TestGenerator
from node import Node
import csv


class Main:
    """The purpose of this class is to perform all of the actions needed for the program to execute"""

    state_array = []
    state_string = ''

    STARTING_POSITION = ''

    test_states = []
    is_test = False

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

    def create_array(self, state_string):
        array = [0] * 3
        for i in range(3):
            array[i] = [0] * 3

        index = 0
        for i in range(3):
            for j in range(3):
                array[i][j] = int(state_string[index])
                index += 1

        return array

    # Method to print the array
    def print_array(self):
        for row in self.state_array:
            print(' '.join(str(elem) for elem in row))

    # Method to create a new node
    @staticmethod
    def create_node(state_array, state_string, heuristic=None):
        path = [state_string]
        node = Node(state_array, state_string, path, heuristic=heuristic)

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
        print('[3] Use previous starting position')
        print('[4] Run test. (10 runs of each search)')
        answer = input()
        print()
        while answer != '1' and answer != '2' and answer != '3' and answer != '4':
            answer = input('Please enter either \'1\', \'2\', \'3\' or \'4\'.\n')

        if answer == '1':
            state = input('Please enter the starting positions.\n'
                          '(Numbers between 0-8 with no numbers repeated)\n')
            while not self.check_state(state):
                state = input('Not a valid starting state. Try again!!\n')

            self.STARTING_POSITION = state
            answers['state'] = state
            answers['array'] = None
        elif answer == '2':
            generator = Generator()
            generator.set_array()
            generator.randomize()

            answers['array'] = generator.get_array()
            answers['state'] = None
        elif answer == '3':
            if self.STARTING_POSITION == '':
                print('You must run a previous test first!\n')
                return -1
            else:
                answers['state'] = self.STARTING_POSITION
                answers['array'] = None
        elif answer == '4':
            self.is_test = True
            all_states = []
            for _ in range(10):
                generator = TestGenerator()
                generator.set_array()
                generator.randomize()
                state_string = generator.get_state_string(generator.get_array())
                all_states.append(state_string)
            self.test_states = all_states
            return

        if answer == '4':
            answer2 = input('Please select which search you would like to perform: \n'
                            '[1] Breadth First Search\n'
                            '[2] Depth First Search\n'
                            '[3] A* Misplaced Tiles\n'
                            '[4] A* Manhatten Distance\n')
            while answer2 != '1' and answer2 != '2' and answer2 != '3' and answer2 != '4':
                answer2 = input('Invalid answer. Please try again!\n')
        else:
            answer2 = input('Please select which search you would like to perform: \n'
                            '[1] Breadth First Search\n'
                            '[2] Depth First Search\n'
                            '[3] A* Misplaced Tiles\n'
                            '[4] A* Manhatten Distance\n'
                            '[5] All\n')
            while answer2 != '1' and answer2 != '2' and answer2 != '3' and answer2 != '4' and answer2 != '5':
                answer2 = input('Invalid answer. Please try again!\n')

        print()
        if answer2 == '1':
            answers['search'] = 'breadth'
        elif answer2 == '2':
            answers['search'] = 'depth'
        elif answer2 == '3':
            answers['search'] = 'misplaced'
        elif answer2 == '4':
            answers['search'] = 'manhattan'
        elif answer2 == '5':
            answers['search'] = 'all'

        return answers

    # This method is used to create the CSV file after running a test.
    # It takes in a nested map to get all the information from the searches
    # completed and writes the data to it's respective location in the file.
    def create_csv(self, test_map):
        with open('SliderPuzzle.csv', 'w', newline='') as file:
            the_writer = csv.writer(file)

            for i in range(4):
                for j in range(10):
                    if i == 0:
                        if j == 0:
                            the_writer.writerow(['Breadth First Search'])
                            the_writer.writerow(
                                ['Starting State', 'Solution?', 'Depth', 'Path', 'Node Count', 'Time Elapsed'])
                        the_writer.writerow([test_map['breadth']['start'][j], test_map['breadth']['solution'][j],
                                             test_map['breadth']['depth'][j],
                                             test_map['breadth']['path'][j], test_map['breadth']['node_count'][j],
                                             test_map['breadth']['times'][j]])
                        if j == 9:
                            the_writer.writerow('\n')
                    elif i == 1:
                        if j == 0:
                            the_writer.writerow(['Depth First Search'])
                            the_writer.writerow(
                                ['Starting State', 'Solution?', 'Depth', 'Path', 'Node Count', 'Time Elapsed'])
                        the_writer.writerow([test_map['depth']['start'][j], test_map['depth']['solution'][j],
                                             test_map['depth']['depth'][j],
                                             test_map['depth']['path'][j], test_map['depth']['node_count'][j],
                                             test_map['depth']['times'][j]])
                        if j == 9:
                            the_writer.writerow('\n')
                    elif i == 2:
                        if j == 0:
                            the_writer.writerow(['A* Misplaced Tiles'])
                            the_writer.writerow(
                                ['Starting State', 'Solution?', 'Depth', 'Path', 'Node Count', 'Time Elapsed'])
                        the_writer.writerow([test_map['misplaced']['start'][j], test_map['misplaced']['solution'][j],
                                             test_map['misplaced']['depth'][j],
                                             test_map['misplaced']['path'][j], test_map['misplaced']['node_count'][j],
                                             test_map['misplaced']['times'][j]])
                        if j == 9:
                            the_writer.writerow('\n')
                    elif i == 3:
                        if j == 0:
                            the_writer.writerow(['A* Manhattan Distance'])
                            the_writer.writerow(
                                ['Starting State', 'Solution?', 'Depth', 'Path', 'Node Count', 'Time Elapsed'])
                        the_writer.writerow([test_map['manhattan']['start'][j], test_map['manhattan']['solution'][j],
                                             test_map['manhattan']['depth'][j],
                                             test_map['manhattan']['path'][j], test_map['manhattan']['node_count'][j],
                                             test_map['manhattan']['times'][j]])

    # This method is used when the user selects to run a test.
    # It is used instead of the regular run method.
    # It performs a loop 10 times, each with a different starting state
    # and runs each search on each starting state and records the results.
    # The data gathered in this method is passed to the create_csv() method.
    def run_test(self):
        test_map = {'breadth': {'search': [], 'start': [], 'solution': [], 'depth': [], 'path': [], 'node_count': [],
                                'times': []},
                    'depth': {'search': [], 'start': [], 'solution': [], 'depth': [], 'path': [], 'node_count': [],
                              'times': []},
                    'misplaced': {'search': [], 'start': [], 'solution': [], 'depth': [], 'path': [], 'node_count': [],
                                  'times': []},
                    'manhattan': {'search': [], 'start': [], 'solution': [], 'depth': [], 'path': [], 'node_count': [],
                                  'times': []}}

        for i in range(10):
            array = self.create_array(self.test_states[i])
            state = self.test_states[i]
            start = time.time()

            node = self.create_node(array, state)
            breadth = BreadthSearch(node)
            breadth.run()
            test_map['breadth']['solution'].append(breadth.get_solution_found())
            test_map['breadth']['depth'].append(breadth.get_final_depth())
            test_map['breadth']['path'].append(breadth.get_path())
            test_map['breadth']['node_count'].append(breadth.get_node_count())
            test_map['breadth']['search'].append('Breadth First')
            stop = time.time()
            time_elapsed = stop - start
            test_map['breadth']['times'].append(time_elapsed)
            test_map['breadth']['start'].append(state)

            start = time.time()
            node2 = self.create_node(array, state)
            depth = DepthSearch(node2)
            depth.run()
            test_map['depth']['solution'].append(depth.get_solution_found())
            test_map['depth']['depth'].append(depth.get_final_depth())
            test_map['depth']['path'].append(depth.get_path())
            test_map['depth']['node_count'].append(depth.get_node_count())
            test_map['depth']['search'].append('Depth First')
            stop = time.time()
            time_elapsed = stop - start
            test_map['depth']['times'].append(time_elapsed)
            test_map['depth']['start'].append(state)

            start = time.time()
            heuristic = MisplacedTiles.out_of_place_tiles(array)
            node3 = Node(array, state, heuristic=heuristic)
            node3.path = [node3.state_string]
            misplaced = MisplacedTiles(node3)
            misplaced.run()
            test_map['misplaced']['solution'].append(misplaced.get_solution_found())
            test_map['misplaced']['depth'].append(misplaced.get_final_depth())
            test_map['misplaced']['path'].append(misplaced.get_path())
            test_map['misplaced']['node_count'].append(misplaced.get_node_count())
            test_map['misplaced']['search'].append('Misplaced Tiles')
            stop = time.time()
            time_elapsed = stop - start
            test_map['misplaced']['times'].append(time_elapsed)
            test_map['misplaced']['start'].append(state)

            heuristic = ManhattanDistance.manhattan_distance(array)
            node4 = Node(array, state, heuristic=heuristic)
            node4.path = [node4.state_string]
            manhattan = ManhattanDistance(node4)
            manhattan.run()
            test_map['manhattan']['solution'].append(manhattan.get_solution_found())
            test_map['manhattan']['depth'].append(manhattan.get_final_depth())
            test_map['manhattan']['path'].append(manhattan.get_path())
            test_map['manhattan']['node_count'].append(manhattan.get_node_count())
            test_map['manhattan']['search'].append('Manhattan Distance')

            stop = time.time()
            time_elapsed = stop - start
            test_map['manhattan']['times'].append(time_elapsed)
            test_map['manhattan']['start'].append(state)

        self.create_csv(test_map)
        self.is_test = False

    # The main method of this class. It brings together all of the
    # functionality from the other functions to run the program.
    def run(self):
        answer = 'y'
        while answer == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            answers = self.display_menu()

            if self.is_test:
                self.run_test()
                print()
                answer = input('Would you like to perform another test or search? (y/n)\n')
                while answer != 'y' and answer != 'n':
                    answer = input('Invalid answer. Type \'y\' for yes and \'n\' for no.\n')
                continue

            while answers == -1:
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
                self.STARTING_POSITION = answers['state']
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
            elif answers['search'] == 'misplaced':
                heuristic = MisplacedTiles.out_of_place_tiles(array)
                # node = self.create_node(array, answers['state'], heuristic)
                node = Node(array, answers['state'], heuristic=heuristic)
                node.path = [node.state_string]
                misplaced = MisplacedTiles(node)
                misplaced.run()
            elif answers['search'] == 'manhattan':
                heuristic = ManhattanDistance.manhattan_distance(array)
                node4 = Node(array, answers['state'], heuristic=heuristic)
                node4.path = [node4.state_string]
                manhattan = ManhattanDistance(node4)
                manhattan.run()
            elif answers['search'] == 'all':
                node1 = self.create_node(array, answers['state'])
                node1.path = [node1.state_string]
                node2 = self.create_node(array, answers['state'])
                heuristic = MisplacedTiles.out_of_place_tiles(array)
                node3 = Node(array, answers['state'], heuristic=heuristic)
                node3.path = [node3.state_string]
                heuristic = ManhattanDistance.manhattan_distance(array)
                node4 = Node(array, answers['state'], heuristic=heuristic)
                node4.path = [node4.state_string]

                breadth = BreadthSearch(node1)
                breadth.run()
                depth = DepthSearch(node2)
                depth.run()
                misplaced = MisplacedTiles(node3)
                misplaced.run()
                manhattan = ManhattanDistance(node4)
                manhattan.run()
            end = time.time()
            print('Search(es) completed in {} seconds.'.format(end - start))
            print()
            answer = input('Would you like to run another search? (y/n)\n')
            while answer not in ('y', 'n'):
                answer = input('Invalid answer. Please enter \'y\' for yes and \'n\' for no.\n')


if __name__ == '__main__':
    RUN = Main()
    RUN.run()
