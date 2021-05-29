import json
from jsonschema import Draft7Validator
from copy import deepcopy
from collections import Counter


SCHEMA_PATH = '/Users/khueluu/Desktop/NSU/Sem2/SE/SE/Labyrinth/schema/labyrinth.schema.json'

def is_between(value, left, right):
    return left <= value and value <= right

def is_same_cell(cell_1: tuple, cell_2: tuple):
    return (cell_1[0] == cell_2[0]) and (cell_1[1] == cell_2[1])

def check_duplicated_position(list_: list):
    tup = tuple(tuple(ele) for ele in list_)
    res = [ele for ele, count in Counter(tup).items() if count > 1]
    return bool(res)

def check_duplicated_wall_data(wall_data_list):
    tups = []

    for wall_data in wall_data_list:
        (row, col), wall_name = wall_data
        tup = (row, col, wall_name)
        tups.append(tup)
        
    tups = tuple(tups)
    duplicated = check_duplicated_position(list_=tups)
    return bool(duplicated)

def get_matching_wall(row: int, col: int, wall_type: str):
    if wall_type == 'top':
        return ((row-1, col), 'bottom')
    if wall_type == 'bottom':
        return ((row+1, col), 'top')
    if wall_type == 'left':
        return ((row, col-1), 'right')
    if wall_type == 'right':
        return((row, col+1), 'left')

def get_next_idx_of_seq(idx: int, seq_length: int):
    next_idx = idx + 1
    return next_idx if next_idx < seq_length else 0

def validate_schema(instance: dict):
    with open(SCHEMA_PATH, 'r') as schema_file:
        schema = json.load(schema_file)

    val = Draft7Validator(schema=schema)
    val.validate(instance)


