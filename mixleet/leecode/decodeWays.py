# coding: utf-8
"""
https://soulmachine.gitbooks.io/algorithm-essentials/content/cpp/dp/decode-ways.html
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12). The number of ways decoding "12" is 2
"""


def decode_ways_resc(str_):
    if str_ == '':
        return 1

    else:
        if str_[0] == '0':
            return 0

        a = decode_ways_resc(str_[1:])
        if len(str_) >= 2:
            if 0 < int(str_[:2]) <= 26:
                a += decode_ways_resc(str_[2:])

        return a


def decode_ways_plan(str_):
    if str_ == '':
        return 0

    if len(str_) == 1:
        return str_ != '0'

    pre_n = 1 if str_[0] != '0' else 0
    curr_n = all(i != '0' for i in str_[:2]) + (0 < int(str_[:2]) <= 26)

    for i in range(2, len(str_)):
        curr_n, pre_n = (curr_n if str_[i] != '0' else 0) + (pre_n if 0 < int(str_[i-1: i+1]) <= 26 else 0), curr_n

    return curr_n


decode_ways = decode_ways_plan


def test():
    assert decode_ways('120') == 1
    assert decode_ways('12') == 2
    assert decode_ways('10') == 1
    assert decode_ways('121') == 3
    assert decode_ways('12312') == 1 + 3 + 2



if __name__ == '__main__':
    """
    python -m mixleet.201908.decodeWays test
    """
    from fire import Fire
    Fire()