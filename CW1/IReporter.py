import abc

class IReporter(abc.ABC):
    @abc.abstractmethod
    def report(self):
        pass

class Reporter(IReporter):
    def __init__(self, description: str, stream):
        self.description = description
        self.stream = stream

    def report(self):
        self.stream.write(self.description)


