from abc import *

class IGenerator(metaclass=ABCMeta):
    @abstractmethod
    def random_border_cell(self): pass

    @abstractmethod
    def random_walls(self): pass

    @abstractmethod
    def random_sequence_of_cells(self, length: int): pass

    @abstractmethod
    def random_cell(self): pass
