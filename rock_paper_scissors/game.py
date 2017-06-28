from rock_paper_scissors.valid_choices import VALID_CHOICES
from rock_paper_scissors import exc


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
            raise exc.InvalidRoundsError('Choice must be an integer')

        try:
            assert value % 2 != 0
        except AssertionError:
            raise exc.InvalidRoundsError('Choice must be an odd number')

        try:
            assert value > 0
        except AssertionError:
            raise exc.InvalidRoundsError('Choice must be greater than zero')

        self._rounds = value

    @property
    def valid_choices(self):
        return tuple(VALID_CHOICES.keys())

    @staticmethod
    def convert_input_to_move(user_input):
        try:
            move = VALID_CHOICES[user_input]
        except KeyError:
            raise exc.InvalidChoiceError('Choice must be a valid key')

        return move

    def play(self):
        if self.player1.choice == self.player2.choice:
            return 'Tie'
        elif self.player1.choice < self.player2.choice:
            self.player2.score += 1
            return '{} wins'.format(self.player2.name)
        else:
            self.player1.score += 1
            return '{} wins'.format(self.player1.name)

    def determine_winner(self):
        if self.player1.score > self.player2.score:
            return '{} wins game!'.format(self.player1.name)
        elif self.player1.score < self.player2.score:
            return '{} wins game!'.format(self.player2.name)
        else:
            return None

    @property
    def is_complete(self):
        if self.rounds > (self.player1.score + self.player2.score):
            return False
        else:
            return True
