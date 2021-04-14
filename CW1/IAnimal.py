import abc

class IAnimal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass

class Cat(IAnimal):
    def __init__(self, sound_output):
        self.sound_output = sound_output

    def make_sound(self):
        self.sound_output.write('Miao')

class Dog(IAnimal):
    def __init__(self, sound_output):
        self.sound_output = sound_output

    def make_sound(self):
        self.sound_output.write('Woof')
