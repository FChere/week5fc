import unittest
import logic

class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            'x', None, '0',
            [None, 'x', None],
            [None, '0', 'x'],
        ]

        self.assertEqual(logic.get_winner(board), 'x')

        #TODO: Test all functions from logic.py!

if __name__== '__main__':
    unittest.main()
