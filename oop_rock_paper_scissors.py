""" Object-Oriented Rock Paper Scissors """

import random


class User(object):

    user_score = 0
    computer_score = 0

    valid_choices = ["rock", "paper", "scissors"]

    def __init__(self):
        self.choice = ''

    # prompt user input
    def prompt_move(self):
        user_choice = input("Choose rock, paper, or scissors: ")
        self.choice = user_choice

    # return user move
    def move(self):
        return self.choice


class NPCUser(User):

    # get random computer move
    def move(self):
        self.choice = random.choice(self.valid_choices)
        return self.choice


def play():

    user = User()
    user.prompt_move()
    user.move()

    computer = NPCUser()
    computer.move()


if __name__ == "__main__":
    play()
