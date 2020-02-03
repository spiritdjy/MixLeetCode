# coding: utf-8
"""
https://soulmachine.gitbooks.io/algorithm-essentials/content/cpp/string/longest-palindromic-substring.html
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""
from operator import itemgetter


def is_huiwen(str_):
    return str_ == ''.join(reversed(str_))


def do(str_):
    """
    n**3
    :param str_:
    :return:
    """
    len_ = len(str_)
    max_str = ''
    max_len = 0
    for i in range(0, len_):
        for j in range(len_, i, -1):
            if is_huiwen(str_[i:j]):
                if j - i > max_len:
                    max_len = j-i
                    max_str = str_[i:j]

    return max_str


def get_long(str_a, str_b):
    ret = ''
    for i, j in zip(str_a, str_b):
        if i == j:
            ret += i
        else:
            break
    return ret


def do(str_):
    str_o = ''.join(reversed(str_))
    max_num = 0
    max_str = ''

    for i in range(0, len(str_)):
        for j in range(0, len(str_)):
            v = get_long(str_[i:], str_o[j:])
            # print(i, j , str_[i:], str_o[j:], max_num, v)
            if len(v) > max_num:
                max_num = len(v)
                max_str = v

    return max_str



def do_2(str_):
    def is_huiwen_middle(s, i):
        pass
    for i in range(len(str_)):
        pass


def test():
    assert do('a') == 'a'
    assert do('abcbd') == 'bcb'
    assert do('') == ''
    print('-----------------')
    assert do('abc') == 'a'
    assert do('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab') == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    assert do('baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    assert do('aabccbaabccbac') == 'abccbaabccba'
    assert do('aabccbaacbdbcaabccbac') == 'abccbaacbdbcaabccba'


if __name__ == '__main__':
    """
    python -m mixleet.201908.LongestPalindromicSubstring test
    """
    from fire import Fire
    Fire()