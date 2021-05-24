import random

from services.generator import IGenerator
from utils import get_matching_wall, is_between

random.seed(0)

class Generator(IGenerator):
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
