"""Object-Oriented Rock Paper Scissors"""
import random

from rock_paper_scissors.user import User

from rock_paper_scissors.game import Game

from rock_paper_scissors import exc


def human_input_to_move(game, human):
    choices = ', or '.join(
        [
            ', '.join(game.valid_choices[:-1]),
            game.valid_choices[-1]
        ]
    )

    try:
        return game.convert_input_to_move(input('Choose {}: '.format(choices)))
    except exc.InputError:
        print('Input from {} is invalid. Please enter a valid choice'.format(human))
        return human_input_to_move(game, human)


def computer_input_to_move(game):
    return game.convert_input_to_move(random.choice(game.valid_choices))


def players_input(human, computer):
    players_input_store = []
    for player in human, computer:
        players_input_store.append('{} Input: {}'.format(player.name, player.choice))

    return '\n'.join(players_input_store)


def players_score(human, computer):
    players_score_store = []
    for player in human, computer:
        players_score_store.append('{} Score: {}'.format(player.name, player.score))

    return '\n'.join(players_score_store)


def main():
    human = User('Human')
    computer = User('Computer')
    game = Game(human, computer)

    while game.rounds == 0:
        try:
            game.rounds = input('How many odd rounds would you like to play? ')
        except exc.InputError as e:
            print('Rounds choice is invalid')
            print(e)
            continue

    while not game.is_complete:
        human.choice = human_input_to_move(game, human)
        computer.choice = computer_input_to_move(game)

        print(players_input(human, computer))
        print(game.play())
        print(players_score(human, computer))

    print(game.determine_winner())


if __name__ == '__main__':
    try:
        main()
    except exc.RockPaperScissorsError as e:
        print(e)
