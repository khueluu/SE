from abc import *
from services.generator import IGenerator

class ICell(metaclass=ABCMeta):
    @property
    @abstractmethod
    def position(self): pass

    @property
    @abstractmethod
    def walls(self): pass

    @abstractmethod
    def set_wall(self, wall_name: str, wall_type: str): pass

    @abstractmethod
    def get_dict(self): pass


class ILabyrinth(metaclass=ABCMeta):
    @abstractmethod
    def __getitem__(self, idx: int): pass

    @abstractmethod
    def create(self, size: int, generator: IGenerator): pass

    @abstractmethod
    def do_found_treasure(self): pass

    @property
    @abstractmethod
    def size(self):
        return self.__size

    @size.setter
    @abstractmethod
    def size(self, size: int):
        self.__size = size

    @property
    @abstractmethod
    def maze(self): pass

    @maze.setter
    @abstractmethod
    def maze(self, data): pass

    @property
    @abstractmethod
    def wormholes(self): pass

    @wormholes.setter
    @abstractmethod
    def wormholes(self, data: tuple): pass

    @property
    @abstractmethod
    def found_treasure(self): pass

    @found_treasure.setter
    @abstractmethod
    def found_treasure(self, data: bool): pass

    @property
    @abstractmethod
    def current(self): pass

    @current.setter
    @abstractmethod
    def current(self, data: tuple): pass

    @property
    @abstractmethod
    def treasure(self): pass
    
    @treasure.setter
    @abstractmethod
    def treasure(self, data: tuple): pass

    @property
    @abstractmethod
    def walls(self): pass

    @walls.setter
    @abstractmethod
    def walls(self, data: tuple): pass

    @property
    @abstractmethod
    def monoliths(self): pass

    @property
    @abstractmethod
    def exit(self): pass
    
    @exit.setter
    @abstractmethod
    def exit(self, data: tuple): pass
