import abc

class IOutput(abc.ABC):
    @abc.abstractmethod
    def write(self, text: str):
        pass

class ConsoleOutput(IOutput):
    def write(self, text: str):
        print(text)

class FileOutput(IOutput):
    def __init__(self, file_path):
        self.file_path = file_path

    def reset_file_path(self, new_file_path):
        self.file_path = new_file_path

    def write(self, text: str):
        with open(self.file_path, 'w+') as f:
            f.write(text)
        print(f'Printed to {self.file_path}')
