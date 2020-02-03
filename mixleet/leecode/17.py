# coding: utf-8
"""
判断2~9个数字能组成的字母列表
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits or all(c == '1' for c in digits):
            return []

        def rec_(curr, left, ret):
            if not left:
                ret.append(curr)
            digit, left = left[0], left[1:]
            chars = mapper.get(digit)
            if chars:
                for c in chars:
                    rec_(curr + c, left, ret)
            else:
                rec_(curr, left, ret)

        ret = []
        rec_('', digits, ret)
        return ret
