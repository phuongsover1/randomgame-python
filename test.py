import unittest
import randomgame


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        min = 1
        max = 10
        result = randomgame.run_guess(guess, answer, min, max)
        self.assertEqual(result, True)

    def test_input_wrong_guess(self):
        result = randomgame.run_guess(5, 0, 0, 10)
        self.assertFalse(result)

    def test_input_wrong_guess1(self):
        result = randomgame.run_guess(-1, 0, 0, 10)
        self.assertFalse(result)

    def test_input_wrong_guess2(self):
        result = randomgame.run_guess(15, 0, 0, 10)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
