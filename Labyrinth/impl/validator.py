from services.validator import IValidator
from services.labyrinth import ILabyrinth
from helpers import is_between, check_duplicated_position, check_duplicated_wall_data, get_matching_wall

class Validator(IValidator):
    def validate(self, labyrinth: ILabyrinth, return_invalid: bool=False):
        validities = {
            'cells': self.validate_cells(labyrinth),
            'walls': self.validate_walls(labyrinth),
            'wormholes': self.validate_wormholes(labyrinth),
            'monolith': self.validate_monolith(labyrinth),
            'exit': self.validate_exit(labyrinth),
            'treasure': self.is_valid_position(
                position=labyrinth.treasure,
                lbr_size=labyrinth.size),
            'current': self.is_valid_position(
                position=labyrinth.current,
                lbr_size=labyrinth.size)
        }

        invalid_objects = [obj for obj, is_valid in validities.items() if not is_valid]
        is_valid_labyrinth = len(invalid_objects) == 0
        return (is_valid_labyrinth, invalid_objects) if return_invalid else is_valid_labyrinth

    def validate_cells(self, labyrinth: ILabyrinth):
        N = labyrinth.size
        valid_cells = []

        for row in range(N):
            for col in range(N):
                cell = labyrinth[row][col]
                is_valid_cell = self.validate_one_cell(cell=cell, lbr_size=N)
                valid_cells.append(is_valid_cell)

        is_all_cells_valid = all(valid_cells)
        return is_all_cells_valid
    
    def validate_one_cell(self, cell: tuple, lbr_size: int):
        is_opened_cell = self.is_opened_cell(cell)
        is_valid_position = self.is_valid_position(
            position=cell.position,
            lbr_size=lbr_size)
        return is_opened_cell and is_valid_position

    def is_opened_cell(self, cell: tuple):
        num_wall = 0
        cell_wall_list = cell.walls.values()
        for wall in cell_wall_list:
            if wall is not None: num_wall += 1
        return num_wall < 4

    def is_valid_position(self, position: tuple, lbr_size: int):
        row, col = position
        is_valid_row = is_between(row, 0, lbr_size-1)
        is_valid_col = is_between(col, 0, lbr_size-1)
        return is_valid_row and is_valid_col

    def validate_walls(self, labyrinth: ILabyrinth):
        is_duplicated = check_duplicated_wall_data(labyrinth.walls)
        return (not is_duplicated)

    def validate_wormholes(self, labyrinth):
        is_duplicated = check_duplicated_position(labyrinth.wormholes)
        return (not is_duplicated)

    def validate_monolith(self, labyrinth: ILabyrinth):
        N = labyrinth.size
        for row in range(N):
            for col in range(N):
                cell = labyrinth[row][col]
                cell_wall_dict = cell.walls
                if (row == 0) and (cell_wall_dict['top'] not in ['monolith', 'exit']):
                    return False
                if (row == N-1) and (cell_wall_dict['bottom'] not in ['monolith', 'exit']):
                    return False
                if (col == 0) and (cell_wall_dict['left'] not in ['monolith', 'exit']):
                    return False
                if (col == N-1) and (cell_wall_dict['right'] not in ['monolith', 'exit']):
                    return False
        return True

    def validate_exit(self, labyrinth: ILabyrinth):
        if not labyrinth.exit:
            return False

        exit_count = 0
        N = labyrinth.size

        for row in range(N):
            for col in range(N):
                cell = labyrinth[row][col]
                cell_wall_list = cell.walls.values()
                if 'exit' in cell_wall_list:
                    exit_count += 1
        return exit_count == 1
        