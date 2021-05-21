import sys

from services.command import IUserCommand
from impl.objects import Labyrinth
from impl.controller import move, move_through_wormhole

class GoUp(IUserCommand):
    def get_command_tag(self):
        return 'up'
    
    def get_args_count(self):
        return 0

    def __call__(self, lbr): 
        lbr = move(lbr, 'up')
        return lbr


class GoDown(IUserCommand):
    def get_command_tag(self):
        return 'down'

    def get_args_count(self):
        return 0

    def __call__(self, lbr):
        lbr = move(lbr, 'down')
        return lbr


class GoLeft(IUserCommand):
    def get_command_tag(self):
        return 'left'

    def get_args_count(self):
        return 0

    def __call__(self, lbr):
        lbr = move(lbr, 'left')
        return lbr


class GoRight(IUserCommand):
    def get_command_tag(self):
        return 'right'

    def get_args_count(self):
        return 0

    def __call__(self, lbr):
        lbr = move(lbr, 'right')
        return lbr


class Skip(IUserCommand):
    def get_command_tag(self):
        return 'skip'

    def get_args_count(self):
        return 0

    def __call__(self, lbr):
        current_cell = lbr.get_current_cell()
        current_wormhole_idx = current_cell.wormhole_idx
        if current_wormhole_idx >=0:
            lbr = move_through_wormhole(lbr)
        else:
            print('Step skipped')
        return lbr


class Quit(IUserCommand):
    def get_command_tag(self):
        return 'quit'

    def get_args_count(self):
        return 0

    def __call__(self, lbr):
        sys.exit('Quit game without saving')
    

class Save(IUserCommand):
    def get_command_tag(self):
        return 'save'

    def get_args_count(self):
        return 1

    def __call__(self, lbr, output_file='labyrinth.txt'): 
        lbr.save(output_file)
        print(f'Saved to {output_file} and quit')
        sys.exit()


class Load(IUserCommand):
    def get_command_tag(self):
        return 'load'

    def get_args_count(self):
        return 1

    def __call__(self, lbr, input_file):
        lbr.load(input_file)
        return lbr