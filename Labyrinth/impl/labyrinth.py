import random
import json
from copy import deepcopy

from services.labyrinth import ILabyrinth, ILabyrinthGenerator
from utils import is_between, get_matching_wall

class Labyrinth(ILabyrinth):
    def __init__(self):
        self.size = None
        self.maze = None
        self.current = None
        self.exit = None
        self.treasure = None
        self.found_treasure = False
        self.wormholes = None
        self.generator = None
        self.walls = None

    def __getitem__(self, idx):
        if self.maze:
            return self.maze[idx]
        else:
            return 'Labyrinth has not been created or loaded.'

    def __str__(self):
        return f"""
        'size': ({self.size}, {self.size})
        'wormholes': {self.wormholes}
        'treasure': {self.treasure}
        'exit': {self.exit}
        'walls': {self.walls}
        'current': {self.current}
        'found_treasure': {self.found_treasure}
        """

    def create(self, size: int, generator: ILabyrinthGenerator):
        self.size = size
        self.generator = generator

        self.maze = self.create_maze(size)
        self.exit = self.generator.random_border_cell()
        self.current = self.generator.random_cell()
        self.treasure = self.generator.random_cell()
        self.wormholes = self.generator.random_sequence_of_cells()
        self.walls = self.generator.random_walls()

        self.set_walls_to_maze()

    def set_walls_to_maze(self):
        for wall_data in self.walls:
            (row, col), wall_type = wall_data
            self.maze[row][col]['walls'][wall_type] = 'wall'

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
                cell = {
                    'position': (row, col),
                    'walls': walls,
                }
                maze_row.append(cell)
            maze.append(maze_row)
        return deepcopy(maze)

    def get_current(self):
        row, col = self.current
        return self.maze[row][col]

    def set_current(self, row, col):
        self.current = (row, col)

    def save(self, output_file='labyrinth.txt'):
        state_dict = {
            'size': self.size,
            'maze': self.maze,
            'wormholes': self.wormholes,
            'treasure': self.treasure,
            'exit': self.exit,
            'walls': self.walls,
            'current': self.current,
            'found_treasure': self.found_treasure
        }

        with open(output_file, 'w') as f:
            f.write(json.dumps(state_dict))

    def load(self, input_file):
        with open(input_file, 'r') as f:
            data = json.load(f)
        state_dict = deepcopy(data)

        self.size = state_dict['size']
        self.maze = state_dict['maze']
        self.wormholes= state_dict['wormholes']
        self.treasure = state_dict['treasure']
        self.exit = state_dict['exit']
        self.walls = state_dict['walls']
        self.current = state_dict['current']
        self.found_treasure = state_dict['found_treasure']



class LabyrinthGenerator(ILabyrinthGenerator):
    def __init__(self, size, wall_rate=0.5, sequence_length=5):
        self.size = size
        self.wall_rate = wall_rate
        self.sequence_length = sequence_length
    
    def random_border_cell(self):
        min_ = 0
        max_ = self.size-1

        if random.random() >= 0.5:
            row = random.choice([min_, max_])
            col = random.randint(min_, max_)
        else:
            row = random.randint(min_, max_)
            col = random.choice([min_, max_])

        return (row, col)

    def random_cell(self):
        return tuple(random.choices(range(self.size), k=2))

    def random_sequence_of_cells(self):
        return tuple(self.random_cell() for i in range(self.sequence_length))

    def random_walls(self):
        random_walls = []
        N = int(self.size*self.size*self.wall_rate)

        for i in range(N):
            random_wall = tuple([
                self.random_cell(),
                random.choice(['top', 'bottom', 'left', 'right'])
            ])
            random_walls.append(random_wall)
            
            (row, col), wall_type = random_wall
            matching_wall = get_matching_wall(row, col, wall_type)
            (new_row, new_col), new_wall_type = matching_wall
            if is_between(new_row, 0, self.size-1) and is_between(new_col, 0, self.size-1):
                random_walls.append(matching_wall)

        return random_walls





    