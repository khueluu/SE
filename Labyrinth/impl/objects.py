import networkx as nx
from services.object import IObject

class Labyrinth(IObject):
    def __init__(self, size):
        self.size = size

    def get_name(self):
        return 'labyrinth'

class Treasure(IObject):
    def get_name(self):
        return 'treasure'

class Wormhole(IObject):
    def get_name(self):
        return 'wormhole'

class UserInventory(IObject):
    def get_name(self):
        return 'inventory'
        