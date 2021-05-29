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
        if self.__lbr.found_treasure:
            print(messages['win'])
            sys.exit()
    
    def get_directing_wall(self, cell: tuple, direction: str):
        mapper = movement_mapper[direction]
        wall_type = mapper['wall_to_check']
        row, col = cell
        cell_wall_dict = self.__lbr[row][col].walls
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
        self.__lbr.current = new_cell
        print(messages['step_possible'])
        
        return new_cell

    def do_step_possible(self, cell: tuple, direction: str):
        new_cell = self.move_cell(cell, direction)
        self.check_treasure(new_cell)
        self.check_wormhole(new_cell)


    # Treasure
    def is_treasure(self, cell: tuple):
        treasure = self.__lbr.treasure
        return False if not treasure else is_same_cell(cell, treasure)
    
    def check_treasure(self, cell: tuple):
        if self.is_treasure(cell):
            print(messages['objects']['treasure'])
            self.__lbr.do_found_treasure()


    # Wormhole
    def is_wormhole(self, cell: tuple):
        wormholes = self.__lbr.wormholes
        for wormhole in wormholes:
            if is_same_cell(cell, wormhole):
                return True
        return False

    def get_wormhole_idx(self, cell: tuple):
        wormholes = self.__lbr.wormholes
        for idx, wormhole in enumerate(wormholes):
            if is_same_cell(cell, wormhole):
                return idx

    def get_next_wormhole(self, current_idx: int):
        wormholes = self.__lbr.wormholes
        wormholes_len = len(wormholes)
        next_idx = get_next_idx_of_seq(current_idx, wormholes_len)
        return wormholes[next_idx]

    def move_through_wormhole(self, cell: tuple):
        current_idx = self.get_wormhole_idx(cell)
        next_wormhole = self.get_next_wormhole(current_idx)
        
        self.__lbr.current = next_wormhole
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
        current_cell = self.__lbr.current
        directing_wall = self.get_directing_wall(current_cell, direction)

        if directing_wall:
            self.do_step_impossible(directing_wall)
        else:
            self.do_step_possible(current_cell, direction)

    def skip(self):
        print(messages['skip'])
        current_cell = self.__lbr.current
        self.check_wormhole(current_cell, verbose=False)

    def get_labyrinth(self):
        return deepcopy(self.__lbr)
    

class Saver(IInputOutput):
    def __init__(self, lbr: ILabyrinth):
        self.__lbr = lbr

    def __call__(self, filepath: str):
        state_dict = {
            'size': self.__lbr.size,
            'maze': self.__lbr.maze,
            'wormholes': self.__lbr.wormholes,
            'treasure': self.__lbr.treasure,
            'exit': self.__lbr.exit,
            'walls': self.__lbr.walls,
            'current': self.__lbr.current,
            'found_treasure': self.__lbr.found_treasure
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

        self.__lbr.size = state_dict['size']
        self.__lbr.maze = state_dict['maze']
        self.__lbr.wormholes = state_dict['wormholes']
        self.__lbr.treasure = state_dict['treasure']
        self.__lbr.exit = state_dict['exit']
        self.__lbr.walls = state_dict['walls']
        self.__lbr.current = state_dict['current']
        self.__lbr.found_treasure = state_dict['found_treasure']

        lbr_val = Validator()
        is_valid_labyrinth, invalid_objects = lbr_val.validate(self.__lbr, return_invalid=True)
        
        if not is_valid_labyrinth:
            print(f'These Labyrinth values are invalid: {invalid_objects}')
            sys.exit()

        return deepcopy(self.__lbr)

