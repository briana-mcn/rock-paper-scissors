from rock_paper_scissors.moves import Move

from rock_paper_scissors import exc


class User(object):
    def __init__(self, name):
        self.score = 0
        self._choice = None
        self.name = name

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.name)

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        try:
            assert isinstance(value, Move)
        except AssertionError:
            raise InstanceNotMoveError('Choice must be an instance of Move')

        self._choice = value
