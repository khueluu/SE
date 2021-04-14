import abc

class IReporter(abc.ABC):
    def report(self):
        pass

class Reporter(IReporter):
    def __init__(self, description: str, output):
        self.description = description
        self.output = output

    def report(self):
        self.output.print(self.description)


