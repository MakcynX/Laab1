# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    num_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        num_ops[i] = num_ops[i - 1] + 1

        if i % 2 == 0:
            num_ops[i] = min(num_ops[i], num_ops[i // 2] + 1)

        if i % 3 == 0:
            num_ops[i] = min(num_ops[i], num_ops[i // 3] + 1)

    sequence = []
    current = n
    while current >= 1:
        sequence.append(current)
        if current == 1:
            break

        if num_ops[current] == num_ops[current - 1] + 1:
            current -= 1
        elif current % 2 == 0 and num_ops[current] == num_ops[current // 2] + 1:
            current //= 2
        else:
            current //= 3

    return list(reversed(sequence))


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
