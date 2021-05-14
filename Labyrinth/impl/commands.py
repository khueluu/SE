from services.command import IUserCommand

class GoUp(IUserCommand):
    def get_command_tag(self):
        return 'go up'

class GoDown(IUserCommand):
    def get_command_tag(self):
        return 'go down'

class GoLeft(IUserCommand):
    def get_command_tag(self):
        return 'go left'

class GoRight(IUserCommand):
    def get_command_tag(self):
        return 'go right'

class Skip(IUserCommand):
    def get_command_tag(self):
        return 'skip'
