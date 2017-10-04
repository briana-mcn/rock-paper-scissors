import unittest

from rock_paper_scissors.core.exc import InvalidRoundsError, InvalidChoiceError
from rock_paper_scissors.core.game import Game
from rock_paper_scissors.core.moves import Paper, Rock
from rock_paper_scissors.core.user import User
from rock_paper_scissors.core.valid_choices import VALID_CHOICES


class GameInitTestCase(unittest.TestCase):
    def test_player1_and_player2_and_starting_rounds_types(self):
        player1 = 'Joe'
        player2 = 'Jane'
        game = Game(player1, player2)

        self.assertIsInstance(game.player1, str)
        self.assertIsInstance(game.player2, str)
        self.assertEqual(game._rounds, 0)


class GameSetRoundsTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game('player1', 'player2')

    def test_valid_rounds_input(self):
        value = self.game.rounds = 11

        self.assertEqual(value, 11)

    def test_raises_error_if_round_not_an_int(self):
        with self.assertRaises(InvalidRoundsError) as ctx:
            self.game.rounds = 'a'

        self.assertEqual(
            str(ctx.exception),
            'Choice must be an integer'
        )

    def test_raises_error_if_value_is_not_odd(self):
        with self.assertRaises(InvalidRoundsError) as ctx:
            self.game.rounds = 2

        self.assertEqual(
            str(ctx.exception),
            'Choice must be an odd number'
        )

    def test_raises_error_if_value_is_not_positive(self):
        with self.assertRaises(InvalidRoundsError) as ctx:
            self.game.rounds = -1

        self.assertEqual(
            str(ctx.exception),
            'Choice must be greater than zero'
        )


class GameGetRoundsTestCase(unittest.TestCase):
    def test_return_rounds_of_game(self):
        self.game = Game('player1', 'player2')
        self.game._rounds = 1

        self.assertEqual(self.game.rounds, 1)


class GameValidChoicesTestCase(unittest.TestCase):
    def test_assert_tuple_of_valid_choices(self):
        self.game = Game('player1', 'player2')
        game_valid_choices = self.game.valid_choices

        self.assertIsInstance(game_valid_choices, tuple)
        self.assertCountEqual(game_valid_choices, tuple(VALID_CHOICES.keys()))


class GameConvertPlayerInputToMove(unittest.TestCase):
    def test_user_input_is_a_valid_string_for_conversion_to_move(self):
        self.game = Game('player1', 'player2')
        expected = VALID_CHOICES['rock']
        result = self.game.convert_input_to_move('rock')

        self.assertEqual(expected, result)

    def test_user_input_is_not_a_valid_string_for_conversion_to_object(self):
        self.assertRaises(InvalidChoiceError, Game.convert_input_to_move, 'fish')


class GamePlayLogicTestCase(unittest.TestCase):
    def setUp(self):
        player1 = User('Joe')
        player2 = User('Jane')
        self.game = Game(player1, player2)

    def test_player1_move_equals_player2_move_returns_tie(self):
        self.game.player1.choice = Rock()
        self.game.player2.choice = Rock()

        actual_tie = self.game.play()
        expected_tie = 'Tie'

        self.assertEqual(actual_tie, expected_tie)

    def test_player1_does_not_get_point_if_player1_move_equals_player2_move(self):
        self.game.player1.choice = Rock()
        self.game.player2.choice = Rock()
        self.game.play()

        actual_score = self.game.player1.score
        expected_score = 0

        self.assertEqual(actual_score, expected_score)

    def test_player2_does_not_get_point_if_player1_move_equals_player2_move(self):
        self.game.player1.choice = Rock()
        self.game.player2.choice = Rock()
        self.game.play()

        actual_score = self.game.player2.score
        expected_score = 0

        self.assertEqual(actual_score, expected_score)

    def test_player2_gets_point_if_player2_move_is_greater_than_player1_move(self):
        self.game.player1.choice = Rock()
        self.game.player2.choice = Paper()
        self.game.play()
        actual_score = self.game.player2.score
        expected_score = 1

        self.assertEqual(actual_score, expected_score)

    def test_player1_gets_no_point_if_player2_move_greater_than_player1_move(self):
        self.game.player1.choice = Rock()
        self.game.player2.choice = Paper()
        self.game.play()
        actual_score = self.game.player1.score
        expected_score = 0

        self.assertEqual(actual_score, expected_score)

    def test_player1_gets_point_if_player1_move_greater_than_player2_move(self):
        self.game.player1.choice = Paper()
        self.game.player2.choice = Rock()
        self.game.play()
        actual_score = self.game.player1.score
        expected_score = 1

        self.assertEqual(actual_score, expected_score)

    def test_player2_gets_no_point_if_player1_move_greater_than_player2_move(self):
        self.game.player1.choice = Paper()
        self.game.player2.choice = Rock()
        self.game.play()
        actual_score = self.game.player2.score
        expected_score = 0

        self.assertEqual(actual_score, expected_score)

    def test_player1_move_greater_than_player2_move_returns_winner_string(self):
        self.game.player1.choice = Paper()
        self.game.player2.choice = Rock()

        expected = '{} wins'.format(self.game.player1.name)
        actual = self.game.play()

        self.assertEqual(actual, expected)

    def test_player2_move_greater_than_player1_move_returns_winner_string(self):
        self.game.player1.choice = Rock()
        self.game.player2.choice = Paper()

        expected = '{} wins'.format(self.game.player2.name)
        actual = self.game.play()

        self.assertEqual(actual, expected)


class GameDetermineWinnerTestCase(unittest.TestCase):
    def setUp(self):
        player1 = User('Joe')
        player2 = User('Jane')
        self.game = Game(player1, player2)

    def test_player1_end_score_greater_than_player_2_end_score_returns_winner_string(self):
        self.game.player1.score = 2
        self.game.player2.score = 1

        expected = '{} wins game!'.format(self.game.player1.name)
        actual = self.game.determine_winner()

        self.assertEqual(expected, actual)

    def test_player2_end_score_greater_than_player_1_end_score_returns_winner_string(self):
        self.game.player1.score = 1
        self.game.player2.score = 2

        expected = '{} wins game!'.format(self.game.player2.name)
        actual = self.game.determine_winner()

        self.assertEqual(expected, actual)

    def test_player1_score_equals_player2_score_returns_none(self):
        self.game.player1.score = 0
        self.game.player2.score = 0

        expected = None
        actual = self.game.determine_winner()

        self.assertEqual(expected, actual)


class GameIsCompleteTestCase(unittest.TestCase):
    def setUp(self):
        player1 = User('Joe')
        player2 = User('Jane')
        self.game = Game(player1, player2)

    def test_rounds_greater_than_players_score_returns_false(self):
        self.game.rounds = 3
        self.game.player1.score = 1
        self.game.player2.score = 1

        self.assertFalse(self.game.is_complete)

    def test_rounds_less_than_combined_players_score_returns_false(self):
        self.game.rounds = 3
        self.game.player1.score = 1
        self.game.player2.score = 2

        self.assertTrue(self.game.is_complete)
