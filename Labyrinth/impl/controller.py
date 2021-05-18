import sys

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

def check_wall(lbr, wall):
    if wall == 'monolith':
        return 'Step impossible, monolith'
    if wall == 'wall':
        return 'Step impossible, wall'
    if wall == 'exit':
        if lbr.found_treasure:
            return 'Step executed, exit. YOU WIN!'
        else:
            return 'Step impossible, exit. You must find treasure before exitting'
    return ''

def move_through_wormhole(lbr):
    current_cell = lbr.get_current_cell()
    current_wormhole_idx = current_cell.wormhole_idx
    # print('current wh idx', current_wormhole_idx)
    new_wormhole_idx = current_wormhole_idx+1
    new_wormhole_idx = new_wormhole_idx if new_wormhole_idx <=4 else 0
    next_wormhole = lbr.wormholes_cells[new_wormhole_idx]
    curr_row, curr_col = lbr.current_cell
    next_row, next_col = next_wormhole
    lbr.current_cell = (next_row, next_col)
    lbr[curr_row][curr_col].is_current = False
    lbr[next_row][next_col].is_current = True
    # print('moved to', (next_row, next_col))
    return lbr

def move(lbr, direction):
    print(lbr)
    mapper = movement_mapper[direction]
    current_cell = lbr.get_current_cell()
    # print('current_cell', current_cell.row, current_cell.col)
    wall = current_cell.walls[mapper['wall_to_check']]
    if wall is not None:
        msg = check_wall(lbr, wall)
        print(msg)
        if msg == 'Step executed, exit. YOU WIN!':
            sys.exit()
    else:
        row = current_cell.row
        col = current_cell.col
        lbr[row][col].is_current = False
        new_row = row + mapper['row_change']
        new_col = col + mapper['col_change']
        # print('new cell', new_row, new_col)
        lbr[new_row][new_col].is_current = True
        lbr.current_cell = (new_row, new_col)

        # Check collectables of new cell
        has_treasure = lbr[new_row][new_col].treasure
        if has_treasure:
            lbr[new_row][new_col].treasure = False
            lbr.found_treasure = True
        has_wormhole = lbr[new_row][new_col].wormhole_idx >= 0
        msg = 'Step executed'
        has_both = has_treasure and has_wormhole
        if has_both:
            msg = 'Step executed, treasure and wormhole'
        elif has_treasure and (not has_wormhole):
            msg = 'Step executed, treasure'
        elif has_wormhole and (not has_treasure):
            msg = 'Step executed, wormhole'
        
        if has_wormhole:
            lrb = move_through_wormhole(lbr)
        print(msg)
    return lbr
