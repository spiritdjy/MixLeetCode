class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1 2 3 --> 1 3 2
        1 2 3 1 -> 1 3 1 2
        """
        def max_(i, j):
            ret = nums[i]
            for k in range(i+1, j):
                if nums[k] > ret:
                    ret = nums[k]

            return ret

        for i in range(len(nums) - 1, -1, -1):
            if max_(i, len(nums)) == nums[i]:
                continue


            return

        nums.sort()
        return nums