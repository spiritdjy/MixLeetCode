# coding: utf-8
"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
进阶：
你能在线性时间复杂度内解决此题吗？
"""
class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        ret = []
        for i in range(0, len(nums)+1-k):
            ret.append(max(nums[i:i+k]))
        return ret

    def maxSlidingWindow(self, nums: list, k: int) -> list:
        """
        原理只保留窗口里面大到小的值，如[1, 3, 5, 1, 3, 2]则只需要记录[5, 3, 2]对应的index，然后窗口依次移动，超过5则将5移掉，然后将里面比新值小的去掉
        最大值始终在index第一个
        :param nums:
        :param k:
        :return:
        """
        win, ret = [], []
        for i, v in enumerate(nums):
            if i >= k and win[0] < i - k:
                win.pop(0)
            while win and nums[win[-1]] <= v:
                win.pop()
            win.append(i)
            if i >= k - 1:
                ret.append(nums[win[0]])
        return ret

    def maxSlidingWindow(self, nums: list, k: int) -> list:
        """
        dp
        :param nums:
        :param k:
        :return:
        """
        left, right = [], []

        max_ = None
        for i, num in enumerate(nums):
            if i % k == 0:
                max_ = num
            else:
                max_ = max(max_, num)
            left.append(max_)

        max_ = None
        n = len(nums) - 1
        for i, num in enumerate(reversed(nums)):
            i = n - i
            if max_ is None or i % k == k-1:
                max_ = num
            else:
                max_ = max(num, max_)
            right.append(max_)
        right.reverse()

        ret = []
        for i in range(len(nums) - k + 1):
            if i % k == 0:
                ret.append(left[i + k - 1])
            else:
                ret.append(max(left[i+k-1], right[i]))

        print(left, right, ret)
        return ret


def test():
    assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]


if __name__ == '__main__':
    test()
