import random
import json
from copy import deepcopy

from services.labyrinth import ICell, ILabyrinth, ILabyrinthGenerator
from utils import *

random.seed(0)

class Cell(ICell):
    def __init__(self, row: int, col: int, walls: dict):
        self.__position = (row, col)
        self.__walls = walls

    def get_position(self):
        return deepcopy(self.__position)

    def get_walls(self):
        return deepcopy(self.__walls)

    def set_wall(self, wall_name: str, wall_type: str):
        self.__walls[wall_name] = wall_type


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

    def __getitem__(self, idx):
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

    def create(self, size: int, generator: ILabyrinthGenerator):
        self.__size = size
        self.__generator = generator
        self.__maze = self.create_maze(size)
        self.__exit = self.set_exit_to_maze()
        self.__current = self.__generator.random_cell()
        self.__treasure = self.__generator.random_cell()
        self.__wormholes = self.__generator.random_sequence_of_cells()
        self.__walls = self.set_walls_to_maze()

    def get_size(self):
        return self.__size
    
    def get_exit(self):
        return deepcopy(self.__exit)
    
    def get_treasure(self):
        return deepcopy(self.__treasure)

    def get_wormholes(self):
        return deepcopy(self.__wormholes)

    def get_wormhole_by_idx(self, idx: int):
        return deepcopy(self.__wormholes[idx])

    def get_walls(self):
        return deepcopy(self.__walls)

    def get_current(self):
        return deepcopy(self.__current)

    def set_current(self, row, col):
        self.__current = (row, col)

    def get_current_cell(self):
        row, col = self.__current
        return self.__maze[row][col]

    def get_found_treasure(self):
        return self.__found_treasure
        
    def set_found_treasure(self):
        self.__found_treasure = True
        self.__treasure = None

    def set_walls_to_maze(self):
        random_walls = self.__generator.random_walls()
        for wall_data in random_walls:
            (row, col), wall_name = wall_data
            self.__maze[row][col].set_wall(wall_name, 'wall')
        return deepcopy(random_walls)

    def set_exit_to_maze(self):
        (row, col), wall_name = random.choice(self.get_monoliths())
        self.__maze[row][col].set_wall(wall_name, 'exit')
        return (row, col)

    def create_maze(self, size):
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
            maze.append(maze_row)
        return deepcopy(maze)

    def get_monoliths(self):
        monoliths = []
        for row in self.__maze:
            for cell in row:
                cell_wall_dict = cell.get_walls()
                for wall_name, wall_type in cell_wall_dict.items():
                    if wall_type == 'monolith':
                        monolith = (cell.get_position(), wall_name)
                        monoliths.append(monolith)
        return deepcopy(monoliths)

    def save(self, output_file='labyrinth.txt'):
        state_dict = {
            'size': self.__size,
            'maze': self.__maze,
            'wormholes': self.__wormholes,
            'treasure': self.__treasure,
            'exit': self.__exit,
            'walls': self.__walls,
            'current': self.__current,
            'found_treasure': self.__found_treasure
        }

        with open(output_file, 'w') as f:
            f.write(json.dumps(state_dict))

    def load(self, input_file):
        with open(input_file, 'r') as f:
            data = json.load(f)
        state_dict = deepcopy(data)

        self.__size = state_dict['size']
        self.__maze = state_dict['maze']
        self.__wormholes= state_dict['wormholes']
        self.__treasure = state_dict['treasure']
        self.__exit = state_dict['exit']
        self.__walls = state_dict['walls']
        self.__current = state_dict['current']
        self.__found_treasure = state_dict['found_treasure']


class LabyrinthGenerator(ILabyrinthGenerator):
    def __init__(self, size, wall_rate=0.5, sequence_length=5):
        self.__size = size
        self.wall_rate = wall_rate
        self.sequence_length = sequence_length
    
    def random_border_cell(self):
        min_ = 0
        max_ = self.__size-1

        if random.random() >= 0.5:
            row = random.choice([min_, max_])
            col = random.randint(min_, max_)
        else:
            row = random.randint(min_, max_)
            col = random.choice([min_, max_])

        return (row, col)

    def random_cell(self):
        return tuple(random.choices(range(self.__size), k=2))

    def random_sequence_of_cells(self):
        return tuple(self.random_cell() for i in range(self.sequence_length))

    def random_walls(self):
        random_walls = []
        N = int(self.__size*self.__size*self.wall_rate)

        for i in range(N):
            random_wall = tuple([
                self.random_cell(),
                random.choice(['top', 'bottom', 'left', 'right'])
            ])
            random_walls.append(random_wall)
            
            (row, col), wall_type = random_wall
            matching_wall = get_matching_wall(row, col, wall_type)
            (new_row, new_col), new_wall_type = matching_wall

            if is_between(new_row, 0, self.__size-1) and is_between(new_col, 0, self.__size-1):
                random_walls.append(matching_wall)

        random_walls = list(set(random_walls))
        return random_walls





    