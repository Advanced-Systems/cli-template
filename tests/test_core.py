import unittest

from src.clitemplate import core

class TestCore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # load test data or instantiate objects
        pass

    @classmethod
    def tearDownClass(cls):
        # close file stream or destroy objects
        pass

    def test_square_function(self):
        min_x, max_x = 2, 6
        expected = [4, 9, 16, 25, 36]
        self.assertEqual(list(core.square_function(min_x, max_x)), expected, msg=f"Range: [{min_x},{max_x}]")