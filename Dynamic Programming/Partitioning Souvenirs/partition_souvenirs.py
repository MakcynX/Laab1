from itertools import product
from sys import stdin


def partition3_naive(values):
    for c in product(range(3), repeat=len(values)):
        sums = [0] * 3
        for i in range(3):
            sums[i] = sum(values[k] for k in range(len(values)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    total_sum = sum(values)
    if total_sum % 3 != 0 or len(values) < 3:
        return 0

    target = total_sum // 3
    memo = {}

    def can_partition(idx, s1, s2):
        state = (idx, s1, s2)
        if state in memo:
            return memo[state]

        if s1 == target and s2 == target:
            return 1

        if idx == len(values) or s1 > target or s2 > target:
            return 0

        if can_partition(idx + 1, s1 + values[idx], s2):
            memo[state] = 1
            return 1

        if can_partition(idx + 1, s1, s2 + values[idx]):
            memo[state] = 1
            return 1

        if can_partition(idx + 1, s1, s2):
            memo[state] = 1
            return 1

        memo[state] = 0
        return 0

    return can_partition(0, 0, 0)


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
