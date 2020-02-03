# coding: utf-8
"""
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
示例 1:
输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:
输入: "abcd"
输出: "dcbabcd"
"""

class Solution:

    def is_huiwen(self, s: str):
        for i in range(0, len(s)//2):
            if s[i] != s[-i - 1]:
                return False
        return True

    def shortestPalindrome(self, s: str) -> str:
        if self.is_huiwen(s):
            return s

        for i in range(len(s), len(s)):
            if s[:i][::-1] != s[:i]
                # print(new_)
                return new_


def test():
    assert Solution().shortestPalindrome('aacecaaa') == 'aaacecaaa'
    assert Solution().shortestPalindrome('abcd') == 'dcbabcd'


if __name__ == '__main__':
    test()