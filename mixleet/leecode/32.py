# coding: utf-8
"""

"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left_count = 0
        right_count = 0
        last_count = 0
        curr = []
        ret = []
        for i in s:
            exception_right = True
            if i == '(':
                left_count += 1
                exception_right = False
            elif i == ')':
                if left_count > 0:
                    right_count += 1
                    exception_right = False
            else:
                continue

            if exception_right:
                if last_count:
                    ret.append(last_count)
                    last_count = 0
            elif left_count == right_count:
                last_count = last_count + right_count
                right_count, left_count = 0, 0
                curr = []
            elif left_count > right_count:
                if i == ')':
                    pass

        if last_count:
            ret.append(last_count)
        ret.append(right_count)
        return max(ret) * 2

    def clear_left_stacks(self, stack: list):
        ret = []
        curr = 0
        for i in stack:
            if i > 0:
                curr += i
            else:
                if curr:
                    ret.append(curr)
                    curr = 0

        if curr:
            ret.append(curr)

        return ret

    def increase_left_stack(self, stack: list):
        for i in range(len(stack)-1, -1, -1):
            if stack[i] < 0:
                stack[i] = 1
                break

    def longestValidParentheses(self, s: str) -> int:
        left_stacks = []
        ret = []
        for i in s:
            if i == '(':
                left_stacks.append(-1)
            if i == ')':
                if not left_stacks or all(_ > 0 for _ in left_stacks):
                    ret.extend(self.clear_left_stacks(left_stacks))
                    left_stacks = []
                elif any(_ < 0 for _ in left_stacks):
                    self.increase_left_stack(left_stacks)
        if left_stacks:
            ret.extend(self.clear_left_stacks(left_stacks))
        if not ret:
            return 0
        return max(ret) * 2


def test():
    assert Solution().longestValidParentheses('(()(((()') == 2
    assert Solution().longestValidParentheses(')()())') == 4
    assert Solution().longestValidParentheses("()(()") == 2
    assert Solution().longestValidParentheses("()(((()))") == 6
    assert Solution().longestValidParentheses(")))))))()((()))") == 8


if __name__ == '__main__':
    """
    python -m mixleet.leecode.32 test
    """
    from fire import Fire
    Fire()



