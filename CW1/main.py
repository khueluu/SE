from IPrinter import ConsolePrinter, FilePrinter
from IReporter import Reporter

OUTPUT_PATH = './CW1/output.txt'

def main():
    # Initialize printers
    console_printer = ConsolePrinter()
    file_printer = FilePrinter(file_path=OUTPUT_PATH)

    # Initialize reporters
    console_reporter = Reporter(
        description='I am a Console Reporter.',
        printer=console_printer)
    file_reporter = Reporter(
        description='I am a File Reporter.',
        printer=file_printer)

    # Report descriptions
    console_reporter.report()
    file_reporter.report()

if __name__ == '__main__':
    main()

