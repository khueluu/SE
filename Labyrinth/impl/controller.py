import sys
from services.controller import IController
from mapper import *

def is_same_cell(cell_1, cell_2):
    return (cell_1[0] == cell_2[0]) and (cell_1[1] == cell_2[1])

def get_next_idx_of_seq(idx, seq_length):
    next_idx = idx + 1
    return next_idx if next_idx < seq_length else 0


class Controller(IController):
    def __init__(self, labyrinth):
        self.lbr = labyrinth


    # Helpers
    def check_exit(self):
        if self.lbr.found_treasure:
            print(messages['win'])
            sys.exit()
    
    def get_directing_wall(self, cell, direction):
        mapper = movement_mapper[direction]
        wall_type = mapper['wall_to_check']
        row, col = cell
        current = self.lbr[row][col]
        return current['walls'][wall_type]
    
    def do_step_impossible(self, wall_type):
        if wall_type == 'exit':
            self.check_exit()
        print(messages['step_impossible'][wall_type])

    def move_cell(self, cell, direction):
        mapper = movement_mapper[direction]
        row, col = cell
        new_row = row + mapper['row_change']
        new_col = col + mapper['col_change']
        self.lbr.set_current(new_row, new_col)
        print(messages['step_possible'])
        new_cell = (new_row, new_col)
        return new_cell

    def do_step_possible(self, cell, direction):
        new_cell = self.move_cell(cell, direction)
        self.check_treasure(new_cell)
        self.check_wormhole(new_cell)


    # Treasure
    def is_treasure(self, cell):
        if not self.lbr.treasure:
            return False
        return is_same_cell(cell, self.lbr.treasure)
    
    def check_treasure(self, cell):
        if self.is_treasure(cell):
            print(messages['objects']['treasure'])
            self.lbr.found_treasure = True
            self.lbr.treasure = None


    # Wormhole
    def is_wormhole(self, cell):
        for wormhole in self.lbr.wormholes:
            if is_same_cell(cell, wormhole):
                return True
        return False

    def get_wormhole_idx(self, cell):
        for idx, wormhole in enumerate(self.lbr.wormholes):
            if is_same_cell(cell, wormhole):
                return idx

    def get_next_wormhole(self, current_idx):
        wormholes_len = len(self.lbr.wormholes)
        next_idx = get_next_idx_of_seq(current_idx, wormholes_len)
        return self.lbr.wormholes[next_idx]

    def move_through_wormhole(self, cell):
        wormhole_idx = self.get_wormhole_idx(cell)
        next_wormhole = self.get_next_wormhole(wormhole_idx)
        
        self.lbr.set_current(next_wormhole[0], next_wormhole[1])
        print(messages['objects']['wormhole_next'])

        self.check_treasure(next_wormhole)

    def check_wormhole(self, cell, verbose=True):
        if self.is_wormhole(cell):
            if verbose:
                print(messages['objects']['wormhole'])
            self.move_through_wormhole(cell)


    # Actions
    def move(self, direction: str):
        mapper = movement_mapper[direction]
        current_cell = self.lbr.current
        directing_wall = self.get_directing_wall(current_cell, direction)

        if directing_wall:
            self.do_step_impossible(directing_wall)
        else:
            self.do_step_possible(current_cell, direction)

    def skip(self):
        current_cell = self.lbr.current
        print(messages['skip'])
        self.check_wormhole(current_cell, verbose=False)
            
