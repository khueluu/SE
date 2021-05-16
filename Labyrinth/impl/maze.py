from copy import deepcopy

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f"<Cell object at ({self.row}, {self.col})>"

class Labyrinth:
    def __init__(self, size):
        self.size = size
        self.maze = self.create_maze(self.size)

    def create_maze(self, size):
        maze = []
        for row in range(size):
            maze_row = []
            for col in range(size):
                cell = Cell(row, col)
                maze_row.append(cell)
            maze.append(maze_row)
        return deepcopy(maze)
    
    def __str__(self):
        return f"<Labyrinth object of size ({self.size}x{self.size})>"

    def __getitem__(self, idx):
        return self.maze[idx]

if __name__ == "__main__":
    lbr = Labyrinth(size=4)
    maze = lbr.maze

    print(lbr[0][0])
    print(maze[0][0])