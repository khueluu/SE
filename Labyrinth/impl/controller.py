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

    def get_msg_for_impossible_step(self, wall_type):
        msg = ''
        if wall_type == 'exit':
            exit_messages = messages['step_impossible']['exit']
            msg = exit_messages['found_treasure'] if self.lbr.found_treasure else exit_messages['not_found_treasure']
        else:
            msg = messages['step_impossible'][wall_type]
        return msg

    def get_msg_for_possible_step(self, is_treasure, is_wormhole):
        msg = ''
        if is_treasure and is_wormhole:
            msg = messages['step_possible']['treasure_and_wormhole']
        elif is_treasure:
            msg = messages['step_possible']['treasure']
        elif is_wormhole:
            msg = messages['step_possible']['wormhole']
        else:
            msg = messages['step_possible']['normal']
        return msg

    def is_treasure(self, cell):
        if not self.lbr.treasure:
            return False
        return is_same_cell(cell, self.lbr.treasure)

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

    def move(self, direction: str):
        current = self.lbr.get_current()
        mapper = movement_mapper[direction]
        wall_type = mapper['wall_to_check']
        checking_wall = current['walls'][wall_type]

        if checking_wall is not None:
            msg = self.get_msg_for_impossible_step(checking_wall)
            print(msg)
            if msg == 'Step executed, exit. YOU WIN!':
                sys.exit()
        else:
            # Move current cell to new cell
            row, col = current['position']
            new_row = row + mapper['row_change']
            new_col = col + mapper['col_change']
            self.lbr.set_current(new_row, new_col)

            # Check collectables of new cell
            new_cell = (new_row, new_col)
            is_treasure = self.is_treasure(new_cell)
            is_wormhole = self.is_wormhole(new_cell)
            
            msg = self.get_msg_for_possible_step(is_treasure, is_wormhole)
            print(msg)

            if is_treasure:
                self.lbr.found_treasure = True
                self.lbr.treasure = None
            if is_wormhole:
                self.move_through_wormhole(new_cell)

    def move_through_wormhole(self, cell):
        wormhole_idx = self.get_wormhole_idx(cell)
        next_wormhole = self.get_next_wormhole(wormhole_idx)
        self.lbr.set_current(next_wormhole[0], next_wormhole[1])

    def skip(self):
        current_cell = self.lbr.current
        if self.is_wormhole(current_cell):
            msg = messages['skip']['wormhole']
            self.move_through_wormhole(current_cell)
        else:
            msg = messages['skip']['normal']
        print(msg)
            
