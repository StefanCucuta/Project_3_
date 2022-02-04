""" Battlefield Game """

# Libraires

import re
import random
import time

# Legend, Allows the game display to be updated with ease
EMPTY = '─'

# Coordinate doesn't hold ship/hasn't been guessed
SHIP = '■'

# Coordinate holds a ship that has been attacked
HITSHIP = 'X'

# Coordinate that was guessed and resulted in miss
GUESSED = 'O'

# Used to separate the different phases of the game
PHASE = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'


def welcome_message():
    """ Welcome Message """
    print('\nWELCOME TO BATTLESHIPS GAME!')
    print('  IT MAY TAKE SOME TIME SO MAKE YOURSELF COMFORTABLE')
    print('\n THE BOARD IS A GRID OF 10X10 WITH FOUR SHIPS TO SINK')
    print('  EACH PLAYER HAS 15 LIVES, THEY LOSE 1 FOR EACH HIT\n')
    print('YOUR FLEET:')
    print('AIRCRAFT CARRIER - BATTLECRUISER - SUBMARINE - FRIGATE\n')
    print('LEGEND:\n')
    print(f"{EMPTY} IS FOR AN EMPTY OR CO-ORDINATE THAT HASN'T BEEN GUESSED")
    print(f'{SHIP} REPRESENTS A SHIP')
    print(f'{HITSHIP} REPRESENTS A HIT OR SUNK SHIP')
    print(f'{GUESSED} IS FOR A CO-ORDINATE THAT HAS BEEN GUESSED\n')
    print("    NOW LET'S CHOESE THE NAME OF THE CAPTAIN")


def validate_team_name(name):
    """ Validate the name of the team """
    if not re.match('^[A-Za-z0-9_]*$', name):
        print('INVALID NAME. LETTERS, NUMBERS AND UNDERSCORES ONLY')
        return False
    elif len(name) > 10:
        print('INVALID NAME. 10 CHARACTERS MAX')
        return False
    elif len(name) == 0:
        print('INVALID NAME. NOT LONG ENOUGH')
    else:
        return True


def name_input():
    """Collects the user name input"""

    print('NAME CAN BE 10 CHARACTERS MAX. LETTERS, NUMBERS & UNDERSCORES ONLY')
    while True:
        player_name = input('ENTER YOUR NAME CAPTAIN!:\n')
        if validate_team_name(player_name):
            break
    print(f'\nTHE NAME YOU CHOSE IS: {player_name}\n')
    print(PHASE)
    time.sleep(1)
    print(' ')
    return player_name

# Game Board


