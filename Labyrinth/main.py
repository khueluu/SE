import sys
import random
from impl.commands import *

supported_commands = {
    "up": GoUp(),
    "down": GoDown(),
    "left": GoLeft(),
    "right": GoRight(),
    "skip": Skip(),
    "start": Start(),
    "quit": Quit(),
    "save": Save(),
}

def parse_user_input(user_input):
    tokens = user_input.strip().split(" ")

    cmd = tokens[0].strip().lower() if len(tokens) > 0 else None
    args = tokens[1:] if len(tokens) > 1 else None

    valid_cmd = supported_commands[cmd] if (cmd and is_valid_command(cmd)) else None
    valid_args = args if (valid_cmd and args and is_valid_args(valid_cmd, args)) else None

    return (valid_cmd, valid_args)

def validate(assertion, error_message):
    try:
        assert assertion
    except:
        print(error_message)
        return False
    return True

def is_valid_command(cmd: IUserCommand):
    assertion = cmd in supported_commands
    error_message = f"Command not supported"
    return validate(assertion, error_message)

def is_valid_args(cmd : IUserCommand, args: list):
    cmd_args_count = cmd.get_args_count()
    current_args_count = len(args)
    assertion = cmd_args_count == current_args_count
    error_message = f"Invalid number of args. Expected: {cmd_args_count}, got {current_args_count}"
    return validate(assertion, error_message)


# def validate_labyrinth_size(size):
#     assertion = (int(size) >= 4) and (int(size) <= 10)
#     error_message = "Labyrinth size must be an integer from 4 to 10"
#     return validate(assertion, error_message)


# def create_labyrinth():
#     size_selected = False
#     while not size_selected:
#         size = input("$> Select labyrinth size from 4 to 10: ")
#         if eval_labyrinth_size(size):
#             size = int(size)
#             print(f"Created labyrinth of size {size}x{size}")
#             size_selected = True

def play():
    finished = False
    try:
        while not(finished):
            user_input = input("$> ")
            cmd, args = parse_user_input(user_input)

            
    except KeyboardInterrupt:
        print("\nQuit game")
    except:
        print("Unexpected error:", sys.exc_info()[0])

if __name__ == "__main__":
    print("="*20, "Welcome to Labyrith", "="*20)
    # create_labyrinth()
    play()

    