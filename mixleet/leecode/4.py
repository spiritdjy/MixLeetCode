# coding: utf-8
"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""
class Solution:
    def findMedianSortedArrays_sorted(self, nums1: list, nums2: list) -> float:
        new_ = nums1 + nums2
        new_.sort()
        middle = len(new_) // 2
        if len(new_) % 2 == 1:
            return new_[middle]
        else:
            return (new_[middle] + new_[middle-1]) / 2

    def _find(self, first, second, index):
        if len(first) and len(second):
            mid_a = len(first) // 2 + 1
            mid_b = len(second) // 2 + 1
            # print(f'find, {first}, {second}, {index}, {mid_a}, {mid_b}')
            if first[mid_a - 1] == second[mid_b - 1]:
                if index in [mid_a + mid_b, mid_a + mid_b - 1]:
                    return first[mid_a - 1]
                if index < mid_a + mid_b - 1:
                    return self._find(first[:mid_a-1], second[:mid_b-1], index,)
                if index > mid_a + mid_b:
                    return self._find(first[mid_a:], second[mid_b:], index - mid_a - mid_b)

            if first[mid_a - 1] > second[mid_b - 1]:
                first, second, mid_a, mid_b = second, first, mid_b, mid_a

            if index < mid_a + mid_b:
                return self._find(first, second[:mid_b - 1], index)
            else:
                return self._find(first[mid_a:], second, index - mid_a)

        not_empty = first or second
        return not_empty[index-1]

    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        all_n = len(nums1) + len(nums2)
        middle = all_n // 2 + 1
        avg_middle = (all_n % 2 == 0)
        if avg_middle:
            return self._find(nums1, nums2, middle)/2 + self._find(nums1, nums2, middle-1) / 2
        return self._find(nums1, nums2, middle)


def test():
    assert Solution().findMedianSortedArrays([], [1]) == 1
    assert Solution().findMedianSortedArrays([1, 2], []) == 1.5
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert Solution().findMedianSortedArrays([0, 0], [0, 0]) == 0


if __name__ == '__main__':
    test()
