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
            raise Exception('Choice must be an integer')

        try:
            assert value % 2 != 0
        except AssertionError:
            raise Exception('Choice must be an odd number')

        try:
            assert value > 0
        except AssertionError:
            raise Exception('Choice must be greater than zero')

        self._rounds = value

    @property
    def valid_choices(self):
        return tuple(VALID_CHOICES.keys())

    @staticmethod
    def convert_input_to_move(user_input):
        try:
            move = VALID_CHOICES[user_input]
        except KeyError:
            raise Exception('Choice must be a valid key')

        return move

    @property
    def players_input(self):
        players_input_store = []
        for player in self.player1, self.player2:
            players_input_store.append('{} {}: {}'.format(player.name, 'Input', player.choice))

        return '\n'.join(players_input_store)

    @property
    def players_score(self):
        players_score_store = []
        for player in self.player1, self.player2:
            players_score_store.append('{} {}: {}'.format(player.name, 'Score', player.score))

        return '\n'.join(players_score_store)

    def play(self):
        if self.player1.choice == self.player2.choice:
            return 'Tie'
        elif self.player1.choice < self.player2.choice:
            self.player2.score += 1
            return 'Computer wins'
        else:
            self.player1.score += 1
            return 'Human wins'

    def determine_winner(self):
        if self.player1.score > self.player2.score:
            return 'Human wins game!'
        elif self.player1.score < self.player2.score:
            return 'Computer wins game!'
        else:
            return None

    @property
    def is_complete(self):
        if self.rounds > (self.player1.score + self.player2.score):
            return False
        else:
            return True
