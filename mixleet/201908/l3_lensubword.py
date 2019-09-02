# coding: utf-8
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""
from collections import defaultdict


def get_max_subword(str_: str):
    word_to_index = defaultdict(list)
    for i, c in enumerate(str_):
        word_to_index[c].append(i)


def get_max_subword(str_: str):
    if not str_:
        return 0

    max_len = defaultdict(int)
    max_len[0] = 1
    for i in range(1, len(str_)):
        for j in range(i-1, i-max_len[i-1]-1, -1):
            if str_[i] == str_[j]:
                max_len[i] = i - j
                break
        else:
            max_len[i] = max_len[i-1] + 1

    return max(max_len.values())



def test():
    assert get_max_subword('bbb') == 1
    assert get_max_subword('b') == 1
    assert get_max_subword('') == 0
    assert get_max_subword('abcabcbb') == 3
    assert get_max_subword('pwwkew') == 3
    assert get_max_subword('abcd') == 4
    assert get_max_subword('abcdee') == 5


if __name__ == '__main__':
    """
    python -m mixleet.201908.l3_lensubword test
    """
    from fire import Fire
    Fire()