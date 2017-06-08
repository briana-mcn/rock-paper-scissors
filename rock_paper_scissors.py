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


VALID_CHOICES = {
    'rock': Rock(),
    'paper': Paper(),
    'scissors': Scissors()
}


class User(object):

    def __init__(self):
        self.score = 0
        self._choice = None

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        if value in VALID_CHOICES:
            move = self.convert_input_to_move(value)
            self._choice = move
        else:
            print('Invalid Input')
            exit()

    @staticmethod
    def convert_input_to_move(user_input):
        return VALID_CHOICES.get(user_input)


class Game(object):

    def __init__(self, player1, player2):
        self._rounds = 0
        self.player1 = player1
        self.player2 = player2

    @property
    def rounds(self):
        return self._rounds

    @rounds.setter
    def rounds(self, value):

            try:
                value = int(value)
            except ValueError:
                print('Input cannot be a string')
                return

            try:
                assert value % 2 != 0
            except AssertionError:
                print('Please enter an odd number of rounds')
                return

            try:
                assert value > 0
            except AssertionError:
                print('Please enter a number greater than zero')
                return

            self._rounds = value

    @property
    def valid_choices(self):
        return tuple(VALID_CHOICES.keys())

    def play(self):

        print('User Input: {} '
              'Computer Input: {}'.format(self.player1.choice,
                                          self.player2.choice
                                          )
              )

        if self.player1.choice == self.player2.choice:
            print('Tie')
        elif self.player1.choice < self.player2.choice:
            print('Computer wins')
            self.player2.score += 1
        else:
            print('User wins')
            self.player1.score += 1

        print('User Score: {} '
              'Computer Score: {}'.format(self.player1.score,
                                          self.player2.score
                                          )
              )

    def determine_winner(self):
        if self.player1.score > self.player2.score:
            print('User wins game!')
        elif self.player1.score < self.player2.score:
            print('Computer wins game!')
        else:
            return None

    @property
    def is_complete(self):
        if self.rounds > (self.player1.score + self.player2.score):
            return False
        else:
            return True


def main():

    user = User()
    computer = User()

    game = Game(user, computer)

    while game.rounds == 0:
        game.rounds = input('How many odd rounds would you like to play? ')

    while not game.is_complete:
        user.choice = input('Choose from the following: {}: '.format(', '.join(game.valid_choices)))
        computer.choice = random.choice(game.valid_choices)
        game.play()

    game.determine_winner()


if __name__ == '__main__':
    main()
