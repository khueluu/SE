movement_mapper = {
    'up': {
        'wall_to_check': 'top',
        'row_change': -1,
        'col_change': 0
    },
    'down': {
        'wall_to_check': 'bottom',
        'row_change': 1,
        'col_change': 0
    },
    'left': {
        'wall_to_check': 'left',
        'row_change': 0,
        'col_change': -1
    },
    'right': {
        'wall_to_check': 'right',
        'row_change': 0,
        'col_change': 1
    }
}

messages = {
    'step_impossible':{
        'monolith': 'Step impossible, monolith.',
        'wall': 'Step impossible, wall.',
        'exit': {
            'found_treasure':'Step executed, exit. YOU WIN!',
            'not_found_treasure': 'Step impossible, exit. You must find treasure before exitting.'
        }
    },
    'step_possible': {
        'wormhole': 'Step executed, wormhole.',
        'normal': 'Step executed.',
    },
    'skip': {
        'treasure_and_wormhole': 'Skip, move to next wormhole and found treasure!',
        'wormhole': 'Skip, move to next wormhole.',
        'normal': 'Skip.'
    }
}