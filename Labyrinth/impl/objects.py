from services.object import IObject

class Maze(IObject):
    def get_name(self):
        return 'maze'

class Treasure(IObject):
    def get_name(self):
        return 'treasure'

class Wormhole(IObject):
    def get_name(self):
        return 'wormhole'

class UserInventory(IObject):
    def get_name(self):
        return 'inventory'