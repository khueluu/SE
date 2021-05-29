from abc import *
from services.labyrinth import ILabyrinth

class IValidator(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, labyrinth: ILabyrinth, return_invalid: bool=False): pass