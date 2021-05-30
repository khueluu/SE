import sys

from services.command import IUserCommand
from services.labyrinth import ILabyrinth
from impl.controller import Controller, Saver, Loader

class Go(IUserCommand):
    def get_command_tag(self):
        return 'go'
    
    def get_args_count(self):
        return 0

    def __call__(self, lbr: ILabyrinth):
        controller = Controller(lbr)
        controller.move(self.get_command_tag())
        return controller.get_labyrinth()


class GoUp(Go):
    def __init__(self):
        super().__init__()
        
    def get_command_tag(self):
        return 'up'


class GoDown(Go):
    def __init__(self):
        super().__init__()

    def get_command_tag(self):
        return 'down'


class GoLeft(Go):
    def __init__(self):
        super().__init__()

    def get_command_tag(self):
        return 'left'


class GoRight(Go):
    def __init__(self):
        super().__init__()

    def get_command_tag(self):
        return 'right'


class Skip(IUserCommand):
    def get_command_tag(self):
        return 'skip'

    def get_args_count(self):
        return 0

    def __call__(self, lbr: ILabyrinth):
        controller = Controller(lbr)
        controller.skip()
        return controller.get_labyrinth()


class Quit(IUserCommand):
    def get_command_tag(self):
        return 'quit'

    def get_args_count(self):
        return 0

    def __call__(self, lbr: ILabyrinth):
        sys.exit('Quit game without saving')


class Save(IUserCommand):
    def get_command_tag(self):
        return 'save'

    def get_args_count(self):
        return 1

    def __call__(self, lbr: ILabyrinth, output_file='labyrinth.txt'): 
        saver = Saver(lbr)
        saver(output_file)
        print(f'Saved to {output_file} and quit')
        sys.exit()


class Load(IUserCommand):
    def get_command_tag(self):
        return 'load'

    def get_args_count(self):
        return 1

    def __call__(self, lbr: ILabyrinth, input_file: str):
        loader = Loader(lbr)
        new_lbr = loader(input_file)
        print(f"Loaded labyrinth of size {new_lbr.size}x{new_lbr.size}")
        return new_lbr