import abc

class IPrinter(abc.ABC):
    @abc.abstractmethod
    def write(self, string: str):
        pass

class ConsolePrinter(IPrinter):
    def write(self, string: str):
        print(string)

class FilePrinter(IPrinter):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, string: str):
        with open(self.file_path, 'w+') as f:
            f.write(string)
        print(f'Printed to {self.file_path}')
