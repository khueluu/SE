from abc import *

class IUserCommand(metaclass = ABCMeta):
    @abstractmethod
    def get_command_tag(self): pass

    @abstractmethod
    def get_args_count(self): pass

    @abstractmethod
    def __call__(self, lbr, *args, **kwargs): pass