class GameBoard:
    """ Game Board """
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
        """ Prints the required board to the terminal."""
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
        """Holds the logic to check if the placed ship fits."""
        if orientation == 'H':
            if column + ship_length > 10:
                if self.user == 'player':
                    print('CAPTAIN,THE SHIP DOES NOT FIT, TRY AGAIN SIR!\n')
                    return False
                else:
                    return False
            else:
                return True
        else:
            if row + ship_length > 10:
                if self.user == 'player':
                    print('CAPTAIN,THE SHIP DOES NOT FIT, TRY AGAIN SIR!\n')
                    return False
                else:
                    return False
            else:
                return True

    #  Check for ships collision after placement

    def collision_check(self, board, row, column, orientation, ship_length):
        """Holds the logic to check for ship collisions upon placement."""
        if orientation == 'H':
            for i in range(column, column + ship_length):
                if board[row][i] == SHIP:
                    if self.user == 'player':
                        print('\nALREADY PLACED WITHIN THESE CO-ORDINATES.')
                        print('TRY AGAIN SIR!\n')
                        return True
                    else:
                        return True
        else:
            for i in range(row, row + ship_length):
                if board[i][column] == SHIP:
                    if self.user == 'player':
                        print(
                            '\nALREADY PLACED WITHIN THESE CO-ORDINATES.')
                        print('TRY AGAIN SIR!\n')
                        return True
                    else:
                        return True
        return False

    # Prints out which ship they are placing.

    def ship_prompt(self, ship_length):
        """Prints out to the user which ship they are placing."""
        print('THE SAME POINT CANNOT BE USED TWICE!')
        print('HORIZONTAL AND VERTICAL PLACEMENT ONLY.')
        if ship_length == 6:
            print('PLEASE PLACE THE AIRCRAFT CARRIER (1x6)\n')
        elif ship_length == 4:
            print('PLEASE PLACE THE CRUISER (1x4)\n')
        elif ship_length == 3:
            print('PLEASE PLACE THE DESTROYER (1x3)\n')
        elif ship_length == 2:
            print('PLEASE PLACE THE ASSAULT SHIP (1x2)\n')

    def ship_input(self):
        """Collects the users desired"""
        while True:
            try:
                orientation = input('ENTER ORIENTATION (H OR V): \n').upper()
                if orientation == 'H' or orientation == 'V':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('PLEASE ENTER A VALID ORIENTATION')
        while True:
            try:
                column = input('ENTER DESIRED COLUMN (A-J): \n').upper()
                if not re.match('^[A-J]*$', column):
                    print('PLEASE ENTER A VALID LETTER BETWEEN A-J')
                else:
                    column = self.letters_to_numbers[column]
                    break
            except KeyError:
                print('PLEASE ENTER A LETTER')
        while True:
            try:
                row = input('ENTER DESIRED ROW (0-9): \n')
                if row in self.row_input:
                    row = int(row)
                    break
                else:
                    raise ValueError
            except ValueError:
                print('PLEASE ENTER A VALID NUMBER BETWEEN 0-9')
        return orientation, column, row

    # Place ships randomly on the computer board

    def place_ships(self):
        """Places the ships randomly on the computers board"""
        length_of_ships = [6, 4, 3, 2]

        for ship_length in length_of_ships:
            while True:
                if self.user == 'computer':
                    orientation = random.choice(['H', 'V'])
                    row = random.randint(0, 9)
                    column = random.randint(0, 9)
                    if self.check_ship_fits(
                        ship_length, row, column, orientation
                    ):
                        if self.collision_check(
                            self.board, row, column, orientation, ship_length
                        ) is False:
                            if orientation == 'H':
                                for i in range(column, column + ship_length):
                                    self.board[row][i] = SHIP
                            else:
                                for i in range(row, row + ship_length):
                                    self.board[i][column] = SHIP
                            break
                else:
                    if self.user == 'player':
                        self.ship_prompt(ship_length)
                        orientation, column, row = self.ship_input()
                        if self.check_ship_fits(
                            ship_length, row, column, orientation
                        ):
                            if self.collision_check(
                                self.board,
                                row,
                                column,
                                orientation,
                                ship_length
                            ) is False:
                                if orientation == 'H':
                                    for i in range(
                                        column, column + ship_length
                                    ):
                                        self.board[row][i] = SHIP
                                else:
                                    for i in range(row, row + ship_length):
                                        self.board[i][column] = SHIP
                                print(' ')
                                self.print_board()
                                break

    # Returns a random int between 1 and 2.

    def random_attk_int(self):
        """Returns a random int between 1 and 2"""
        attk_random = random.randint(1, 2)
        return attk_random

    # Holds the logic for computers attack horisontaly and verticaly.

    def comp_attack_column(self):
        """Holds the logic for computers attack"""
        column_hit = self.column_arry[-1]
        if column_hit == 10:
            column = random.randint(0, 9)
            return column
        else:
            attk_random = self.random_attk_int()
            if attk_random == 1:
                column = column_hit + 1
                return column
            elif attk_random == 2:
                column = column_hit - 1
                return column

    def comp_attack_row(self):
        """Holds the logic for computers attack"""
        row_hit = self.row_arry[-1]
        if row_hit == 10:
            row = random.randint(0, 9)
            return row
        else:
            attk_random = self.random_attk_int()
            if attk_random == 1:
                row = row_hit + 1
                return row
            elif attk_random == 2:
                row = row_hit - 1
                return row

    # Allows the player to input their desired attack co-ordinates.

    def attack_input(self):
        """Allows the player to input their desired attack co-ordinates."""
        while True:
            if self.user == 'player':
                print("ITS YOUR TURN TO ATTACK!\n")
                try:
                    column = input('ENTER DESIRED COLUMN (A-J): \n').upper()
                    if not re.match('^[A-J]*$', column):
                        print('PLEASE ENTER A VALID LETTER BETWEEN A-J')
                    else:
                        column = self.letters_to_numbers[column]
                        break
                except KeyError:
                    print('PLEASE ENTER A LETTER')
            elif self.user == 'computer guess':
                column = self.comp_attack_column()
                if column == range(0, 10):
                    break
                else:
                    column = random.randint(0, 9)
                    break
        while True:
            if self.user == 'player':
                try:
                    row = input('ENTER DESIRED ROW (0-9): \n')
                    if row in self.row_input:
                        row = int(row)
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('PLEASE ENTER A VALID NUMBER BETWEEN 0-9')
            elif self.user == 'computer guess':
                row = self.comp_attack_row()
                if row == range(0, 10):
                    break
                else:
                    row = random.randint(0, 9)
                    break
        return column, row

    # Updates the lives of the respective player.

    def lives_counter(self):
        """Updates the lives of the player, runs each time a ship is hit"""
        count = 15
        for row in self.board:
            for column in row:
                if column == HITSHIP:
                    count -= 1
                    self.lives = count
        return self.lives

    def check_miss_count(self):
        """Returns the last four values of attk_arry."""
        first = self.attk_arry[-1]
        second = self.attk_arry[-2]
        third = self.attk_arry[-3]
        fourth = self.attk_arry[-4]
        sum_of_attk = first + second + third + fourth
        if sum_of_attk == 8:
            self.column_arry.append(10)
            self.row_arry.append(10)
        else:
            pass

