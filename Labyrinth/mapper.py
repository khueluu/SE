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
        'exit': 'Step impossible, exit. You must find treasure before exitting.'
    },
    'step_possible': 'Step executed.',
    'skip':  'Skip.',
    'win': 'Step executed, exit. YOU WIN!',
    'objects': {
        'treasure': 'TREASURE!',
        'wormhole': 'WORMHOLE!',
        'wormhole_next': 'Moved to next wormhole.'
    }
}