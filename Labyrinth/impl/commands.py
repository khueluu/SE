from services.command import IUserCommand

class GoUp(IUserCommand):
    def get_command_tag(self):
        return 'up'
    
    def get_args_count(self):
        return 0

    def execute(self): pass


class GoDown(IUserCommand):
    def get_command_tag(self):
        return 'down'

    def get_args_count(self):
        return 0

    def execute(self): pass


class GoLeft(IUserCommand):
    def get_command_tag(self):
        return 'left'

    def get_args_count(self):
        return 0

    def execute(self): pass


class GoRight(IUserCommand):
    def get_command_tag(self):
        return 'right'

    def get_args_count(self):
        return 0

    def execute(self): pass


class Skip(IUserCommand):
    def get_command_tag(self):
        return 'skip'

    def get_args_count(self):
        return 0

    def execute(self): pass


class Start(IUserCommand):
    def get_command_tag(self):
        return 'start'

    def get_args_count(self):
        return 1

    def is_valid_size(self, size):
        try:
            assert (int(size) >= 4) and (int(size) <= 10)
        except:
            print("Labyrinth size must be an integer from 4 to 10")
            return False
        return True

    def execute(self, labyrinth_size):
        if self.is_valid_size(size=labyrinth_size):
            print(f"Created labyrinth of size {labyrinth_size}x{labyrinth_size}") 


class Quit(IUserCommand):
    def get_command_tag(self):
        return 'quit'

    def get_args_count(self):
        return 0

    def execute(self): pass
    

class Save(IUserCommand):
    def get_command_tag(self):
        return 'save'

    def get_args_count(self):
        return 1

    def execute(self): pass
