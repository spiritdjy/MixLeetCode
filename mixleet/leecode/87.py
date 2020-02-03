# coding: utf-8
"""
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

下图是字符串 s1 = "great" 的一种可能的表示形式。

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

示例 1:

输入: s1 = "great", s2 = "rgeat"
输出: true
示例 2:

输入: s1 = "abcde", s2 = "caebd"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/scramble-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def judge(self, s1, s2):
        for i in range(1, len(s1)):
            p_ = s1[:i]
            p__ = s1[i:]
            if p__ + p_ == s2:
                return True

        return False

    def two_continue_char(self, s):
        last_char = None
        for char in s:
            if char == last_char:
                return True
            last_char = char
        return False

    def isScramble_com(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        len_ = len(s1)
        for i in range(len_-1):
            for j in range(i+2, len_+1):
                s_ = s1[i:j]
                s__ = s2[i:j]
                if self.judge(s_, s__):
                    return True

        return False

    def isScramble_diff(self, s1, s2):
        len_ = len(s1)
        diff_index = [i for i in range(len_) if s1[i] != s2[i]]
        for i in range(min(diff_index), -1, -1):
            for j in range(max(diff_index), len_+1, 1):
                if self.judge(s1[i:j], s2[i:j]):
                    return True

        return False

    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False

        if sorted(s1) != sorted(s2):
            return False

        if s1 == s2:
            return True
        else:
            return self.isScramble_diff(s1, s2)


def test():
    assert Solution().isScramble('gabcabc', 'gabcabc') == True
    assert Solution().isScramble('great', 'great') == False
    assert Solution().isScramble('greet', 'greet') == True
    assert Solution().isScramble('great', 'rgeat') == True
    assert Solution().isScramble('abcde', 'caebd') == False
    assert Solution().isScramble('geelelek', 'geelekel') == True
    assert Solution().isScramble('eleeleke', 'elekeele') == True


if __name__ == '__main__':
    test()
