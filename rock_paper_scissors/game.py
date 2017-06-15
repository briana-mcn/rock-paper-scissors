from rock_paper_scissors.valid_choices import VALID_CHOICES


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