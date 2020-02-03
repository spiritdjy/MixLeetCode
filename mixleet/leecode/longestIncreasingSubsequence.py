# coding: utf-8
"""
longest increasing subsequence
一个序列有 [公式] 个数： [公式] ，求出最长非降子序列的长度。 (讲DP基本都会讲到的一个问题LIS：longest increasing subsequence),非连续
"""


def get_max_inc_sequence(int_list):
    if len(int_list) == 1:
        return 1
    else:
        ret = [1]
        for i in range(1,len(int_list)):
            curr_ = int_list[i]
            max_ = []
            for j in range(len(ret)):
                if int_list[j] <= curr_:
                    max_.append(ret[j] + 1)
                else:
                    max_.append(1)
            ret.append(max(max_))

        return max(ret)


def test():
    assert get_max_inc_sequence([1,2,3,4,5]) == 5
    assert get_max_inc_sequence([1,3,2,4,5]) == 4
    assert get_max_inc_sequence([1]) == 1
    assert get_max_inc_sequence([5,4,3,2,1]) == 1
    assert get_max_inc_sequence([1,1,1,2,2,2]) == 6
    assert get_max_inc_sequence([1,1,1,1,1]) == 5
    assert get_max_inc_sequence([5, 1, 1, 1, 2, 2, 2, 1]) == 6


if __name__ == '__main__':
    """
    python -m mixleet.201908.longestIncreasingSubsequence test
    """
    from fire import Fire
    Fire()
