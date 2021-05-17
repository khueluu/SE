movement_mapper = {
    'up': {
        'wall_to_check': 'top_wall',
        'row_change': -1,
        'col_change': 0
    },
    'down': {
        'wall_to_check': 'bottom_wall',
        'row_change': 1,
        'col_change': 0
    },
    'left': {
        'wall_to_check': 'left_wall',
        'row_change': 0,
        'col_change': -1
    },
    'right': {
        'wall_to_check': 'right_wall',
        'row_change': 0,
        'col_change': 1
    }
}

def check_exit(lbr):
    if lbr.found_treasure:
        return 'Step executed, exit. YOU WIN!'
        sys.exit()
    else:
        return 'Step impossible, exit. You must find treasure before exitting'

wall_check_mapper = {
    'monolith': 'Step impossible, monolith',
    'wall': 'Step impossible, wall',
    'exit': 'Step executed, exit. YOU WIN!'
}
def move_through_wormhole(lbr):
    current_cell = lbr.get_current_cell()
    current_wormhole_idx = current_cell.wormhole_idx
    print('current wh idx', current_wormhole_idx)
    next_wormhole = lbr.wormholes_cells[current_wormhole_idx+1]
    curr_row, curr_col = lbr.current_cell
    next_row, next_col = next_wormhole
    print('wh list', lbr.wormholes_cells)
    print('next wh idx', (next_row, next_col))
    lbr.current_cell = (next_row, next_col)
    lbr[curr_row][curr_col].is_current = False
    lbr[new_row][next_col].is_current = True
    return lbr

def move(lrb, direction):
    mapper = movement_mapper[direction]
    current_cell = lbr.get_current_cell()
    print('current_cell', current_cell.row, current_cell.col)
    wall = current_cell.walls[mapper['wall_to_check']]
    if wall is not None:
        msg = wall_check_mapper[wall]
        print('Wall not none msg', msg)
    else:
        row = current_cell.row
        col = current_cell.col
        lbr[row][col].is_current = False
        new_row = row + mapper['row_change']
        new_col = col + mapper['col_change']
        print('new cell', new_row, new_col)
        lbr[new_row][new_col].is_current = True
        lbr.current_cell = (new_row, new_col)

        # Check collectables of new cell
        has_treasure = lbr[new_row][new_col].treasure
        if has_treasure:
            lbr[new_row][new_col].treasure = False
            lbr.found_treasure = True
        has_wormhole = lbr[new_row][new_col].wormhole_idx >= 0
        msg = 'Step executed'
        print('has tresure', has_treasure)
        print('has wormhole', has_wormhole)
        if has_treasure and has_wormhole:
            msg = 'Step executed, treasure and wormhole'
        if has_treasure and (not has_wormhole):
            msg = 'Step executed, treasure'
        if has_wormhole and (not has_treasure):
            msg = 'Step executed, worm hole'
        if has_wormhole:
            lrb = move_through_wormhole(lbr)
        print('check_collectables msg', msg)
    return lbr

if __name__ == '__main__':
    from impl.objects import Labyrinth
    lbr = Labyrinth(size=4)
    print('=== up ===')
    lbr = move(lbr, 'up')
    print('')
    print('=== down ===')
    lbr = move(lbr, 'down')
    print('')
    print('=== left ===')
    lbr = move(lbr, 'left')
    print('')
    print('=== right ===')
    lbr = move(lbr, 'right')
    print('')
    print('found_treasure', lbr.found_treasure)