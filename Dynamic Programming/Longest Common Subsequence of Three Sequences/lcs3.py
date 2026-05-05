# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    len_n, len_m, len_l = len(first_sequence), len(second_sequence), len(third_sequence)
    # Створюємо 3D масив розміром (n+1) x (m+1) x (l+1)
    dp = [[[0] * (len_l + 1) for _ in range(len_m + 1)] for _ in range(len_n + 1)]

    for i in range(1, len_n + 1):
        for j in range(1, len_m + 1):
            for k in range(1, len_l + 1):
                # Якщо елементи в усіх трьох послідовностях збігаються
                if first_sequence[i-1] == second_sequence[j-1] == third_sequence[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    # Інакше беремо максимум, ігноруючи по одному елементу з кожної черги
                    dp[i][j][k] = max(dp[i-1][j][k],
                                      dp[i][j-1][k],
                                      dp[i][j][k-1])
    return dp[len_n][len_m][len_l]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
