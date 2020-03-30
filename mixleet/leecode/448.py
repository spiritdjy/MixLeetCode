class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        start = 1
        end = len(nums)
        ret = []
        for i in nums:
            if i > start:
                for _ in range(start, i):
                    ret.append(_)
                start = i + 1
            elif i == start:
                start += 1
        for _ in range(start, end + 1):
            ret.append(_)

        return ret
