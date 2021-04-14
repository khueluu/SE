from IOutput import ConsoleOutput, FileOutput
from IReporter import Reporter

OUTPUT_PATH = '/Users/khueluu/Desktop/NSU/Sem2/SE/SE/CW1/output.txt'

def main():
    # Initialize printers
    console_output = ConsoleOutput()
    file_output = FileOutput(file_path=OUTPUT_PATH)

    # Initialize reporters
    console_reporter = Reporter(
        description='I am a Console Reporter.',
        output=console_output)
    file_reporter = Reporter(
        description='I am a File Reporter.',
        output=file_output)

    # Report descriptions
    console_reporter.report()
    file_reporter.report()

if __name__ == '__main__':
    main()

