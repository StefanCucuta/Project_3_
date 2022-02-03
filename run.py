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

# Welcome message used at the begaining

def welcome_message():
    
    print('WELCOME TO BATTLESHIPS GAME!')
    print('THE BOARD IS A GRID OF 10X10 WITH FOUR SHIPS TO SINK')
    print('AIRCRAFT CARRIER - BATTLECRUISER - SUBMARINE - FRIGATE')
    print('EACH PLAYER HAS 15 LIVES, THEY LOSE 1 FOR EACH HIT FROM THE OPPONENT\n')
    print(f"{EMPTY} IS FOR AN EMPTY OR CO-ORDINATE THAT HASN'T BEEN GUESSED")
    print(f'{SHIP} REPRESENTS A SHIP')
    print(f'{HITSHIP} REPRESENTS A HIT OR SUNK SHIP')
    print(f'{GUESSED} IS FOR A CO-ORDINATE THAT HAS BEEN GUESSED\n')

# Validate the name of the team

def validate_team_name(name):
    
    if not re.match('^[A-Za-z0-9_]*$', name):
        print('INVALID NAME. LETTERS, NUMBERS AND UNDERSCORES ONLY')
        return False
    elif len(name) > 10:
        print('INVALID NAME. 10 CHARACTERS MAX')
        return False
    elif len(name) == 0:
        print('INVALID NAME. NAME NOT LONG ENOUGH')
    else:
        return True

# Game Board

class GameBoard:

    # Converts letters for display purposes to numbers for functionality
    letters_to_numbers = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
        'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9
        }

    # Valid row input
    row_input = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def __init__(self, name, user):
        self.board = [[EMPTY] * 10 for x in range(10)]
        self.lives = 15
        self.name = name
        self.user = user
        self.column_arry = [10]
        self.row_arry = [10]
        self.attk_arry = [1, 1, 1, 1]

    # Prints the game board

    def print_board(self):
        
        print(f'{self.name} BOARD:\n')
        print('  A B C D E F G H I J ')
        print('  -------------------')
        row_number = 0
        for row in self.board:
            print('%d|%s ' % (row_number, ' '.join(row)))
            row_number += 1
        print(f'\nLIVES REMAINING: {self.lives}\n')

    # Checks if the ships fits to the board

    def check_ship_fits(self, ship_length, row, column, orientation):
        if orientation == 'H':
            if column + ship_length > 10:
                if self.user == 'player':
                    print('SHIP DOES NOT FIT, TRY AGAIN SIR!\n')
                    return False
                else:
                    return False
            else:
                return True
        else:
            if row + ship_length > 10:
                if self.user == 'player':
                    print('SHIP DOES NOT FIT, TRY AGAIN SIR!\n')
                    return False
                else:
                    return False
            else:
                return True

    #  Check for ships collision after placement

    def collision_check(self, board, row, column, orientation, ship_length):
        if orientation == 'H':
            for i in range(column, column + ship_length):
                if board[row][i] == SHIP:
                    if self.user == 'player':
                        print('\nA SHIP IS ALREADY PLACED WITHIN THESE CO-ORDINATES.')
                        print('TRY AGAIN SIR!\n')
                        return True
                    else:
                        return True
        else:
            for i in range(row, row + ship_length):
                if board[i][column] == SHIP:
                    if self.user == 'player':
                        print('\nA SHIP IS ALREADY PLACED WITHIN THESE CO-ORDINATES.')
                        print('TRY AGAIN SIR!\n')
                        return True
                    else:
                        return True
        return False


run_game()