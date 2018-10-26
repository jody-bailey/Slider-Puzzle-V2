from breadth_first import BreadthSearch
import random

class Generator:
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

    def __init__(self):
        self.array = [0] * 3
        for i in range(3):
            self.array[i] = [0] * 3

        self.zero = [self.swap_0_and_1, self.swap_0_and_3]
        self.one = [self.swap_0_and_1, self.swap_1_and_2, self.swap_1_and_4]
        self.two = [self.swap_1_and_2, self.swap_2_and_5]
        self.three = [self.swap_0_and_3, self.swap_3_and_4, self.swap_3_and_6]
        self.four = [self.swap_1_and_4, self.swap_3_and_4, self.swap_4_and_7, self.swap_4_and_5]
        self.five = [self.swap_2_and_5, self.swap_4_and_5, self.swap_5_and_8]
        self.six = [self.swap_3_and_6, self.swap_6_and_7]
        self.seven = [self.swap_4_and_7, self.swap_6_and_7, self.swap_7_and_8]
        self.eight = [self.swap_5_and_8, self.swap_7_and_8]

    def set_array(self):
        state = '123456780'
        index = 0
        for i in range(3):
            for j in range(3):
                self.array[i][j] = int(state[index])
                index += 1

    def print_array(self):
        print(' '.join(str(elem) for row in self.array for elem in row))

    def randomize(self):
        rand = random.randint(500, 1000)

        for i in range(rand):
            loc = BreadthSearch.locate_hole(self.array)
            if loc == (0, 0):
                random.choice(self.zero)()
            elif loc == (0, 1):
                random.choice(self.one)()
            elif loc == (0, 2):
                random.choice(self.two)()
            elif loc == (1, 0):
                random.choice(self.three)()
            elif loc == (1, 1):
                random.choice(self.four)()
            elif loc == (1, 2):
                random.choice(self.five)()
            elif loc == (2, 0):
                random.choice(self.six)()
            elif loc == (2, 1):
                random.choice(self.seven)()
            elif loc == (2, 2):
                random.choice(self.eight)()

    def get_array(self):
        return self.array

    def swap_0_and_1(self):
        """Needs comments"""
        self.array[0][0], self.array[0][1] = \
            self.array[0][1], self.array[0][0]

    def swap_0_and_3(self):
        """Needs comments"""
        self.array[0][0], self.array[1][0] = \
            self.array[1][0], self.array[0][0]

    def swap_1_and_2(self):
        """Needs comments"""
        self.array[0][1], self.array[0][2] = \
            self.array[0][2], self.array[0][1]

    def swap_1_and_4(self):
        """Needs comments"""
        self.array[0][1], self.array[1][1] = \
            self.array[1][1], self.array[0][1]

    def swap_2_and_5(self):
        """Needs comments"""
        self.array[0][2], self.array[1][2] = \
            self.array[1][2], self.array[0][2]

    def swap_3_and_4(self):
        """Needs comments"""
        self.array[1][0], self.array[1][1] = \
            self.array[1][1], self.array[1][0]

    def swap_3_and_6(self):
        """Needs comments"""
        self.array[1][0], self.array[2][0] = \
            self.array[2][0], self.array[1][0]

    def swap_4_and_5(self):
        """Needs comments"""
        self.array[1][1], self.array[1][2] = \
            self.array[1][2], self.array[1][1]

    def swap_4_and_7(self):
        """Needs comments"""
        self.array[1][1], self.array[2][1] = \
            self.array[2][1], self.array[1][1]

    def swap_5_and_8(self):
        """Needs comments"""
        self.array[1][2], self.array[2][2] = \
            self.array[2][2], self.array[1][2]

    def swap_6_and_7(self):
        """Needs comments"""
        self.array[2][0], self.array[2][1] = \
            self.array[2][1], self.array[2][0]

    def swap_7_and_8(self):
        """Needs comments"""
        self.array[2][1], self.array[2][2] = \
            self.array[2][2], self.array[2][1]

