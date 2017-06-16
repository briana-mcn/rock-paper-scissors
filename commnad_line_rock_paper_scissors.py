"""Object-Oriented Rock Paper Scissors"""
import random

from rock_paper_scissors.user import User

from rock_paper_scissors.game import Game


def human_input_to_move(game, human):
    choices = ', or '.join(
        [
            ', '.join(game.valid_choices[:-1]),
            game.valid_choices[-1]
        ]
    )

    try:
        return game.convert_input_to_move(input('Choose {}: '.format(choices)))
    except Exception:
        print('Input from {} is invalid. Enter another choice'.format(human))
        return human_input_to_move(game, human)


def computer_input_to_move(game):
    return game.convert_input_to_move(random.choice(game.valid_choices))


def main():
    human = User('Human')
    computer = User('Computer')
    game = Game(human, computer)

    while game.rounds == 0:
        game.rounds = input('How many odd rounds would you like to play? ')

    while not game.is_complete:
        human_input_to_move(game, human)
        computer.choice = computer_input_to_move(game)

        game.print_players_menu('Input')
        game.play()
        game.print_players_menu('Score')

    game.determine_winner()


if __name__ == '__main__':
    main()
