import time
import queue


class LabyrinthSolver:
    def __init__(self, labyrinth, start, end):
        """
        Initialize the labyrinth solver.
        :param labyrinth: list
        :param start: tuple
        :param end: i
        """
        self.labyrinth = labyrinth
        self.start = start
        self.end = end

    def can_move(self, x, y):
        """
        Checks if the solver can move at the given coordinates.
        :param x: int (the x coordinate)
        :param y: i (the y coordinate)
        :return: bool (True if the solver can, False otherwise)
        """
        if 0 <= x < len(self.labyrinth) and 0 <= y < len(self.labyrinth[0]) and self.labyrinth[x][y] == 0:
            return True
        else:
            return False

    def print_labyrinth(self):
        """
        Prints the labyrinth.
        :return: str with labyrinth
        """
        for row in self.labyrinth:
            for_print = ''
            for cell in row:
                for_print += str(cell) + ' '
            print(for_print)
        print()
        time.sleep(1)

    def find_path(self):
        """
        Finds the path from start to end of the labyrinth. Using backtracking and BFS.
        :param x: int (x coordinate)
        :param y: i (y coordinate)
        :return: bool(True if path found, False if not.)
        """
        moves = queue.Queue()
        moves.put([self.start])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while not moves.empty():
            path = moves.get()
            x, y = path[-1]
            if x == self.end[0] and y == self.end[1]:
                for x, y in path:
                    labyrinth[x][y] = "/"
                print("Yey, yupi!! Path found.")
                self.print_labyrinth()
                return True

            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]

                if self.can_move(new_x, new_y):
                    new_path = list(path)
                    new_path.append((new_x, new_y))
                    moves.put(new_path)

                    self.labyrinth[new_x][new_y] = 2
                    self.print_labyrinth()
        return False


labyrinth = [
    [0, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0]
]

start = (0, 0)
end = (4, 3)

solver = LabyrinthSolver(labyrinth, start, end)

if solver.find_path() is False:
    print("Bro, labyrinth is a bit impossible.-_-")
