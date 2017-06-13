""" Object-Oriented Rock Paper Scissors """

import random

from rock_paper_scissors.user import User

from rock_paper_scissors.game import Game


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
        human.choice = input('Choose {}: '.format(choices))
        computer.choice = random.choice(game.valid_choices)
        game.print_players_menu('Input')
        game.play()
        game.print_players_menu('Score')

    game.determine_winner()

if __name__ == '__main__':
    main()
