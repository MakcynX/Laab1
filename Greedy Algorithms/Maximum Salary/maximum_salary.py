# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers = [str(x) for x in numbers]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] + numbers[i] > numbers[i] + numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    res = "".join(numbers)

    return res


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
