import abc

class IReporter(abc.ABC):
    def report(self):
        pass

class Reporter(IReporter):
    def __init__(self, description: str, printer):
        self.description = description
        self.printer = printer

    def report(self):
        self.printer.print(self.description)


