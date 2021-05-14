from abc import *

class IObject(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self): pass
