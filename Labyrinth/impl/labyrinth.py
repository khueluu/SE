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

    def get_position(self):
        return self.__position

    def get_walls(self):
        return deepcopy(self.__walls)

    def set_wall(self, wall_name: str, wall_type: str):
        self.__walls[wall_name] = wall_type
    
    def get_dict(self):
        return {
            'position': self.get_position(),
            'walls': self.get_walls()
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
        self.__maze = self.set_maze(size)
        self.__exit = self.set_exit(random.choice(self.get_monoliths()))
        self.__current = self.__generator.random_cell()
        self.__treasure = self.__generator.random_cell()
        self.__wormholes = self.__generator.random_sequence_of_cells()
        self.__walls = self.set_walls(self.__generator.random_walls())

    def do_found_treasure(self):
        self.__found_treasure = True
        self.__treasure = None

    # Getters
    def get_size(self):
        return self.__size
    
    def get_exit(self):
        return deepcopy(self.__exit)
    
    def get_treasure(self):
        return deepcopy(self.__treasure)

    def get_monoliths(self):
        monoliths = []
        for row in self.__maze:
            for cell in row:
                cell_wall_dict = cell.get_walls()
                for wall_name, wall_type in cell_wall_dict.items():
                    if wall_type == 'monolith':
                        monolith = (cell.get_position(), wall_name)
                        monoliths.append(monolith)
        return tuple(monoliths)

    def get_wormholes(self):
        return self.__wormholes

    def get_wormhole_by_idx(self, idx: int):
        return self.__wormholes[idx]

    def get_walls(self):
        return self.__walls

    def get_current(self):
        return self.__current

    def get_found_treasure(self):
        return self.__found_treasure

    def get_maze(self):
        maze = []
        for row in self.__maze:
            maze_row = []
            for cell in row:
                cell_dict = cell.get_dict()
                maze_row.append(cell_dict)
            maze.append(tuple(maze_row))
        return tuple(maze)

    # Setters
    def set_size(self, size: int):
        self.__size = size

    def set_exit(self, exit_):
        (row, col), wall_name = exit_
        self.__maze[row][col].set_wall(wall_name, 'exit')
        return ((row, col), wall_name)

    def set_treasure(self, treasure):
        self.__treasure = treasure

    def set_wormholes(self, wormholes: tuple):
        self.__wormholes = wormholes

    def set_walls(self, walls: tuple):
        for wall_data in walls:
            (row, col), wall_name = wall_data
            self.__maze[row][col].set_wall(wall_name, 'wall')
        return walls

    def set_current(self, current: tuple):
        self.__current = current

    def set_found_treasure(self, found_treasure: bool):
        self.__found_treasure = found_treasure
    
    def set_maze(self, size: int):
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
        return tuple(maze)

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
