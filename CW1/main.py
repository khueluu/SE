from IPrinter import ConsolePrinter, FilePrinter
from IReporter import ConsoleReporter, FileReporter

def main():
    console_reporter = ConsoleReporter('I am a Console Reporter', ConsolePrinter)
    console_reporter.report()

    file_reporter = FileReporter('I am a File Reporter', './CW1/output.txt', FilePrinter)
    file_reporter.report()

if __name__ == '__main__':
    main()

