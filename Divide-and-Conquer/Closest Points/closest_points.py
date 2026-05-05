# python3
import math
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared(points):
        points.sort(key=lambda p: p.x)
        return _closest_squared(points)

def _closest_squared(points_sorted_x):
    n = len(points_sorted_x)

    if n <= 3:
        return minimum_distance_squared_naive(points_sorted_x)

    mid = n // 2
    mid_point = points_sorted_x[mid]

    left_min = _closest_squared(points_sorted_x[:mid])
    right_min = _closest_squared(points_sorted_x[mid:])

    d_squared = min(left_min, right_min)
    d = math.sqrt(d_squared)

    strip = [p for p in points_sorted_x if abs(p.x - mid_point.x) < d]

    strip.sort(key=lambda p: p.y)

    min_strip = d_squared
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j].y - strip[i].y) >= d:
                break
            min_strip = min(min_strip, distance_squared(strip[i], strip[j]))

    return min(d_squared, min_strip)


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
