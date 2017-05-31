import unittest
from oop_rock_paper_scissors import Scissors, Paper, Rock, User, VALID_CHOICES

# write out all class method test cases for classes
# top to bottom of all classes, start each test
# main function test case


class MoveTest(unittest.TestCase):

    def test_eq_returns_true_if_type_of_instance_is_type_of_instance(self):
        scissors1 = Scissors()
        scissors2 = Scissors()
        self.assertIs(type(scissors1), type(scissors2))

    def test_eq_returns_false_if_type_of_instance_is_not_type_of_instance(self):
        scissors = Scissors()
        rock = Rock()
        self.assertIsNot(type(scissors), type(rock))


class ScissorsTest(unittest.TestCase):

    def test_gt_returns_true_if_paper(self):
        scissors = Scissors()
        paper = Paper()
        self.assertGreater(scissors, paper)

    def test_gt_returns_false_if_not_paper(self):
        scissors = Scissors()
        rock = Rock()
        self.assertLess(scissors, rock)

    def test_lt_returns_true_if_rock(self):
        scissors = Scissors()
        rock = Rock()
        self.assertLess(scissors, rock)

    def test_lt_returns_false_if_not_rock(self):
        scissors = Scissors()
        paper = Paper()
        self.assertGreater(scissors, paper)


class PaperTest(unittest.TestCase):

    def test_gt_returns_true_if_rock(self):
        paper = Paper()
        rock = Rock()
        self.assertGreater(paper, rock)

    def test_gt_returns_false_if_not_rock(self):
        paper = Paper()
        scissors = Scissors()
        self.assertLess(paper, scissors)

    def test_lt_returns_true_if_scissors(self):
        paper = Paper()
        scissors = Scissors()
        self.assertLess(paper, scissors)

    def test_lt_returns_false_if_not_scissors(self):
        paper = Paper()
        rock = Rock()
        self.assertGreater(paper, rock)


class RockTest(unittest.TestCase):

    def test_gt_returns_true_if_scissors(self):
        rock = Rock()
        scissors = Scissors()
        self.assertGreater(rock, scissors)

    def test_gt_returns_false_if_not_scissors(self):
        rock = Rock()
        paper = Paper()
        self.assertLess(rock, paper)

    def test_lt_returns_true_if_paper(self):
        rock = Rock()
        paper = Paper()
        self.assertLess(rock, paper)

    def test_lt_returns_false_if_not_paper(self):
        rock = Rock()
        scissors = Scissors()
        self.assertGreater(rock, scissors)


class UserTest(unittest.TestCase):
    # init method

    def test_get_move_if_user_choice_in_valid_choices(self):
        user_choice = 'rock'
        self.assertIn(user_choice, VALID_CHOICES)

    def test_get_move_if_user_choice_not_in_valid_choices(self):
        user_choice = 'choice'
        self.assertNotIn(user_choice, VALID_CHOICES)

    def test_play_move_returns_choice(self):
        pass

    def test_convert_input_to_move_if_user_choice_rock(self):
        pass

    def test_convert_input_to_move_if_user_choice_paper(self):
        pass

    def test_convert_input_to_move_if_user_choice_scissors(self):
        pass


class NPCUserTest(unittest.TestCase):

    def test_get_move_if_computer_choice_in_valid_choices(self):
        computer_choice = 'rock'
        self.assertIn(computer_choice, VALID_CHOICES)


class GameTest(unittest.TestCase):

    def test_get_rounds_if_rounds_is_odd(self):
        self.rounds = 3
        self.assertTrue(self.rounds % 2 != 0)

    def test_get_rounds_if_rounds_is_even(self):
        self.rounds = 4
        self.assertFalse(self.rounds % 2 != 0)


# isinstance need a unit test?
# FIXME use opposing assert method
# sanitize RPS classes?

