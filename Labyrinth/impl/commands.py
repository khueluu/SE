import sys

from services.command import IUserCommand
from impl.objects import Labyrinth

class GoUp(IUserCommand):
    def get_command_tag(self):
        return 'up'
    
    def get_args_count(self):
        return 0

    def __call__(self, lbr): 
        row, col = lbr.current_cell
        wall = lbr[row][col].walls['top_wall']
        print("Before", lbr.current_cell)
        if wall is not None:
            print(f"Step impossible, {wall}")
            print("After", lbr.current_cell)
        else:
            lbr[row][col].is_current = False
            lbr[row-1][col].is_current = True
            lbr.current_cell = (row-1, col)
            print("After", lbr.current_cell)
        return lbr


class GoDown(IUserCommand):
    def get_command_tag(self):
        return 'down'

    def get_args_count(self):
        return 0

    def __call__(self, lbr):
        row, col = lbr.current_cell
        wall = lbr[row][col].walls['bottom_wall']
        print("Before", lbr.current_cell)
        if wall is not None:
            print(f"Step impossible, {wall}")
            print("After", lbr.current_cell)
        else:
            lbr[row][col].is_current = False
            lbr[row+1][col].is_current = True
            lbr.current_cell = (row+1, col)
            print("After", lbr.current_cell)
        return lbr


class GoLeft(IUserCommand):
    def get_command_tag(self):
        return 'left'

    def get_args_count(self):
        return 0

    def __call__(self, lbr):
        row, col = lbr.current_cell
        wall = lbr[row][col].walls['left_wall']
        print("Before", lbr.current_cell)
        if wall is not None:
            print(f"Step impossible, {wall}")
            print("After", lbr.current_cell)
        else:
            lbr[row][col].is_current = False
            lbr[row][col-1].is_current = True
            lbr.current_cell = (row, col-1)
            print("After", lbr.current_cell)
        return lbr


class GoRight(IUserCommand):
    def get_command_tag(self):
        return 'right'

    def get_args_count(self):
        return 0

    def __call__(self, lbr):
        row, col = lbr.current_cell
        wall = lbr[row][col].walls['right_wall']
        print("Before", lbr.current_cell)
        if wall is not None:
            print(f"Step impossible, {wall}")
            print("After", lbr.current_cell)
        else:
            lbr[row][col].is_current = False
            lbr[row][col+1].is_current = True
            lbr.current_cell = (row, col+1)
            print("After", lbr.current_cell)
        return lbr


class Skip(IUserCommand):
    def get_command_tag(self):
        return 'skip'

    def get_args_count(self):
        return 0

    def __call__(self, lbr):
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
        print(f'Saved to {output_file} and quit')
        sys.exit()
