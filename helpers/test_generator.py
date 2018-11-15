# Jody Bailey
# Intro to AI
# 10/31/2018
# This class is used to generate random boards that the program can
# then use for the different searches.

from searches.breadth_first import BreadthSearch
from helpers.interface import Interface
import random


class TestGenerator(Interface):
    array = []
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []

    # Constructor
    def __init__(self):
        self.array = [0] * 3
        for i in range(3):
            self.array[i] = [0] * 3

        self.moves = [self.swap_0_and_1, self.swap_0_and_3, self.swap_1_and_2, self.swap_1_and_4,
                      self.swap_2_and_5, self.swap_3_and_4, self.swap_3_and_6, self.swap_4_and_5,
                      self.swap_4_and_7, self.swap_5_and_8, self.swap_6_and_7, self.swap_7_and_8]

    # Method used to set the class level variable named 'array'
    def set_array(self):
        state = '123456780'
        index = 0
        for i in range(3):
            for j in range(3):
                self.array[i][j] = int(state[index])
                index += 1

    # This method will take the goal state of a board and apply random
    # moves to it to create a random board every time.
    def randomize(self):
        rand = random.randint(500, 1000)

        for i in range(rand):
            loc = BreadthSearch.locate_hole(self.array)
            if loc == (0, 0):
                random.choice(self.moves)()
            elif loc == (0, 1):
                random.choice(self.moves)()
            elif loc == (0, 2):
                random.choice(self.moves)()
            elif loc == (1, 0):
                random.choice(self.moves)()
            elif loc == (1, 1):
                random.choice(self.moves)()
            elif loc == (1, 2):
                random.choice(self.moves)()
            elif loc == (2, 0):
                random.choice(self.moves)()
            elif loc == (2, 1):
                random.choice(self.moves)()
            elif loc == (2, 2):
                random.choice(self.moves)()

    def get_array(self):
        return self.array

    # All of the methods below are used from swapping the position of
    # 0 and the new location of 0.
    def swap_0_and_1(self):
        self.array[0][0], self.array[0][1] = \
            self.array[0][1], self.array[0][0]

    def swap_0_and_3(self):
        self.array[0][0], self.array[1][0] = \
            self.array[1][0], self.array[0][0]

    def swap_1_and_2(self):
        self.array[0][1], self.array[0][2] = \
            self.array[0][2], self.array[0][1]

    def swap_1_and_4(self):
        self.array[0][1], self.array[1][1] = \
            self.array[1][1], self.array[0][1]

    def swap_2_and_5(self):
        self.array[0][2], self.array[1][2] = \
            self.array[1][2], self.array[0][2]

    def swap_3_and_4(self):
        self.array[1][0], self.array[1][1] = \
            self.array[1][1], self.array[1][0]

    def swap_3_and_6(self):
        self.array[1][0], self.array[2][0] = \
            self.array[2][0], self.array[1][0]

    def swap_4_and_5(self):
        self.array[1][1], self.array[1][2] = \
            self.array[1][2], self.array[1][1]

    def swap_4_and_7(self):
        self.array[1][1], self.array[2][1] = \
            self.array[2][1], self.array[1][1]

    def swap_5_and_8(self):
        self.array[1][2], self.array[2][2] = \
            self.array[2][2], self.array[1][2]

    def swap_6_and_7(self):
        self.array[2][0], self.array[2][1] = \
            self.array[2][1], self.array[2][0]

    def swap_7_and_8(self):
        self.array[2][1], self.array[2][2] = \
            self.array[2][2], self.array[2][1]
