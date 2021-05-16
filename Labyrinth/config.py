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