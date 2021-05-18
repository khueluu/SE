import sys
import random
import os
from impl.commands import *
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
    except KeyboardInterrupt:
        print("\nQuit game without saving")

def validate_size(size):
    try:
        assert (int(size) >= 4) and (int(size) <= 10)
    except:
        print("Labyrinth size must be an integer from 4 to 10")
        return False
    return True

def create_labyrinth():
    finished = False
    try:
        while not(finished):
            size = input("$> Please select labyrinth size from 4 to 10: ")
            is_valid = validate_size(size)
            if is_valid:
                lbr = Labyrinth()
                lbr.create_new(size=size)
                print(f"Created labyrinth of size {lbr.size}x{lbr.size}")
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
    

def main():
    print("="*20, "Welcome to Labyrith", "="*20)
    #lbr = create_labyrinth()
    lbr = load_labyrinth()
    play(lbr)

if __name__ == "__main__":
    main()

    