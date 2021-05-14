from abc import *

class IUserCommand(metaclass = ABCMeta):
    @abstractmethod
    def get_command_tag(self): pass

    # Returns: (finish?, state, msg)
