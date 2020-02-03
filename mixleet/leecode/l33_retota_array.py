class Solution:
    def search(self, nums: list, target: int) -> int:
        return self._search(nums, target, 0)

    def _search(self, nums, target, base):
        # print(nums, target, base)
        if len(nums) == 0:
            return -1

        middle = len(nums)//2
        middle_value = nums[middle]
        if target == middle_value:
            return base + middle
        if target == nums[0]:
            return base
        if target == nums[-1]:
            return base + len(nums) - 1

        if nums[0] < middle_value:
            if target < nums[0] or target > middle_value:
                return self._search(nums[middle+1:], target, middle+base+1)
            else:
                return self._search(nums[:middle], target, base)
        else:
            if target < middle_value or target >= nums[0]:
                return self._search(nums[:middle], target, base)
            else:
                return self._search(nums[middle+1:], target, middle + base+1)


def test():
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert Solution().search([], 3) == -1
    assert Solution().search([2], 3) == -1
    assert Solution().search([4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3], 3) == 10
    assert Solution().search([4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3], 4) == 0
    assert Solution().search([4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3], 6) == 2
    assert Solution().search([4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3], 8) == 4
    assert Solution().search([4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3], 10) == 6
    assert Solution().search([4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3], 1) == 8
    assert Solution().search([4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3], 2) == 9


if __name__ == '__main__':
    """
    python -m mixleet.201908.l33_retota_array test
    """
    from fire import Fire
    Fire()
