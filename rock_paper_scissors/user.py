from valid_choices import VALID_CHOICES


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
