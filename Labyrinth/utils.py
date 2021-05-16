
from services.command import IUserCommand
from config import supported_commands

def validate(assertion: bool, error_message: str):
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

def parse_user_input(user_input):
    tokens = user_input.strip().split(" ")

    if len(tokens) == 0:
        return (None, None)

    cmd, *args = tokens
    cmd = cmd.strip().lower()
    valid_cmd = supported_commands[cmd] if (cmd and is_valid_command(cmd)) else None
    valid_args = args if (valid_cmd and args and is_valid_args(valid_cmd, args)) else None

    return (valid_cmd, valid_args)