# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments.sort(key=lambda x: x.end)
    points = []

    if not segments:
        return points

    current_point = segments[0].end
    points.append(current_point)

    for s in segments:
        if s.start > current_point:
            current_point = s.end
            points.append(current_point)

    return points

if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
