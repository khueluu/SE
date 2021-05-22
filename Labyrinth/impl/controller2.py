import sys
from services.labyrinth import ILabyrinth
from services.controller import IController
from config import movement_mapper, messages
from utils import is_same_cell, get_next_idx_of_seq


class Controller(IController):
    def __init__(self, labyrinth: ILabyrinth):
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
                wormhole_idx = self.get_wormhole_idx(new_cell)
                next_wormhole = self.get_next_wormhole(wormhole_idx)
                self.lbr.set_current(next_wormhole[0], next_wormhole[1])
            
