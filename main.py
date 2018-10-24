"""This module needs comments"""
from breadth_first import BreadthSearch
from node import Node


class Main:
    """This class needs comments"""
    state_array = []
    state_string = ''

    def __init__(self, state_string):
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

    def run(self):
        """Needs comments"""
        self.set_array()
        node = self.create_note(self.state_array, self.state_string)
        search = BreadthSearch(node)
        if not search.complete(node.state_array):
            search.run()
        self.print_array()


if __name__ == '__main__':
    RUN = Main('783415602')
    RUN.run()
