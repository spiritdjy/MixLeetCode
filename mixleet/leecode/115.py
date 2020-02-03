# coding: utf-8
"""
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
示例 1:
输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:
如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2:
输入: S = "babgbag", T = "bag"
输出: 5
解释:
如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""
class Solution:
    def _resc(self, s, t):
        """
        10582116 11
        :param s:
        :param t:
        :return:
        """
        if len(t) > len(s):
            return 0
        if not t:
            return 1

        c = t[0]
        sum_ = 0
        index = -1
        while True:
            index = s.find(c, index + 1)
            if index < 0:
                break
            count = self._resc(s[index+1:], t[1:])
            if count == 0:
                break
            sum_ += count

        return sum_

    def _rec(self, s, t):
        """
        10582116 5.48954701423645
        :param s:
        :param t:
        :return:
        """
        if len(t) > len(s):
            return 0
        if not t:
            return 1

        def get_index(s, c):
            ret = []
            index = -1
            while True:
                index = s.find(c, index + 1)
                if index >= 0:
                    ret.append(index)
                else:
                    break
            return ret

        indexs = [get_index(s, c) for c in t]
        sum_ = 0

        def __resc(i, last_index):
            nonlocal sum_
            if i == len(indexs):
                sum_ += 1
                return
            for index in indexs[i]:
                if index > last_index:
                    __resc(i+1, index)

        __resc(0, -1)
        return sum_

    cache = {}

    def _rec2(self, s, t):
        """
        10582116 Cache: 5.995663642883301, No_Cache: 6.0
        :param s:
        :param t:
        :return:
        """
        v = self.cache.get((s, t))
        if v is not None:
            return v

        if len(s) < len(t):
            return 0

        if s == t:
            return 1

        if not t:
            return 1

        v = (self._rec2(s[:-1], t[:-1]) if s[-1] == t[-1] else 0) + self._rec(s[:-1], t)
        self.cache[(s, t)] = v
        return v

    def dp(self, s, t):
        ret = {}
        for i in range(0, len(t)):
            for j in range(0, len(s)):
                print(ret)
                if i == 0 or j == 0:
                    ret[(i, j)] = s[:j+1].count(t[:i+1])
                    continue
                ret[(i, j)] = ret[(i-1, j-1)] + ret[(i, j-1)] if s[j] == t[i] else ret[(i, j-1)]

        return ret[(len(t)-1, len(s)-1)]


    def numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        if not s:
            return 0
        return self.dp(s, t)


def test():
    import time
    assert Solution().numDistinct('rabbbit', 'rabbit') == 3
    assert Solution().numDistinct('babgbag', 'bag') == 5
    assert Solution().numDistinct('abcde', 'ace') == 1
    assert Solution().numDistinct('abcde', 'aec') == 0
    assert Solution().numDistinct('', '') == 1
    assert Solution().numDistinct('', 't') == 0
    now = time.time()
    s, t = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe", "bddabdcae"
    print(Solution().numDistinct(s, t))
    print(time.time() - now)


if __name__ == '__main__':
    test()
