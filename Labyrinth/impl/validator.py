from services.validator import IValidator
from services.labyrinth import ILabyrinth
from helpers import is_between, check_duplicated_position, check_duplicated_wall_data, get_matching_wall

class Validator(IValidator):
    def validate(self, labyrinth: ILabyrinth):
        valid_cells = self.validate_cells(labyrinth)
        valid_walls = self.validate_walls(labyrinth)
        valid_wormholes = self.validate_wormholes(labyrinth)
        valid_monolith = self.validate_monolith(labyrinth)
        valid_exit = self.validate_exit(labyrinth)

        return (valid_cells and valid_walls and valid_wormholes and valid_monolith and valid_exit)

    def validate_cells(self, labyrinth: ILabyrinth):
        N = labyrinth.get_size()
        for row in range(N):
            for col in range(N):
                valid_cell = self.validate_one_cell(labyrinth[row][col])
                if not valid_cell:
                    return False
        return True
    
    def validate_one_cell(self, cell):
        num_wall = 0
        cell_wall_list = cell.get_walls().values()
        for wall in cell_wall_list:
            if wall is not None:
                num_wall += 1
        return num_wall < 4

    def validate_walls(self, labyrinth: ILabyrinth):
        walls = labyrinth.get_walls()
        N = labyrinth.get_size()

        for wall in walls:
            (row, col), wall_position = wall
            if (not is_between(row, 0, N)) or (not is_between(col, 0, N)):
                return False

        is_duplicated = check_duplicated_wall_data(walls)
        return (not is_duplicated)

    def validate_wormholes(self, labyrinth):
        wormholes = labyrinth.get_wormholes()
        is_duplicated = check_duplicated_position(wormholes)
        return (not is_duplicated)

    def validate_monolith(self, labyrinth):
        N = labyrinth.get_size()
        for row in range(N):
            for col in range(N):
                cell = labyrinth[row][col]
                cell_wall_dict = cell.get_walls()
                if (row == 0) and (cell_wall_dict['top'] not in ['monolith', 'exit']):
                    return False
                if (row == N-1) and (cell_wall_dict['bottom'] not in ['monolith', 'exit']):
                    return False
                if (col == 0) and (cell_wall_dict['left'] not in ['monolith', 'exit']):
                    return False
                if (col == N-1) and (cell_wall_dict['right'] not in ['monolith', 'exit']):
                    return False
        return True

    def validate_exit(self, labyrinth):
        if not labyrinth.get_exit():
            return False

        exit_count = 0
        N = labyrinth.get_size()
        for row in range(N):
            for col in range(N):
                cell = labyrinth[row][col]
                cell_wall_list = cell.get_walls().values()
                if 'exit' in cell_wall_list:
                    exit_count += 1
        return exit_count == 1
        