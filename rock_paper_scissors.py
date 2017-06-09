""" Object-Oriented Rock Paper Scissors """

import random


class Move(object):

    def __eq__(self, other):
        if type(self) is type(other):
            return True
        return False

    def __repr__(self):
        return self.__class__.__name__


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

    def __init__(self, name):
        self.score = 0
        self._choice = None
        self.name = name

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

    def print_players_menu(self, menu_word):
        for player in self.player1, self.player2:
            if menu_word == 'Input':
                print('{} {}: {}'.format(player.name, menu_word, player.choice))
            elif menu_word == 'Score':
                print('{} {}: {}'.format(player.name, menu_word, player.score))
            else:
                return None

    def play(self):

        if self.player1.choice == self.player2.choice:
            print('Tie')
        elif self.player1.choice < self.player2.choice:
            print('Computer wins')
            self.player2.score += 1
        else:
            print('Human wins')
            self.player1.score += 1

    def determine_winner(self):
        if self.player1.score > self.player2.score:
            print('Human wins game!')
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

    human = User('Human')
    computer = User('Computer')

    game = Game(human, computer)

    while game.rounds == 0:
        game.rounds = input('How many odd rounds would you like to play? ')

    while not game.is_complete:
        choices = ', or '.join(
            [
                ', '.join(game.valid_choices[:-1]),
                game.valid_choices[-1]
            ]
        )
        human.choice = input('Choose {}'.format(choices))
        computer.choice = random.choice(VALID_CHOICES)
        game.print_players_menu('Input')
        game.play()
        game.print_players_menu('Score')

    game.determine_winner()


if __name__ == '__main__':
    main()
