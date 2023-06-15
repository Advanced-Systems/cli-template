import unittest

from src.clitemplate import commands


class TestCore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_square_function(self):
        # arrange
        xmin, xmax = 2, 6

        # act
        result = list(commands.square_function(xmin, xmax))

        # assert
        self.assertEqual(result, [4, 9, 16, 25, 36], msg=f"Range: [{xmin},{xmax}]")
