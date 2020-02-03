# coding: utf-8
"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  
示例 1:
输入: "1 + 1"
输出: 2
示例 2:
输入: " 2-1 + 2 "
输出: 3
示例 3:
输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
"""
from operator import add, sub


class Solution:

    def sum(self, list_):
        sum_ = 0
        fun_list = []
        for i in list_:
            if isinstance(i, int):
                sum_ = sum_ + i if fun_list.count('-') % 2 == 0 else sum_ - i
                fun_list = []
            else:
                fun_list.append(i)
        return sum_

    def get_token(self, str_):
        nums = []
        for i, char in enumerate(str_):
            if nums and char in '+-() ':
                return int(''.join(nums)), str_[i:]

            if char in '+-()':
                return char, str_[i+1:]

            if str.isdigit(char):
                nums.append(char)

        if nums:
            return int(''.join(nums)), ''
        return None, ''

    def calculate(self, s: str) -> int:
        parts = []
        while s:
            token, s = self.get_token(s)
            print(token, parts, s, sep=' |  ')
            if token is None:
                break

            if token == ')':
                try:
                    index = -1
                    while True:
                        index = parts.index('(', index + 1)
                except:
                    pass
                sum_ = self.sum(parts[index+1:])
                parts = parts[:index] + [sum_]

            elif isinstance(token, int):
                parts.append(token)

            elif token in ['+', '-', '(']:
                parts.append(token)

            else:
                print('wrong')

        return self.sum(parts)

    def calculate(self, s: str) -> int:
        left = 0
        func_ = add
        stack = []
        num = 0
        last_operator = False
        for i, c in enumerate(s):
            if str.isdigit(c):
                num = num * 10 + int(c)
            elif c in '+-':
                if last_operator:
                    func_ = add if ([add if c == '+' else sub] + [func_]).count(sub) % 2 == 0 else sub
                    continue
                left = func_(left, num)
                num = 0
                func_ = add if c == '+' else sub
            elif c == '(':
                stack.append(left)
                stack.append(func_)
                left = 0
                func_ = add
            elif c == ')':
                left_ = func_(left, num)
                func_ = stack.pop()
                left = stack.pop()
                left = func_(left, left_)
                func_ = add
                num = 0
            else:
                continue
            last_operator = True if c in '+-' else False
            # print(f'{s[:i+1]}, left: {left}, num: {num}, fun: {func_}, stack: {stack}')
        return func_(left, num)


class Solution:

    def __init__(self):
        self.s = None

    def get_token(self, str_):
        print(self.s)
        nums = []
        for i, char in enumerate(str_):
            if nums and char in '+-() ':
                self.s = str_[i:]
                return int(''.join(nums))

            if char in '+-()':
                self.s = str_[i+1:]
                return char

            if str.isdigit(char):
                nums.append(char)

        if nums:
            self.s = ''
            return int(''.join(nums))
        self.s = ''
        return None

    def calculate(self, s: str) -> int:
        sum_ = self.value(s)
        while self.s:
            token = self.get_token(self.s)
            if token == '+':
                value = self.value(self.s)
                sum_ += value
            elif token == '-':
                value = self.value(self.s)
                sum_ -= value
            elif token == ')':
                return sum_
        return sum_

    def value(self, s):
        token = self.get_token(s)
        if token == '-':
            return - self.value(self.s)
        if isinstance(token, int):
            return token
        if token == '(':
            return self.calculate(self.s)


def test():
    assert Solution().calculate('-1') == -1
    assert Solution().calculate('0') == 0
    assert Solution().calculate('1 - -1  ') == 2
    assert Solution().calculate(' 2-1 + 2 ') == 3
    assert Solution().calculate('(1+(4+5+2)-3)+(6+8)') == 23
    assert Solution().calculate('((1+1))') == 2
    assert Solution().calculate(' - (1 - 6) + 4 + 1 ') == 10
    assert Solution().calculate(' - 1 - 1 - 1 - 1 - 1 -1') == -6


if __name__ == '__main__':
    test()

