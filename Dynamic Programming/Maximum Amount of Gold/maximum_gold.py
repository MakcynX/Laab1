# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)


    dp = [False] * (capacity + 1)
    dp[0] = True

    for weight in weights:
        for w in range(capacity, weight - 1, -1):
            if dp[w - weight]:
                dp[w] = True

    for w in range(capacity, -1, -1):
        if dp[w]:
            return w

    return 0


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
