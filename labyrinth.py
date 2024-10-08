import time


class LabyrinthSolver:
    def __init__(self, labyrinth, start, end):
        self.labyrinth = labyrinth
        self.start = start
        self.end = end

    def can_move(self, x, y):
        if x < len(self.labyrinth) and y < len(self.labyrinth) and self.labyrinth[x][y] == 0:
            return True
        else:
            return False

    def move_back(self, x, y):
        if x < len(self.labyrinth) and y < len(self.labyrinth) and self.labyrinth[x][y] == '/':
            return True
        else:
            return False

    def print_labyrinth(self):
        for row in self.labyrinth:
            for_print = ''
            for cell in row:
                for_print += str(cell) + ' '
            print(for_print)
        print()
        time.sleep(1)

    def find_path(self, x=None, y=None):
        if x is None and y is None:
            x = self.start[0]
            y = self.start[1]

        if x == self.end[0] and y == self.end[1]:
            print("Yey, yupi!!")
            self.print_labyrinth()
            return True

        self.print_labyrinth()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if self.can_move(new_x, new_y):
                self.labyrinth[x][y] = '/'
                self.labyrinth[new_x][new_y] = 2
                if self.find_path(new_x, new_y):
                    return True
            else:
                self.labyrinth[x][y] = 'x'
                if self.move_back(x, y):
                    # self.labyrinth[new_x][new_y] = 'x'
                    if self.find_path(new_x, new_y):
                        self.print_labyrinth()
                        # self.labyrinth[new_x][new_y] = 'x'
                        return True


labyrinth = [
    [0, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0]
]

start = (0, 0)
end = (4, 3)

solver = LabyrinthSolver(labyrinth, start, end)
solver.find_path()
