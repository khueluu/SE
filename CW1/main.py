from IOutputStream import ConsoleStream, FileStream
from IAnimal import Cat, Dog
from IReporter import Reporter
import os

BASE = '/Users/khueluu/Desktop/NSU/Sem2/SE/SE/CW1'

def main():
    # Initialize outputs
    console_stream = ConsoleStream()
    file_stream = FileStream(file_path=os.path.join(BASE, 'output.txt'))

    # Initialize reporters
    console_reporter = Reporter(
        description='I am a Console Reporter.',
        stream=console_stream)
    file_reporter = Reporter(
        description='I am a File Reporter.',
        stream=file_stream)

    # Report descriptions
    console_reporter.report()
    file_reporter.report()

    # Cat and Dog
    console_stream = ConsoleStream()
    file_stream_for_cat = FileStream(file_path=os.path.join(BASE, 'cat_sound.txt'))
    cat_console = Cat(sound_output=console_stream)
    cat_file = Cat(sound_output=file_stream_for_cat)
    cat_console.make_sound()
    cat_file.make_sound()

    file_stream_for_dog = FileStream(file_path=os.path.join(BASE, 'dog_sound.txt'))
    dog_console = Dog(sound_output=console_stream)
    dog_file = Dog(sound_output=file_stream_for_dog)
    dog_console.make_sound()
    dog_file.make_sound()

if __name__ == '__main__':
    main()

