import abc

class IPrinter(abc.ABC):
    @abc.abstractmethod
    def prinf(self, string: str):
        pass

class ConsolePrinter(IPrinter):
    def print(self, string: str):
        print(string)

class FilePrinter(IPrinter):
    def __init__(self, file_path):
        self.file_path = file_path

    def print(self, string: str):
        with open(self.file_path) as f:
            f.write(string)
