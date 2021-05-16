from abc import *

class IObject(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self): pass
