import random
import json
from copy import deepcopy

from services.object import IObject
random.seed(0)

class Cell(IObject):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {
            "top_wall": None,
            "bottom_wall": None,
            "left_wall": None,
            "right_wall": None
        }
        self.treasure = False
        self.wormhole_idx = -1
        self.is_current = False

    def __str__(self):
        return f"""
            'row: {self.row},
            'col': {self.col},
            'walls': {self.walls},
            'treasure': {self.treasure},
            'wormhole': {self.wormhole_idx},
            'is_current:' {self.is_current}
        """
        

class Labyrinth(IObject):
    def create_new(self, size):
        self.size = int(size)
        self.found_treasure = False
        self.maze = self.create_maze(self.size)
        self.monoliths = self.set_monolith()
        self.exit_cell = self.set_exit()
        self.treasure_cell = self.set_treasure()
        self.walls = self.set_walls()
        self.wormholes_cells = self.set_wormholes()
        self.current_cell = self.set_initial_cell()


    def load(self, input_file):
        with open(input_file, 'r') as f:
            state_dict = json.load(f)

        self.size = state_dict['size']
        self.maze = self.create_maze(self.size)
        self.monoliths = self.set_monolith()
        self.wormholes_cells = state_dict['wormhole_cells']
        self.treasure_cell = state_dict['treasure_cell']
        self.exit_cell = state_dict['exit_cell']
        self.walls = state_dict['walls']
        self.current_cell = state_dict['current_cell']
        self.found_treasure = state_dict['found_treasure']
        
    def __str__(self):
        return f"""
        <Labyrinth object of size ({self.size}x{self.size})>
        'wormholes': {self.wormholes_cells}
        'treasure': {self.treasure_cell}
        'exit': {self.exit_cell}
        'walls': {self.walls}
        'current': {self.current_cell}
        'found_treasure': {self.found_treasure}
        """

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
                if row == self.size-1:
                    self.maze[row][col].walls["bottom_wall"] = 'monolith'
                    monoliths.append((row, col, 'bottom_wall'))
                if col == 0:
                    self.maze[row][col].walls["left_wall"] = 'monolith'
                    monoliths.append((row, col, 'left_wall'))
                if col == self.size-1:
                    self.maze[row][col].walls["right_wall"] = 'monolith'
                    monoliths.append((row, col, 'right_wall'))
        return monoliths

    def set_exit(self):
        row, col, wall = random.choice(self.monoliths)
        self.maze[row][col].walls[wall] = 'exit'
        return (row, col)

    def set_treasure(self):
        row, col = random.sample(range(self.size), k=2)
        self.maze[row][col].treasure = True
        return (row, col)

    def match_walls_between_two_cells(self, row, col, wall):
        if wall == 'top_wall':
            self.maze[row-1][col].walls['bottom_wall'] = 'wall'
        if wall == 'bottom_wall':
            self.maze[row+1][col].walls['top_wall'] = 'wall'
        if wall == 'left_wall':
            self.maze[row][col-1].walls['right_wall'] = 'wall'
        if wall == 'right_wall':
            self.maze[row][col+1].walls['left_wall'] = 'wall'
        

    def set_walls(self):
        min_ = 2
        wall_coords = []
        for row in range(0, self.size, 2):
            for col in range(self.size):
                walls = self.maze[row][col].walls
                available_walls_num = len([v for v in walls.values() if v is None])

                for wall, value in walls.items():
                    if (value is None) and (random.random() >= 0.8) and (available_walls_num > min_):
                        self.maze[row][col].walls[wall] = 'wall'
                        wall_coords.append((row, col, wall))
                        self.match_walls_between_two_cells(row, col, wall)
                        available_walls_num -= 1
        return wall_coords

    def set_initial_cell(self):
        row, col = random.sample(range(self.size), k=2)
        self.maze[row][col].is_current = True
        return (row, col)


    def set_wormholes(self):
        wormholes_cells = []

        while len(wormholes_cells) < 5:
            wh_cell = random.sample(range(self.size), k=2)
            if wh_cell not in wormholes_cells:
                wormholes_cells.append(wh_cell)

        for idx, (row, col) in enumerate(wormholes_cells):
            self.maze[row][col].wormhole_idx = idx
        
        return wormholes_cells

    def get_current_cell(self):
        row, col = self.current_cell
        return self.maze[row][col]

    def save(self, output_file='labyrinth.txt'):
        state_dict = {
            'size': self.size,
            'wormhole_cells': self.wormholes_cells,
            'treasure_cell': self.treasure_cell,
            'exit_cell': self.exit_cell,
            'walls': self.walls,
            'current_cell': self.current_cell,
            'found_treasure': self.found_treasure
        }

        with open(output_file, 'w') as f:
            f.write(json.dumps(state_dict))


