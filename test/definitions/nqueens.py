import unittest
from search.definitions.nqueens import Queens


class QueensTest(unittest.TestCase):

    def setUp(self) -> None:
        self.queen = Queens(4)

    def test_init(self):
        self.assertEqual(4, self.queen.N)
