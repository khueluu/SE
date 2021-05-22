from services.validator import IValidator
from services.labyrinth import ILabyrinth
from utils import is_between, get_duplicate, get_matching_wall

class Validator(IValidator):
    def validate(self, labyrinth: ILabyrinth):
        valid_cells = self.validate_cells(labyrinth)
        valid_walls = self.validate_walls(labyrinth)
        valid_wormholes = self.validate_wormholes(labyrinth)
        valid_monolith = self.validate_monolith(labyrinth)
        return (valid_cells and valid_walls and valid_wormholes and valid_monolith)

    def validate_cells(self, labyrinth: ILabyrinth):
        N = labyrinth.size
        for row in range(N):
            for col in range(N):
                valid_cell = self.validate_one_cell(labyrinth[row][col])
                if not valid_cell:
                    return False
        return True
    
    def validate_one_cell(self, cell):
        num_wall = 0
        walls = cell['walls']
        for key, value in walls.items():
            if value is not None:
                num_wall += 1
        return num_wall < 4

    def validate_walls(self, labyrinth: ILabyrinth):
        walls = labyrinth.walls
        N = labyrinth.size
        for wall in walls:
            (row, col), wall_position = wall
            if (not is_between(row, 0, N)) or (not is_between(col, 0, N)):
                return False
        duplicated = get_duplicate(walls)
        if duplicated: return False
        return True

    def validate_wormholes(self, labyrinth):
        wormholes = labyrinth.wormholes
        duplicated = get_duplicate(wormholes)
        return (not duplicated)

    def validate_monolith(self, labyrinth):
        N = labyrinth.size
        for row in range(N):
            for col in range(N):
                cell = labyrinth[row][col]
                walls = cell['walls']
                if (row == 0) and (walls['top'] not in ['monolith', 'exit']):
                    return False
                if (row == N-1) and (walls['bottom'] not in ['monolith', 'exit']):
                    return False
                if (col == 0) and (walls['left'] not in ['monolith', 'exit']):
                    return False
                if (col == N-1) and (walls['right'] not in ['monolith', 'exit']):
                    return False
        return True



