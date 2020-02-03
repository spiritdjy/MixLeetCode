# coding: utf-8
"""
Change Coin For Money
"""


def get_coin_num(coin_list, money):
    if money in coin_list:
        return 1
    if money <= 0:
        return 0

    ret = [None]
    for i in range(1, money+1):
        curr_ = []
        for coin in coin_list:
            money_ = i - coin
            if money_ == 0:
                curr_.append(1)
            elif money_ >= 1:
                curr_.append(1+ret[money_])
            else:
                curr_.append(10000000000)
        ret.append(min(curr_))

    return ret[-1]


def test():
    assert get_coin_num([1,3,4], 3) == 1
    assert get_coin_num([1,3,4], 1) == 1
    assert get_coin_num([1,3,4], 2) == 2
    assert get_coin_num([1,3,4], 5) == 2
    assert get_coin_num([1,3,4], 6) == 2
    assert get_coin_num([1,3,4], 7) == 2
    assert get_coin_num([1,3,4], 8) == 2
    assert get_coin_num([1,3,4], 9) == 3
    assert get_coin_num([1,3,4], 10) == 3
    assert get_coin_num([1,3,4], 11) == 3
    assert get_coin_num([1,3,4], 12) == 3
    assert get_coin_num([1,3,4], 14) == 4
    assert get_coin_num([1,3,4], 15) == 4
    assert get_coin_num([1, 3, 4], 16) == 4


if __name__ == '__main__':
    """
    python -m mixleet.201908.num_coin test
    """
    from fire import Fire
    Fire()