# coding: utf-8
class Solution:
    def longestPalindrome(self, s: str) -> str:
        mapper = {}
        max_len = 0
        max_index = 0

        for i in range(len(s)):
            mapper[(i, i + 1)] = True

        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                mapper[(i, i + 2)] = True
                max_len = 2
                max_index = i

            else:
                mapper[(i, i + 2)] = False


        for length in range(3, len(s)):
            for i in range(len(s) - length + 1):
                if mapper[(i + 1, i + length - 1)] and s[i] == s[i+length-1]:
                    mapper[(i, i + length)] = True
                    max_len = length
                    max_index = i

                else:
                    mapper[(i, i + length)] = False

        return s[max_index: max_index + max_len]