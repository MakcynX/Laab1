import unittest
from organizing_lottery import points_cover, points_cover_naive

from random import randint
class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([0, 5], [7, 10], [1, 6, 11]),
            ([-10], [10], [-100, 100, 0]),
            ([0, 3, 7], [5, 2, 10], [1, 6]),
            ([1, 2, 3], [1, 2, 3], [1, 2, 3, 4]),
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        for n_segments, n_points in [(10, 10), (100, 100)]:
            starts = [randint(-10**8, 10**8) for _ in range(n_segments)]
            ends = [s + randint(0, 10**6) for s in starts]
            points = [randint(-10**8, 10**8) for _ in range(n_points)]
            self.assertEqual(points_cover(starts, ends, points),
                             points_cover_naive(starts, ends, points))

    def test_large(self):
        n, m = 50000, 50000
        starts = [i for i in range(n)]
        ends = [i for i in range(n)]
        points = [i for i in range(m)]
        self.assertEqual(points_cover(starts, ends, points), [1] * m)


if __name__ == '__main__':
    unittest.main()
