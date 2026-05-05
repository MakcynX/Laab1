# python3


def edit_distance(first_string, second_string):
    n = len(first_string)
    m = len(second_string)

    d = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if first_string[i - 1] == second_string[j - 1] else 1

            d[i][j] = min(d[i - 1][j] + 1,
                          d[i][j - 1] + 1,
                          d[i - 1][j - 1] + cost)

    return d[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
