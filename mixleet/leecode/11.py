# coding: utf-8

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        len_ = len(height)
        max_value = 0
        for i in range(len_ - 1):
            for j in range(i + 1, len_):
                value = (j - i)* min(height[i], height[j])
                if value > max_value:
                    max_value = value

        return max_value

    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        i = 0
        j = len(height) - 1
        len_ = len(height)
        max_value = 0
        while i < j:
            curr_i = height[i]
            curr_j = height[j]
            value = (j - i) * min(height[i], height[j])
            if value > max_value:
                max_value = value

            if curr_i < curr_j:
                while i < len_:
                    i += 1
                    if height[i] > curr_i:
                        break
            else:
                while j > 0:
                    j -= 1
                    if height[j] > curr_j:
                        break

        return max_value
