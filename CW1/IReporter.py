import abc
from IPrinter import IPrinter

class IReporter(abc.ABC):
    def report(self):
        pass

class ConsoleReporter(IReporter):
    def __init__(self, description: str, Printer: IPrinter):
        self.description = description
        self.printer = Printer()

    def report(self):
        self.printer.print(self.description)

class FileReporter(IReporter):
    def __init__(self, description: str, file_path: str, Printer: IPrinter):
        self.description = description
        self.printer = Printer(file_path)

    def report(self):
        self.printer.print(self.description)

