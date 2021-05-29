import sys
import random
import os

from impl.labyrinth import Labyrinth
from impl.generator import Generator
from impl.validator import Validator
from config import supported_commands
from mapper import messages
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
        print(messages['quit_no_save'])

def generate_labyrinth(size, wall_rate=0.5, sequence_length=5):
    validator = Validator()
    finished = False
    count = 0

    while not finished:
        count += 1
        generator = Generator(
            size=size,
            wall_rate=wall_rate,
            sequence_length=sequence_length)
        
        lbr = Labyrinth()
        lbr.create(size=size, generator=generator)
        
        is_valid_labyrinth = validator.validate(lbr)
        if is_valid_labyrinth: finished = True

    print(f'Created labyrinth of size {lbr.get_size()}x{lbr.get_size()} after {count} generation(s).')
    return lbr

def create_labyrinth():
    finished = False
    try:
        while not(finished):
            size = input(messages['choose_size'])
            is_valid = validate_size(size)
            if is_valid: finished = True
                
        lbr = generate_labyrinth(size=int(size), wall_rate=0.5, sequence_length=5)    
        return lbr
    except KeyboardInterrupt:
        print(messages['quit_no_save'])
        sys.exit()

def load_labyrinth():
    finished = False
    try:
        while not(finished):
            input_file = input(messages['choose_file'])
            is_valid_file = validate(os.path.isfile(input_file), "File not found")
            if is_valid_file: finished = True
        
        cmd = supported_commands['load']
        lbr = cmd(lbr=Labyrinth(), input_file=input_file)
        return lbr
    except KeyboardInterrupt:
        print(messages['quit_no_save'])
        sys.exit()
    
def initialize():
    print(messages['welcome'])
    supported_init_cmds = {
        'create': create_labyrinth,
        'load': load_labyrinth
    }
    finished = False
    
    try:
        while not(finished):
            cmd = input(messages['init'])
            cmd = cmd.strip().lower()

            assertion = cmd in supported_init_cmds.keys()
            error_message = messages['init_error']
            is_valid_cmd = validate(assertion, error_message)
            if is_valid_cmd: finished = True

        func = supported_init_cmds[cmd]
        lbr = func()
        return lbr
    except KeyboardInterrupt:
        print(messages['quit_no_save'])
        sys.exit()

def main():
    lbr = initialize()
    play(lbr)

if __name__ == "__main__":
    main()

    