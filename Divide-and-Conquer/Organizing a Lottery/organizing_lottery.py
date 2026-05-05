# python3
from sys import stdin



def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    count = [0] * len(points)
    events = []

    for s in starts:
        events.append((s, 1))
    for i, p in enumerate(points):
        events.append((p, 2, i))
    for e in ends:
        events.append((e, 3))

    events.sort()

    active_segments = 0
    for event in events:
        if event[1] == 1:
            active_segments += 1
        elif event[1] == 3:
            active_segments -= 1
        elif event[1] == 2:
            count[event[2]] = active_segments

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
