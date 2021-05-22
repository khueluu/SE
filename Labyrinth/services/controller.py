from abc import *
from services.labyrinth import ILabyrinth

class IController(metaclass=ABCMeta):
    @abstractmethod
    def move(self, direction: str): pass

    