# coding: utf-8
"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        递归算法
        :param word1:
        :param word2:
        :return:
        """
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) or len(word2)

        return min(
            self.minDistance(word1[1:], word2) + 1,
            self.minDistance(word1, word2[1:]) + 1,
            self.minDistance(word1[1:], word2[1:]) + 1 - (word1[0] == word2[0])
        )

    def minDistance(self, word1: str, word2: str) -> int:
        """
        动态规划算法
        :param word1:
        :param word2:
        :return:
        """
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) or len(word2)

        cache = {}

        def get_cache(i, j):
            if i == -1 and j == -1:
                return 0
            if i == -1 or j == -1:
                return max(i, j) + 1
            return cache.get((i, j))

        for i in range(len(word1)):
            for j in range(len(word2)):
                cache[(i,j)] = min(
                    get_cache(i-1, j) + 1,
                    get_cache(i, j-1) + 1,
                    get_cache(i-1, j-1) + (0 if word1[i] == word2[j] else 1)
                )

        return cache[(len(word1) - 1, len(word2) - 1)]


def test():
    assert Solution().minDistance(word1 = "horse", word2 = "ros") == 3
    assert Solution().minDistance(word1 = "intention", word2 = "execution") == 5


if __name__ == '__main__':
    test()
