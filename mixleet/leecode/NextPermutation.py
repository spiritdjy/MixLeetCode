# coding: utf-8
"""
https://soulmachine.gitbooks.io/algorithm-essentials/content/cpp/linear-list/array/next-permutation.html
"""


def next_permutation(int_list: list):
    # special case
    if len(int_list) == 1:
        return int_list
    if len(int_list) == 2:
        return list(reversed(int_list))

    # more than 2, 从后面往前面找，找到小大关系的最近的进行交换
    for i in range(len(int_list)-2, -1, -1):
        curr = int_list[i]
        replace_ = [num for num in int_list[i+1:] if num > curr]
        if replace_:
            next_ = min(replace_)
            index = int_list.index(next_, i+1)
            print(int_list[:i] + int_list[index:index+1] + int_list[i+1:index]+int_list[i:i+1]+int_list[index+1:])
            return int_list[:i] + int_list[index:index+1] + int_list[i+1:index]+int_list[i:i+1]+int_list[index+1:]

    return list(reversed(int_list))


def next_permutation(int_list: list):
    # special case
    if len(int_list) == 1:
        return int_list
    if len(int_list) == 2:
        return list(reversed(int_list))

    # more than 2, 从后面往前面找，找到小大关系的最近的进行交换
    index_curr = len(int_list) - 2
    while index_curr >= 0:
        last_ = int_list[index_curr + 1]
        if int_list[index_curr] >= last_:
            index_curr -= 1
        else:
            break

    if index_curr >= 0:
        curr_num = int_list[index_curr]
        next_index = len(int_list) - 1
        while True:
            if int_list[next_index] <= curr_num:
                next_index -= 1
            else:
                # 允许数字重复则需要找到最左边一个小的
                while int_list[next_index - 1] == int_list[next_index]:
                    next_index -= 1
                break

        print(index_curr, next_index)
        return int_list[:index_curr] + int_list[next_index:next_index+1] + int_list[index_curr+1:next_index]+int_list[index_curr:index_curr+1]+int_list[next_index+1:]

    return list(reversed(int_list))


def test():
    assert next_permutation([1,2,3]) == [1,3,2]
    assert next_permutation([1, 2, 3]) == [1, 3, 2]
    assert next_permutation([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert next_permutation([1,1,5]) == [1,5,1]
    assert next_permutation([1, 5, 1]) == [5, 1, 1]
    assert next_permutation([1, 1, 1]) == [1, 1, 1]
    assert next_permutation([1, 1]) == [1, 1]
    assert next_permutation([1, 2]) == [2, 1]
    assert next_permutation([1]) == [1]
    assert next_permutation([2, 5, 4, 3, 3, 2, 2]) == [3, 5, 4, 2, 3, 2, 2]


if __name__ == '__main__':
    """
    python -m mixleet.201908.NextPermutation test
    """
    from fire import Fire
    Fire()