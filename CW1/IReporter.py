import abc

class IReporter(abc.ABC):
    @abc.abstractmethod
    def report(self):
        pass

class Reporter(IReporter):
    def __init__(self, description: str, text_output):
        self.description = description
        self.text_output = text_output

    def report(self):
        self.text_output.write(self.description)


