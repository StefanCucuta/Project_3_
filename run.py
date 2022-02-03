""" Battlefield Game """

# Libraires

import re
import random
import time

# Legend, Allows the game display to be updated with ease
EMPTY = '─'

# Coordinate doesn't hold ship/hasn't been guessed
SHIP = '■'

# Coordinate holds a ship
HITSHIP = 'X'

# Coordinate holds a ship that has been attacked
GUESSED = 'O'

# Used to separate the different phases of the game
PHASE = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'


def run_game():
    
    print('WELCOME TO BATTLESHIPS!')
    print('THE BOARD IS A GRID OF 10X10 WITH FOUR SHIPS TO SINK')
    print('AIRCRAFT CARRIER - BATTLECRUISER - SUBMARINE - FRIGATE')
    print('A TOTAL SCORE OF 15 IS REQUIRED TO WIN, 1 POINT PER HIT\n')
    print('NAME CAN BE 10 CHARACTERS MAX. LETTERS, NUMBERS & UNDERSCORES ONLY')


run_game()