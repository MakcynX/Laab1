# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    def get_fibonacci_sum_last_digit(n):
        if n < 0: return 0

        n_adj = (n + 2) % 60

        if n_adj <= 1:
            fib_n2 = n_adj
        else:
            prev, curr = 0, 1
            for _ in range(n_adj - 1):
                prev, curr = curr, (prev + curr) % 10
            fib_n2 = curr

        return (fib_n2 - 1) % 10

    sum_n = get_fibonacci_sum_last_digit(to_index)
    sum_m_minus_1 = get_fibonacci_sum_last_digit(from_index - 1)

    return (sum_n - sum_m_minus_1) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
