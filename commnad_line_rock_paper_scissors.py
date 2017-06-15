"""Object-Oriented Rock Paper Scissors"""
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
        validate_users_choice()

        game.print_players_menu('Input')
        game.play()
        game.print_players_menu('Score')

    game.determine_winner()


def validate_users_choice():
    choices = ', or '.join(
        [
            ', '.join(game.valid_choices[:-1]),
            game.valid_choices[-1]
        ]
    )

    p1 = input('Choose {}: '.format(choices))
    p2 = random.choice(game.valid_choices)

    for (player, choice) in ((game.player1, p1), (game.player2, p2)):
        try:
            player.choice = game.convert_input_to_move(choice)
        except Exception:
            print('Input from {} is invalid, enter another choice'.format(player))
            return validate_users_choice()

if __name__ == '__main__':
    main()
