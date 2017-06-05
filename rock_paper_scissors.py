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
        self._choice = None
        self.instance = None

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        if value in VALID_CHOICES:
            self._choice = value
        else:
            print('Invalid Input')
            exit()

    # def get_move(self):
    #     user_choice = input('Choose rock, paper, or scissors: ')
    #     if user_choice in VALID_CHOICES:
    #         self.choice = user_choice
    #     else:
    #         print('Invalid Input')
    #         exit()

    # def play_move(self):
    #     return self.choice

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

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        self._choice = value


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
        if value % 2 != 0:
            self._rounds = value
        else:
            print('Please enter odd number of rounds.')
            exit()

    # def play(self):
    #     while self.rounds > (self.player1.score + self.player2.score):
    #         self._play()

    def play(self):
        for player in self.player1, self.player2:
            # player.get_move()
            player.convert_input_to_move()

        print('User Input: {} '
              'Computer Input: {}'.format(self.player1.choice,
                                          self.player2.choice
                                          )
              )

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
                                          )
              )

    def determine_winner(self):
        if self.player1.score > self.player2.score:
            print('User wins game!')
        else:
            print('Computer wins game!')

    def is_complete(self):
        if self.rounds > (self.player1.score + self.player2.score):
            return False
        else:
            return True


def main():

    user = User()
    computer = NPCUser()

    game = Game(user, computer)

    game.rounds = int(input('How many odd rounds would you like to play? '))

    while not game.is_complete():
        user.choice = input('Choose rock, paper, or scissors: ')
        computer.choice = random.choice(VALID_CHOICES)
        game.play()

    game.determine_winner()


if __name__ == '__main__':
    main()








"""

rock_paper_scissors/
    __init__.py
    game.py
    user/
        user.py
        npcuser.py
    moves/
        move.py
        paper.py
        scissors.py
        rock.py
    test/
        test_rock_paper_scissors.py

"""
