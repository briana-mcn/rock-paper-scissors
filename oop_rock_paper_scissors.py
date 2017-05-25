""" Object-Oriented Rock Paper Scissors """

import random


class Move(object):

    def __eq__(self, other):
        if type(self) == type(other):
            return True
        return False


class Scissors(Move):

    def __gt__(self, other):
        if isinstance(other, Paper):
            return True
        return False

    def __lt__(self, other):
        if isinstance(other, Rock):
            return True
        return False


class Paper(Move):

    def __gt__(self, other):
        if isinstance(other, Rock):
            return True
        return False

    def __lt__(self, other):
        if isinstance(other, Scissors):
            return True
        return False


class Rock(Move):

    def __gt__(self, other):
        if isinstance(other, Scissors):
            return True
        return False

    def __lt__(self, other):
        if isinstance(other, Paper):
            return True
        return False


class User(object):

    def __init__(self):
        self.score = 0
        self.choice = None

    def get_move(self):
        user_choice = input('Choose rock, paper, or scissors: ')
        self.choice = user_choice

    def play_move(self):
        return self.choice


class NPCUser(User):

    def get_move(self):
        computer_choice = random.choice(('rock', 'paper', 'scissors'))
        self.choice = computer_choice


class Game(object):

    def __init__(self):
        self.rounds = 0

    # function to convert input to Move instance
    def convert_input_to_move(self, input_str):
        if input_str == 'rock':
            return Rock()
        elif input_str == 'paper':
            return Paper()
        elif input_str == 'scissors':
            return Scissors()
        else:
            print('Invalid Input')
            exit()

    # check for odd number of rounds
    def get_rounds(self):
        rounds = int(input('How many odd rounds would you like to play? '))
        self.rounds = rounds

    def return_rounds(self):
        return self.rounds


def main():

    user = User()
    computer = NPCUser()
    game = Game()

    # prompt human user for rounds
    game.get_rounds()

    # get original round input for functionality of odd round game play
    original_rounds = game.return_rounds()

    if original_rounds % 2 != 0:
        pass
    else:
        print('Please enter odd number of rounds.')
        exit()

    # loop for main game for each round
    # first user to score (2 divided by original rounds) wins
    while original_rounds/2 > user.score and original_rounds/2 > computer.score:

        # get user choice
        # convert string choice to class instance
        user.get_move()
        print('User input: ' + user.choice)
        user_input = game.convert_input_to_move(user.play_move())

        # get computer choice
        # convert string to class instance
        computer.get_move()
        print('Computer input: ' + computer.choice)
        computer_input = game.convert_input_to_move(computer.play_move())

        # main game play comparison operations
        if user_input == computer_input:
            print('Tie')
        elif user_input < computer_input:
            print('Computer wins')
            computer.score += 1
        else:
            print('User wins')
            user.score += 1

        # print score
        print('User Score: ' + str(user.score) + ' Computer Score:  ' + str(computer.score))

    # determine winner
    if user.score == computer.score:
        game.rounds += 1
    elif user.score > computer.score:
        print('User wins game!')
    else:
        print('Computer wins game!')

if __name__ == '__main__':
    main()

