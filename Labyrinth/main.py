import sys
import random
import os

from impl.labyrinth import Labyrinth, LabyrinthGenerator
from impl.validator import Validator
from utils import *

def play(lbr):
    finished = False
    try:
        while not(finished):
            user_input = input("$> ")
            cmd, args = parse_user_input(user_input)
            if cmd and args:
                lbr = cmd(lbr, *args)
            elif cmd:
                lbr = cmd(lbr)
                print(lbr)
    except KeyboardInterrupt:
        print("\nQuit game without saving")

def validate_size(size):
    try:
        assert (int(size) >= 4) and (int(size) <= 10)
    except:
        print("Labyrinth size must be an integer from 4 to 10")
        return False
    return True

def generate_labyrinth(size, wall_rate=0.5, sequence_length=5):
    validator = Validator()
    finished = False
    count = 0
    while not finished:
        count += 1

        lbr = Labyrinth()
        lbr_gen = LabyrinthGenerator(
            size=size,
            wall_rate=wall_rate,
            sequence_length=sequence_length)
        lbr.create(size=size, generator=lbr_gen)

        is_valid_labyrinth = validator.validate(lbr)
        if is_valid_labyrinth:
            finished = True
    print(f'Created labyrinth of size {lbr.size}x{lbr.size} after {count} generation(s).')
    return lbr

def create_labyrinth():
    finished = False
    try:
        while not(finished):
            size = input("$> Please select labyrinth size from 4 to 10: ")
            is_valid = validate_size(size)
            if is_valid:
                size = int(size)
                lbr = generate_labyrinth(size=size, wall_rate=0.5, sequence_length=5)
                finished = True
                return lbr
    except KeyboardInterrupt:
        print("\nQuit game without saving")
        sys.exit()

def load_labyrinth():
    finished = False
    try:
        while not(finished):
            input_file = input("$> Please type file path to load labyrinth: ")
            is_valid = validate(os.path.isfile(input_file),"File not found")
            if is_valid:
                lbr = Labyrinth()
                lbr.load(input_file=input_file)
                print(f"Loaded labyrinth of size {lbr.size}x{lbr.size}")
                finished = True
                return lbr
    except KeyboardInterrupt:
        print("\nQuit game without saving")
        sys.exit()
    
def welcome():
    print("="*20, "Welcome to Labyrith", "="*20)
    finished = False
    try:
        while not(finished):
            cmd = input("$> To create new game, type 'create'. To load a game, type 'load': ")
            cmd = cmd.strip().lower()
            assertion = cmd in ['create', 'load']
            error_message = "Please only type 'create' or 'load' without any arguments"
            is_valid = validate(assertion, error_message)
            if is_valid:
                return cmd
    except KeyboardInterrupt:
        print("\nQuit game without saving")
        sys.exit()

def main():
    cmd = welcome()
    if cmd == 'create':
        lbr = create_labyrinth()
    elif cmd == 'load':
        lbr = load_labyrinth()
    play(lbr)

if __name__ == "__main__":
    main()

    