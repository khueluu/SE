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
        assert (maze_size >= 4) and (maze_size <= 10)
    except:
        print("Maze size must be an integer from 4 to 10")
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
    , Start()
    , Quit()
    , Save()
    ])

def create_maze():
    maze_size_selected = False
    while not maze_size_selected:
        maze_size = input("$> Select maze size from 4 to 10: ")
        if eval_maze_size(maze_size):
            maze_size = int(maze_size)
            print(f"Created maze of size {maze_size}x{maze_size}")
            maze_size_selected = True

def play():
    finished = False
    try:
        while not(finished):
            user_input = input("$> ")
            cmd, message = parse_user_input(user_input)
            if cmd is None:
                print(message)
                continue
            else:
                print(cmd)
    except KeyboardInterrupt:
        print("\nQuit game")
    except:
        print("Unexpected error:", sys.exc_info()[0])

if __name__ == "__main__":
    print("="*20, "Welcome to Labyrith", "="*20)
    create_maze()
    play()

    