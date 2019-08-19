# coding: utf-8
from fire import Fire
import math


def find_sum_2(nums, sum_):
    b = 0
    e = len(nums) - 1
    curr_delta = max(abs(max(nums)*2 - sum_), abs(min(nums)*2-sum_))

    while True:
        curr_sum = nums[b] + nums[e]
        curr = nums[b], nums[e]

        if b == e:
            return curr_pair, curr_delta

        if curr_sum == sum_:
            return curr, 0

        elif curr_sum < sum_:
            new_delta = sum_ -  curr_sum
            if curr_delta <= new_delta:
                curr_delta = new_delta
                curr_pair = curr
                b += 1
            else:
                e -= 1

        elif curr_sum > sum_:
            new_delta = curr_sum - sum_
            if new_delta < curr_delta:
                curr_delta = new_delta
                curr_pair = curr
                e -= 1
            else:
                b += 1


def chose_k(nums, sum_):
    nums.sort()
    min_sum = max(abs(max(nums)*3 - sum_), abs(min(nums)*3-sum_))
    pairs = None
    for i in range(len(nums)-2):
        num_a = nums[i]
        num_bc, delta = find_sum_2(nums[i+1:], sum_ - num_a)
        if delta < min_sum:
            min_sum = delta
            pairs = (num_a, num_bc[0], num_bc[1])

    print(min_sum, pairs)
    return pairs


def test():
    nums = [-1, 2, 1, 4]
    k = 2
    ret = [-1, 2, 1]
    assert set(chose_k(nums, k)) == set(ret)


if __name__ == '__main__':
    """
    python -m mixleet.201908.sum3closeset test
    """
    from fire import Fire
    Fire()
