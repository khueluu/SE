from abc import *

class ILabyrinth(metaclass=ABCMeta):
    @abstractmethod
    def create(self, size: int): pass

    @abstractmethod
    def load(self, input_file: str): pass

    @abstractmethod
    def get_current(self): pass

    @abstractmethod
    def save(self, output_file: str): pass

    @abstractmethod
    def __getitem__(self, idx: int): pass


class ILabyrinthGenerator(metaclass=ABCMeta):
    @abstractmethod
    def random_border_cell(self): pass

    @abstractmethod
    def random_walls(self): pass

    @abstractmethod
    def random_sequence_of_cells(self, length: int): pass

    @abstractmethod
    def random_cell(self): pass
