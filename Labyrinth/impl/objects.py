from services.object import IObject

class Labyrinth(IObject):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return 'labyrinth'

class Treasure(IObject):
    def __str__(self):
        return 'treasure'

class Wormhole(IObject):
    def __str__(self):
        return 'wormhole'

class UserInventory(IObject):
    def __str__(self):
        return 'inventory'
        