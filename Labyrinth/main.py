import sys
import random
from impl.commands import *
from utils import *

def play(lbr):
    finished = False
    try:
        while not(finished):
            user_input = input("$> ")
            cmd, args = parse_user_input(user_input)
            if cmd and args:
                cmd(lbr, *args)
            elif cmd:
                cmd(lbr)
    except KeyboardInterrupt:
        print("\nQuit game without saving")

def is_valid_size(size):
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
            if is_valid_size(size):
                lbr = Labyrinth(size=size)
                print(f"Created labyrinth of size {lbr.size}x{lbr.size}")
                finished = True
                return lbr
    except KeyboardInterrupt:
        print("\nQuit game without saving")
        sys.exit()
    

def main():
    print("="*20, "Welcome to Labyrith", "="*20)
    lbr = create_labyrinth()
    play(lbr)

if __name__ == "__main__":
    
    main()

    