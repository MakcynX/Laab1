# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    num_10 = money // 10
    money %= 10

    num_5 = money // 5
    money %= 5

    num_1 = money

    return num_10 + num_5 + num_1


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
