# python3


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    digits = [int(dataset[i]) for i in range(0, len(dataset), 2)]
    ops = [dataset[i] for i in range(1, len(dataset), 2)]
    n = len(digits)

    min_val = [[0] * n for _ in range(n)]
    max_val = [[0] * n for _ in range(n)]

    for i in range(n):
        min_val[i][i] = digits[i]
        max_val[i][i] = digits[i]

    def get_min_max(start, end):
        res_min = float('inf')
        res_max = float('-inf')
        for k in range(start, end):
            op = ops[k]
            a = eval(f"{max_val[start][k]} {op} {max_val[k+1][end]}")
            b = eval(f"{max_val[start][k]} {op} {min_val[k+1][end]}")
            c = eval(f"{min_val[start][k]} {op} {max_val[k+1][end]}")
            d = eval(f"{min_val[start][k]} {op} {min_val[k+1][end]}")
            res_min = min(res_min, a, b, c, d)
            res_max = max(res_max, a, b, c, d)
        return res_min, res_max

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_val[i][j], max_val[i][j] = get_min_max(i, j)

    return max_val[0][n-1]


if __name__ == "__main__":
    print(find_maximum_value(input()))
