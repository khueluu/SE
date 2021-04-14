from IOutput import ConsoleOutput, FileOutput
from IAnimal import Cat, Dog
from IReporter import Reporter
import os

BASE = '/Users/khueluu/Desktop/NSU/Sem2/SE/SE/CW1'

def main():
    # Initialize outputs
    console_output = ConsoleOutput()
    file_output = FileOutput(file_path=os.path.join(BASE, 'output.txt'))

    # Initialize reporters
    console_reporter = Reporter(
        description='I am a Console Reporter.',
        text_output=console_output)
    file_reporter = Reporter(
        description='I am a File Reporter.',
        text_output=file_output)

    # Report descriptions
    console_reporter.report()
    file_reporter.report()

    # Cat and Dog
    # console_output = ConsoleOutput()
    # file_output_for_cat = FileOutput(file_path=os.path.join(BASE, 'cat_sound.txt'))
    # cat_console = Cat(sound_output=console_output)
    # cat_file = Cat(sound_output=file_output_for_cat)
    # cat_console.make_sound()
    # cat_file.make_sound()

    # file_output_for_dog = FileOutput(file_path=os.path.join(BASE, 'dog_sound.txt'))
    # dog_console = Dog(sound_output=console_output)
    # dog_file = Dog(sound_output=file_output_for_dog)
    # dog_console.make_sound()
    # dog_file.make_sound()

if __name__ == '__main__':
    main()

