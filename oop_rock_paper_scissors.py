""" Object-Oriented Rock Paper Scissors """

import random


class Move(object):

    def __eq__(self, other):
        if type(self) is type(other):
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
        self.instance = None

    def get_move(self):
        user_choice = input('Choose rock, paper, or scissors: ')
        self.choice = user_choice

    def play_move(self):
        return self.choice

    # function to convert input to Move instance
    def convert_input_to_move(self):
        if self.choice == 'rock':
            self.instance = Rock()
        elif self.choice == 'paper':
            self.instance = Paper()
        elif self.choice == 'scissors':
            self.instance = Scissors()
        else:
            print('Invalid Input')
            exit()

    def get_move_instance(self):
        return self.instance


class NPCUser(User):

    def get_move(self):
        computer_choice = random.choice(('rock', 'paper', 'scissors'))
        self.choice = computer_choice


class Game(object):

    def __init__(self):
        self.rounds = 0

    # check for odd number of rounds
    def get_rounds(self):
        rounds = int(input('How many odd rounds would you like to play? '))
        if rounds % 2 != 0:
            self.rounds = rounds
        else:
            print('Please enter odd number of rounds.')
            exit()


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

        # get user move instance
        user.get_move()
        user.convert_input_to_move()
        user_instance = user.get_move_instance()

        # get computer move instance
        computer.get_move()
        computer.convert_input_to_move()
        computer_instance = computer.get_move_instance()

        print('User Input: {} Computer Input: {}'.format(user.choice, computer.choice))

        # main game play comparison operations
        if user_instance == computer_instance:
            print('Tie')
        elif user_instance < computer_instance:
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

