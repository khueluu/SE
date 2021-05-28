from abc import *
from services.labyrinth import ILabyrinth

class IController(metaclass=ABCMeta):
    @abstractmethod
    def move(self, direction: str): pass

    @abstractmethod
    def skip(self): pass

    @abstractmethod
    def get_labyrinth(self): pass


class IInputOutput(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, filepath: str): pass