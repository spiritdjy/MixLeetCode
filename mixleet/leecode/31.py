class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1 2 3 --> 1 3 2
        1 2 3 1 -> 1 3 1 2
        """

        def swap(i):
            select = None
            index = None
            for j in range(i + 1, len(nums)):
                if (select is None and nums[i] < nums[j]) or nums[i] < nums[j] < select:
                    select = nums[j]
                    index = j

            nums[index], nums[i] = nums[i], nums[index]

        for i in range(len(nums) - 1, -1, -1):
            if max(nums[_] for _ in range(i, len(nums))) == nums[i]:
                continue
            swap(i)
            nums[i+1:] = sorted(nums[i+1:])
            return

        nums.sort()
        return nums
