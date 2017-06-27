class RockPaperScissorsError(Exception):
    """Base exception class for errors raised by rock paper scissors program."""
    pass


class UserDefinedError(ProgramError):
    """Raised for all user input errors."""
    pass


class UserChoiceInputError(UserDefinedError):
    """Raised for invalid User sting input."""
    def __init__(self, message):
        self.message = message


class UserRoundsInputError(UserDefinedError):
    """Raised for invalid rounds input."""
    pass


class RoundsStringError(UserRoundsInputError):
    """Raised if rounds input is a string."""
    def __init__(self, message):
        self.message = message


class RoundsEvenError(UserRoundsInputError):
    """Raised if rounds input is even."""
    def __init__(self, message):
        self.message = message


class RoundsNegativeError(UserRoundsInputError):
    """Raised if rounds input is less than 0."""
    def __init__(self, message):
        self.message = message


class RoundsGreaterThan100(UserRoundsInputError):
    """Raised if rounds input is greater than 100."""
    def __init__(self, message):
        self.message = message


class InstanceNotMoveError(ProgramError):
    """Raised if conversion from user input to Move instance failed."""
    def __init__(self, message):
        self.message = message
