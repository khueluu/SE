import random
from copy import deepcopy

from services.labyrinth import ICell, ILabyrinth
from services.generator import IGenerator
from utils import *

random.seed(0)

class Cell(ICell):
    def __init__(self, row: int, col: int, walls: dict):
        self.__position = (row, col)
        self.__walls = walls
    
    @property
    def position(self):
        return self.__position
    
    @property
    def walls(self):
        return deepcopy(self.__walls)

    def set_wall(self, wall_name: str, wall_type: str):
        self.__walls[wall_name] = wall_type
    
    def get_dict(self):
        return {
            'position': self.position,
            'walls': self.walls
        }


class Labyrinth(ILabyrinth):
    def __init__(self):
        self.__size = None
        self.__maze = None
        self.__current = None
        self.__exit = None
        self.__treasure = None
        self.__found_treasure = False
        self.__wormholes = None
        self.__generator = None
        self.__walls = None
        self.__monoliths = None

    def __getitem__(self, idx: int):
        if self.__maze:
            return self.__maze[idx]
        else:
            return 'Labyrinth has not been created or loaded.'

    def __str__(self):
        return f"""
        'size': ({self.__size}, {self.__size})
        'wormholes': {self.__wormholes}
        'treasure': {self.__treasure}
        'exit': {self.__exit}
        'walls': {self.__walls}
        'current': {self.__current}
        'found_treasure': {self.__found_treasure}
        """

    def create(self, size: int, generator: IGenerator):
        self.__size = size
        self.__generator = generator

        self.__current = self.__generator.random_cell()
        self.__treasure = self.__generator.random_cell()
        self.__wormholes = self.__generator.random_sequence_of_cells()

        self.maze = size
        self.exit = random.choice(self.monoliths)
        self.walls = self.__generator.random_walls()
        
    def do_found_treasure(self):
        self.__found_treasure = True
        self.__treasure = None

    @property
    def size(self):
        return self.__size

    @size.setter 
    def size(self, size: int):
        self.__size = size

    @property
    def maze(self):
        if not self.__maze: return None
        maze = []
        for row in self.__maze:
            maze_row = []
            for cell in row:
                cell_dict = cell.get_dict()
                maze_row.append(cell_dict)
            maze.append(tuple(maze_row))
        return tuple(maze)

    @maze.setter
    def maze(self, data):
        if isinstance(data, int):
            self.set_maze_from_size(size=data)
        elif isinstance(data, list):
            self.set_maze_from_data(data=data)

    @property
    def wormholes(self):
        return self.__wormholes

    @wormholes.setter
    def wormholes(self, data: tuple):
        self.__wormholes = data

    @property
    def found_treasure(self):
        return self.__found_treasure

    @found_treasure.setter
    def found_treasure(self, data: bool):
        self.__found_treasure = data

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, data: tuple):
        self.__current = data

    @property
    def treasure(self):
        return self.__treasure
    
    @treasure.setter
    def treasure(self, data: tuple):
        self.__treasure = data

    @property
    def walls(self):
        return self.__walls

    @walls.setter
    def walls(self, data: tuple):
        for wall_data in data:
            (row, col), wall_name = wall_data
            self.__maze[row][col].set_wall(wall_name, 'wall')
        self.__walls = data

    @property
    def monoliths(self):
        monoliths = []
        for row in self.__maze:
            for cell in row:
                cell_wall_dict = cell.walls
                for wall_name, wall_type in cell_wall_dict.items():
                    if wall_type == 'monolith':
                        monolith = (cell.position, wall_name)
                        monoliths.append(monolith)
        return tuple(monoliths)

    @property
    def exit(self):
        return self.__exit
    
    @exit.setter
    def exit(self, data: tuple):
        (row, col), wall_name = data
        self.__maze[row][col].set_wall(wall_name, 'exit')
        self.__exit = data


    def set_maze_from_size(self, size: int):
        maze = []
        for row in range(size):
            maze_row = []
            for col in range(size):
                walls = {
                    'top': 'monolith' if row == 0 else None,
                    'bottom': 'monolith' if row == size-1 else None,
                    'left': 'monolith' if col == 0 else None,
                    'right': 'monolith' if col == size-1 else None,
                }
                cell = Cell(row, col, walls)
                maze_row.append(cell)
            maze.append(tuple(maze_row))
        self.__maze = tuple(maze)

    
    def set_maze_from_data(self, data: list):
        new_maze = []
        for maze_row in data:
            new_maze_row = []
            for cell in maze_row:
                row, col = cell.get('position')
                walls = cell.get('walls')
                new_maze_row.append(Cell(row, col, walls))
            new_maze.append(tuple(new_maze_row))
        self.__maze = tuple(new_maze)



