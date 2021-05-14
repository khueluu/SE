from abc import *

class IUserCommand(metaclass = ABCMeta):
    @abstractmethod
    def get_command_tag(self): pass

    @abstractmethod
    def execute(self): pass

    # Returns: (finish?, state, msg)
