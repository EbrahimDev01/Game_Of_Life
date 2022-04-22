from random import randint
from time import sleep
from os import system
from copy import deepcopy

# The Cosmos is infinite but computers aren't infinite
COSMOS_HEIGHT = 30
COSMOS_WIDTH = 30

CELL_LIVE = '█'
CELL_DEAD = ' '

SURVIVAL_PROBABILITIES_PERCENT = 15
ALTERNATION_TIME_PERSECOND = .25


def cosmos_draw(cosmos):
    system('cls')
    print('_' * (COSMOS_WIDTH+2))
    for y in cosmos:
        cosmos_row = '|'
        for x in y: 
            cosmos_row += CELL_LIVE if x else CELL_DEAD
        cosmos_row += '|'
        print(cosmos_row)
    print('-' * (COSMOS_WIDTH+2))

    sleep(ALTERNATION_TIME_PERSECOND)
    azraelle(cosmos)
    
def azraelle(cosmos):
    """
    a determinant of life or death
    """
    cosmos_map = deepcopy(cosmos)
    for y in range(COSMOS_HEIGHT):
        for x in range(COSMOS_WIDTH):
            number_live_neighbors = live_neighbors_count(cosmos_map, y, x)
            
            cosmos[y][x] = number_live_neighbors == 3 or (cosmos_map[y][x] and number_live_neighbors == 2)

    cosmos_draw(cosmos)

def live_neighbors_count(cosmos_map, y, x):
    number_live_neighbors = 0

    for neighborhood_y in range(y-1, y+2):
        for neighborhood_x in range(x-1, x+2):
            neighbor_y = (neighborhood_y + COSMOS_HEIGHT) % COSMOS_HEIGHT
            neighbor_x = (neighborhood_x + COSMOS_WIDTH) % COSMOS_WIDTH
            if cosmos_map[neighbor_y][neighbor_x]:
                number_live_neighbors += 1

    if cosmos_map[y][x]:
        number_live_neighbors -= 1

    return number_live_neighbors

def big_bang():
    """
    cosmos beginning
    """
    cosmos = [[randint(0, 100) < SURVIVAL_PROBABILITIES_PERCENT for _ in range(COSMOS_WIDTH)] for _ in range(COSMOS_HEIGHT)]
    cosmos_draw(cosmos)
   
big_bang()
