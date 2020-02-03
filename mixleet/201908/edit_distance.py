# coding: utf-8


def calc_distance(s, t):
    if s == '':
        return len(t)
    if t == '':
        return len(s)

    ret = [
        1 + calc_distance(s, t[1:]),
        1 + calc_distance(s[1:], t),
        calc_distance(s[1:], t[1:]) + (1 if s[0] != t[0] else 0)
    ]
    return min(ret)


def test():
    assert calc_distance('horse', 'ros') == 3
    assert calc_distance('intention', 'execution') == 5
    assert calc_distance('i', 'i') == 0





