import sys
import random
from impl.commands import *
from utils import *

def main():
    finished = False
    try:
        while not(finished):
            user_input = input("$> ")
            cmd, args = parse_user_input(user_input)
            if cmd and args:
                cmd.execute(*args)
            elif cmd:
                cmd.execute()
  
    except KeyboardInterrupt:
        print("\nQuit game")

if __name__ == "__main__":
    print("="*20, "Welcome to Labyrith", "="*20)
    main()

    