class RockPaperScissorsError(Exception):
    """Base exception class for errors raised by rock paper scissors program."""
    pass


class InputError(RockPaperScissorsError):
    """Raised for all user input errors."""
    pass


class InvalidChoiceError(InputError):
    """Raised for invalid User string input."""
    pass


class InvalidRoundsError(InputError):
    """Raised for invalid rounds input."""
    pass


class InstanceNotMoveError(RockPaperScissorsError):
    """Raised if conversion from user input to Move instance failed."""
    def __init__(self, message):
        self.message = message
