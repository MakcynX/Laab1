# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    current_n = n
    current_prize = 1

    while current_n > 0:

        if current_n <= 2 * current_prize:
            summands.append(current_n)
            break
        else:
            summands.append(current_prize)
            current_n -= current_prize
            current_prize += 1


    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
