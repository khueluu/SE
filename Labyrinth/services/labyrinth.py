from abc import *
from services.generator import IGenerator

class ICell(metaclass=ABCMeta):
    @abstractmethod
    def get_position(self): pass

    @abstractmethod
    def get_walls(self): pass

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

    # Getters
    @abstractmethod
    def get_size(self): pass
    
    @abstractmethod
    def get_exit(self): pass
    
    @abstractmethod
    def get_treasure(self): pass

    @abstractmethod
    def get_wormholes(self): pass

    @abstractmethod
    def get_wormhole_by_idx(self, idx: int): pass

    @abstractmethod
    def get_walls(self): pass

    @abstractmethod
    def get_current(self): pass

    @abstractmethod
    def get_found_treasure(self): pass

    @abstractmethod
    def get_maze(self): pass

    # Setters
    @abstractmethod
    def set_size(self, size: int): pass

    @abstractmethod
    def set_exit(self, exit_): pass

    @abstractmethod
    def set_treasure(self, treasure): pass

    @abstractmethod
    def set_wormholes(self, wormholes: list): pass

    @abstractmethod
    def set_walls(self, walls: list): pass

    @abstractmethod
    def set_current(self, current): pass

    @abstractmethod
    def set_found_treasure(self, found_treasure: bool): pass
    
    @abstractmethod
    def set_maze(self, size: int): pass

    @abstractmethod
    def set_maze_from_data(self, data: list): pass

