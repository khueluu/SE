import sys
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from copy import deepcopy

from services.controller import IController, IInputOutput
from services.labyrinth import ILabyrinth
from impl.validator import Validator
from helpers import is_same_cell, get_next_idx_of_seq, validate_schema
from mapper import *


class Controller(IController):
    def __init__(self, labyrinth: ILabyrinth):
        self.__lbr = labyrinth

    # Helpers
    def check_exit(self):
        if self.__lbr.get_found_treasure():
            print(messages['win'])
            sys.exit()
    
    def get_directing_wall(self, cell: tuple, direction: str):
        mapper = movement_mapper[direction]
        wall_type = mapper['wall_to_check']
        row, col = cell
        cell_wall_dict = self.__lbr[row][col].get_walls()
        return cell_wall_dict[wall_type]
    
    def do_step_impossible(self, wall_type: str):
        if wall_type == 'exit':
            self.check_exit()
        print(messages['step_impossible'][wall_type])

    def move_cell(self, cell: tuple, direction: str):
        mapper = movement_mapper[direction]
        row, col = cell
        new_row = row + mapper['row_change']
        new_col = col + mapper['col_change']
        new_cell = (new_row, new_col)
        self.__lbr.set_current(new_cell)
        print(messages['step_possible'])
        
        return new_cell

    def do_step_possible(self, cell: tuple, direction: str):
        new_cell = self.move_cell(cell, direction)
        self.check_treasure(new_cell)
        self.check_wormhole(new_cell)


    # Treasure
    def is_treasure(self, cell: tuple):
        treasure = self.__lbr.get_treasure()
        if not treasure:
            return False
        return is_same_cell(cell, treasure)
    
    def check_treasure(self, cell: tuple):
        if self.is_treasure(cell):
            print(messages['objects']['treasure'])
            self.__lbr.do_found_treasure()


    # Wormhole
    def is_wormhole(self, cell: tuple):
        wormholes = self.__lbr.get_wormholes()
        for wormhole in wormholes:
            if is_same_cell(cell, wormhole):
                return True
        return False

    def get_wormhole_idx(self, cell: tuple):
        wormholes = self.__lbr.get_wormholes()
        for idx, wormhole in enumerate(wormholes):
            if is_same_cell(cell, wormhole):
                return idx

    def get_next_wormhole(self, current_idx: int):
        wormholes = self.__lbr.get_wormholes()
        wormholes_len = len(wormholes)
        next_idx = get_next_idx_of_seq(current_idx, wormholes_len)
        return self.__lbr.get_wormhole_by_idx(idx=next_idx)

    def move_through_wormhole(self, cell: tuple):
        current_idx = self.get_wormhole_idx(cell)
        next_wormhole = self.get_next_wormhole(current_idx)
        
        self.__lbr.set_current(next_wormhole)
        print(messages['objects']['wormhole_next'])

        self.check_treasure(next_wormhole)

    def check_wormhole(self, cell: tuple, verbose=True):
        if self.is_wormhole(cell):
            if verbose:
                print(messages['objects']['wormhole'])
            self.move_through_wormhole(cell)


    # Actions
    def move(self, direction: str):
        mapper = movement_mapper[direction]
        current_cell = self.__lbr.get_current()
        directing_wall = self.get_directing_wall(current_cell, direction)

        if directing_wall:
            self.do_step_impossible(directing_wall)
        else:
            self.do_step_possible(current_cell, direction)

    def skip(self):
        print(messages['skip'])
        current_cell = self.__lbr.get_current()
        self.check_wormhole(current_cell, verbose=False)

    def get_labyrinth(self):
        return deepcopy(self.__lbr)
    

class Saver(IInputOutput):
    def __init__(self, lbr: ILabyrinth):
        self.__lbr = lbr

    def __call__(self, filepath: str):
        state_dict = {
            'size': self.__lbr.get_size(),
            'maze': self.__lbr.get_maze(),
            'wormholes': self.__lbr.get_wormholes(),
            'treasure': self.__lbr.get_treasure(),
            'exit': self.__lbr.get_exit(),
            'walls': self.__lbr.get_walls(),
            'current': self.__lbr.get_current(),
            'found_treasure': self.__lbr.get_found_treasure()
        }

        with open(filepath, 'w') as f:
            f.write(json.dumps(state_dict))


class Loader(IInputOutput):
    def __init__(self, lbr: ILabyrinth):
        self.__lbr = lbr

    def __call__(self, filepath: str):
        with open(filepath, 'r') as f:
            state_dict = json.load(f)

        try:
            validate_schema(state_dict)
        except ValidationError as err:
            print(f'Schema validation error: {err.message}')
            sys.exit()

        self.__lbr.set_size(state_dict['size'])
        self.__lbr.set_maze_from_data(state_dict['maze'])
        self.__lbr.set_wormholes(state_dict['wormholes'])
        self.__lbr.set_treasure(state_dict['treasure'])
        self.__lbr.set_exit(state_dict['exit'])
        self.__lbr.set_walls(state_dict['walls'])
        self.__lbr.set_current(state_dict['current'])
        self.__lbr.set_found_treasure(state_dict['found_treasure'])

        return deepcopy(self.__lbr)

