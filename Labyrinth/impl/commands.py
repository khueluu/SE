from services.command import IUserCommand

class GoUp(IUserCommand):
    def get_command_tag(self):
        return 'up'
    
    def execute(self): pass

class GoDown(IUserCommand):
    def get_command_tag(self):
        return 'down'

    def execute(self): pass

class GoLeft(IUserCommand):
    def get_command_tag(self):
        return 'left'

    def execute(self): pass

class GoRight(IUserCommand):
    def get_command_tag(self):
        return 'right'

    def execute(self): pass

class Skip(IUserCommand):
    def get_command_tag(self):
        return 'skip'

    def execute(self): pass

class Start(IUserCommand):
    def get_command_tag(self):
        return 'start'

    def execute(self): pass

class Quit(IUserCommand):
    def get_command_tag(self):
        return 'quit'

    def execute(self): pass

class Save(IUserCommand):
    def get_command_tag(self):
        return 'save'

    def execute(self): pass