# Loops until a player is out of lives.


def run_game(player_board, user_guess, computer_board, computer_guess):
    """Loops until a player is out of lives."""
    player_turn = 0
    computer_turn = 1
    player_lives = 15
    computer_lives = 15
    while True:
        if player_turn < computer_turn:
            user_guess.print_board()
            column, row = player_board.attack_input()
            if user_guess.board[row][column] == GUESSED:
                print('\nYOU HAVE ALREADY GUESSED THIS CO-ORDINATE\n')
            elif user_guess.board[row][column] == HITSHIP:
                print('\nYOU HAVE ALREADY HIT A SHIP IN THIS CO-ORDINATE\n')
            elif computer_board.board[row][column] == SHIP:
                print(' ')
                print(PHASE)
                print('\nCONGRATULATIONS, YOU HIT A SHIP!\n')
                user_guess.board[row][column] = HITSHIP
                player_turn += 1
                user_guess.lives_counter()
                user_guess.print_board()
                computer_lives -= 1
                print("COMPUTER'S TURN TO ATTACK!")
                time.sleep(3)
                if computer_lives == 0:
                    print('\nTHE COMPUTER HAS NO LIVES LEFT!')
                    print('YOU WIN!')
                    print('🄴🄽🄴🄼🅈 🄳🄸🅂🅃🅁🄾🄴🄳')
                    print(' ')
                    print(PHASE)
                    break
            else:
                print(' ')
                print(PHASE)
                print('\nYOU MISSED!\n')
                user_guess.board[row][column] = GUESSED
                player_turn += 1
                user_guess.print_board()
                print("COMPUTER'S TURN TO ATTACK!")
                time.sleep(3)
        if computer_turn == player_turn:
            row, column = computer_guess.attack_input()
            if computer_guess.board[row][column] == GUESSED:
                pass
            elif computer_guess.board[row][column] == HITSHIP:
                pass
            elif player_board.board[row][column] == SHIP:
                print('THE COMPUTER HIT YOUR SHIP!\n')
                computer_turn += 1
                player_lives -= 1
                computer_guess.column_arry.append(column)
                computer_guess.row_arry.append(row)
                computer_guess.board[row][column] = HITSHIP
                player_board.board[row][column] = HITSHIP
                player_board.lives_counter()
                player_board.print_board()
                computer_guess.attk_arry.append(0)
                time.sleep(3)
                if player_lives == 0:
                    print('\nYOU HAVE NO LIVES LEFT!')
                    print('YOU LOSE!')
                    print('🄶🄰🄼🄴 🄾🅅🄴🅁')
                    print(' ')
                    print(PHASE)
                    break
            else:
                print('COMPUTER MISSED!\n')
                computer_guess.board[row][column] = GUESSED
                computer_turn += 1
                player_board.print_board()
                computer_guess.attk_arry.append(1)
                computer_guess.check_miss_count()
                time.sleep(3)

# Asks the player if they want to play again or quit


def play_again():
    """Asks the player if they want to play again or quit"""
    print('\nWOULD YOU LIKE TO PLAY AGAIN?')
    answer = input('ENTER Y OR N: \n').upper()
    print(' ')
    while True:
        if answer == "Y":
            print(PHASE)
            new_game()
        elif answer == "N":
            print(' ')
            print('GOODBYE!')
            print(' ')
            print(PHASE)
            return False
        else:
            print(' ')
            print('PLEASE ENTER Y OR N')
            answer = input('ENTER Y OR N: \n').upper()

# Start a new game.


def new_game():
    """Starts a new game"""
    welcome_message()
    player_name = name_input()
    player_board = GameBoard(player_name, 'player')
    user_guess = GameBoard('GUESS', 'user guess')
    computer_board = GameBoard("COMPUTER's", 'computer')
    computer_guess = GameBoard('COMPUTER GUESS', 'computer guess')
    computer_board.place_ships()
    player_board.print_board()
    player_board.place_ships()
    time.sleep(2)
    print(PHASE)
    print(' ')
    run_game(player_board, user_guess, computer_board, computer_guess)
    play_again()


new_game()
