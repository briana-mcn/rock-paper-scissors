""" Object-Oriented Rock Paper Scissors """

import random


VALID_CHOICES = ('rock', 'paper', 'scissors')


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
        if user_choice in VALID_CHOICES:
            self.choice = user_choice
        else:
            print('Invalid Input')
            exit()

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

    def get_move_instance(self):
        return self.instance


class NPCUser(User):

    def get_move(self):
        computer_choice = random.choice(('rock', 'paper', 'scissors'))
        self.choice = computer_choice


class Game(object):

    def __init__(self, player1, player2):
        self.rounds = 0
        self.player1 = player1
        self.player2 = player2

    # check for odd number of rounds
    def get_rounds(self):
        rounds = int(input('How many odd rounds would you like to play? '))
        if rounds % 2 != 0:
            self.rounds = rounds
        else:
            print('Please enter odd number of rounds.')
            exit()

    def play(self):

        for player in self.player1, self.player2:
            player.get_move()
            player.convert_input_to_move()

        print('User Input: {} '
              'Computer Input: {}'.format(self.player1.choice,
                                          self.player2.choice))

        if self.player1.instance == self.player2.instance:
            print('Tie')
        elif self.player1.instance < self.player2.instance:
            print('Computer wins')
            self.player2.score += 1
        else:
            print('User wins')
            self.player1.score += 1

        print('User Score: {} '
              'Computer Score: {}'.format(self.player1.score,
                                          self.player2.score
                                          ))

    def determine_winner(self):
        if self.player1.score > self.player2.score:
            print('User wins game!')
        else:
            print('Computer wins game!')


def main():

    user = User()
    computer = NPCUser()
    game = Game(user, computer)
    game.get_rounds()

    while game.rounds > (game.player1.score + game.player2.score):

        game.play()

    game.determine_winner()


if __name__ == '__main__':
    main()
