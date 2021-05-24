from abc import *

class ICell(metaclass=ABCMeta):
    @abstractmethod
    def get_position(self): pass

    @abstractmethod
    def get_walls(self): pass

    @abstractmethod
    def set_wall(self, wall_name: str, wall_type: str): pass

class ILabyrinth(metaclass=ABCMeta):
    @abstractmethod
    def create(self, size: int): pass

    @abstractmethod
    def __getitem__(self, idx: int): pass

    @abstractmethod
    def get_current_cell(self): pass

    @abstractmethod
    def get_current(self): pass

    @abstractmethod
    def set_current(self): pass

    @abstractmethod
    def get_walls(self): pass

    @abstractmethod
    def get_size(self): pass

    @abstractmethod
    def get_wormholes(self): pass

    @abstractmethod
    def get_wormhole_by_idx(self, idx: int): pass

    @abstractmethod
    def get_exit(self): pass

    @abstractmethod
    def get_found_treasure(self): pass

    @abstractmethod
    def set_found_treasure(self): pass

    @abstractmethod
    def load(self, input_file: str): pass

    @abstractmethod
    def save(self, output_file: str): pass


class ILabyrinthGenerator(metaclass=ABCMeta):
    @abstractmethod
    def random_border_cell(self): pass

    @abstractmethod
    def random_walls(self): pass

    @abstractmethod
    def random_sequence_of_cells(self, length: int): pass

    @abstractmethod
    def random_cell(self): pass
