import unittest
from maximum_gold import maximum_gold


class MaximumGold(unittest.TestCase):
    def test(self):
        for capacity, weights, answer in (
            (10, (1, 4, 8), 9),
            (20, (5, 7, 12, 18), 19),
            (10, (3, 5, 3, 3, 5), 10),
            ((1, 2, 3), (2, 1, 3), (1, 3, 5), 2),
            ((8, 3, 2, 1, 7), (8, 2, 1, 3, 8, 10, 7), (6, 8, 3, 1, 4, 7), 3),
            ((1, 1, 1), (1, 1, 1), (1, 1, 1), 3),
            ((1, 2, 3), (4, 5, 6), (7, 8, 9), 0),
        ):
            self.assertEqual(maximum_gold(capacity, weights), answer)


if __name__ == '__main__':
    unittest.main()
