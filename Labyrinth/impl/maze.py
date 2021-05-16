from copy import deepcopy
import random

random.seed(1)

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.top_wall = None
        self.bottom_wall = None
        self.left_wall = None
        self.right_wall = None

    def __str__(self):
        return f"<Cell object at ({self.row}, {self.col})>"
        

class Labyrinth:
    def __init__(self, size):
        self.size = size
        self.maze = self.create_maze(self.size)
        self.monoliths = set()
        self.set_monolith()
    
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
        for row in range(self.size):
            for col in range(self.size):
                if row == 0:
                    self.maze[row][col].top_wall == 'monolith'
                    self.monoliths.add(f'cell_{row}_{col}_top_wall')
                if row == 3:
                    self.maze[row][col].bottom_wall == 'monolith'
                    self.monoliths.add(f'cell_{row}_{col}_bottom_wall')
                if col == 0:
                    self.maze[row][col].left_wall == 'monolith'
                    self.monoliths.add(f'cell_{row}_{col}_left_wall')
                if col == 3:
                    self.maze[row][col].right_wall == 'monolith'
                    self.monoliths.add(f'cell_{row}_{col}_right_wall')




if __name__ == "__main__":
    lbr = Labyrinth(size=4)
    maze = lbr.maze
    print(lbr.monoliths)
    