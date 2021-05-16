from abc import *

class IObject(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self): pass

class IGameObject(IObject): pass
class IUserObject(IObject): pass
