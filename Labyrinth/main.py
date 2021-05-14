import sys
import random
from impl.commands import *


def parse_user_input(user_input):
    cmd = user_input.strip().lower()
    if cmd not in supported_commands:
        print("Command not supported")
    return cmd, ""

def eval_maze_size(maze_size):
    try:
        maze_size = int(maze_size)
        if maze_size < 4 or maze_size > 10:
            print("Maze size must be from 4 to 10")
            return False
    except:
        print("Invalid maze size")
        return False
    return True

def make_commands_dict(cmd_lst):
    cmd_dict = dict()
    for cmd in cmd_lst:
        cmd_dict[cmd.get_command_tag().lower().strip()] = cmd
    return cmd_dict

supported_commands = make_commands_dict(
    [ GoUp()
    , GoDown()
    , GoLeft()
    , GoRight()
    , Skip()
    ])

def set_maze_size():
    maze_size_selected = False
    while not maze_size_selected:
        maze_size = input("$> Select maze size from 4 to 10: ")
        if eval_maze_size(maze_size):
            maze_size = int(maze_size)
            print(f"Created maze of size {maze_size}x{maze_size}")
            maze_size_selected = True

def play():
    finished = False
    state = ""
    message = ""
    cmd = None
    try:
        while not(finished):
            user_input = input("$> ")
            cmd, message = parse_user_input(user_input)
            if cmd is None:
                print(message)
                continue
            else:
                print(f"{cmd.capitalize()}: OK")
    except KeyboardInterrupt:
        print('\nBye bye')
    except:
        print("Unexpected error:", sys.exc_info()[0])

if __name__ == "__main__":
    print("="*20, "Welcome to Labyrith", "="*20)
    set_maze_size()
    play()

    