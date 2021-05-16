from copy import deepcopy
import random

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {
            "top_wall": None,
            "bottom_wall": None,
            "left_wall": None,
            "right_wall": None
        }

    def __str__(self):
        return f"<Cell object at ({self.row}, {self.col})>"
        

class Labyrinth:
    def __init__(self, size):
        self.size = size
        self.maze = self.create_maze(self.size)
        self.monoliths = self.set_monolith()
        self.set_exit()
        
    def __str__(self):
        return f"<Labyrinth object of size ({self.size}x{self.size})>"

    def __getitem__(self, idx):
        return self.maze[idx]

    def create_maze(self, size):
        maze = []
        for row in range(size):
            maze_row = []
            for col in range(size):
                cell = Cell(row, col)
                maze_row.append(cell)
            maze.append(maze_row)
        return deepcopy(maze)

    def set_monolith(self):
        monoliths = []
        for row in range(self.size):
            for col in range(self.size):
                if row == 0:
                    self.maze[row][col].walls["top_wall"] = 'monolith'
                    monoliths.append((row, col, 'top_wall'))
                if row == 3:
                    self.maze[row][col].walls["bottom_wall"] = 'monolith'
                    monoliths.append((row, col, 'bottom_wall'))
                if col == 0:
                    self.maze[row][col].walls["left_wall"] = 'monolith'
                    monoliths.append((row, col, 'left_wall'))
                if col == 3:
                    self.maze[row][col].walls["right_wall"] = 'monolith'
                    monoliths.append((row, col, 'right_wall'))
        return monoliths

    def set_exit(self):
        exit_row, exit_col, exit_wall = random.choice(self.monoliths)
        self.maze[exit_row][exit_col].walls[exit_wall] = 'exit'
        

if __name__ == "__main__":
    lbr = Labyrinth(size=4)
    maze = lbr.maze
    for r, c, w in lbr.monoliths:
        print(r, c, lbr[r][c].walls)

    