import abc

class IOutputStream(abc.ABC):
    @abc.abstractmethod
    def write(self, text: str):
        pass

class ConsoleStream(IOutputStream):
    def write(self, text: str):
        print(text)

class FileStream(IOutputStream):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, text: str):
        with open(self.file_path, 'w+') as f:
            f.write(text)
        print(f'Printed to {self.file_path}')
