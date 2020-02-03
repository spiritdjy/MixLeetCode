# coding: utf-8
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
"""

class PrefixTree:

    def __init__(self):
        self.dict = [None, {}]

    def add_word(self, word, value):
        node = self.dict
        for c in word:
            if c not in node[1]:
                node[1][c] = [None, {}]
            node = node[1][c]
        node[0] = value

    def find(self, string):
        ret = []
        dict_ = self.dict[1]
        for c in string:
            # print(c, dict_)
            n = dict_.get(c)
            if n:
                v, dict_ = n
                if v:
                    ret.append(v)
            else:
                break
        # print(ret)
        return ret


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        if not s or not wordDict:
            return []

        tree = PrefixTree()
        for i in wordDict:
            tree.add_word(i, i)
        # print(tree.dict)

        def get_prefix(str_, words):
            # print(str_, words)
            for v in tree.find(str_):
                if len(v) == len(str_):
                    yield words + [v]
                else:
                    yield from get_prefix(str_[len(v):], words + [v])

        ret = list(' '.join(i) for i in get_prefix(s, []))
        ret.sort()
        # print('-------------', ret)
        return ret


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        if not s or not wordDict:
            return []

        dict_ = set(wordDict)
        lens = list(set(len(i) for i in wordDict))

        def get_prefix(str_, words):
            # print(str_, words)
            n = len(str_)
            for i in lens:
                v = str_[:i]
                if v in dict_:
                    if i == n:
                        yield words + [v]
                    else:
                        yield from get_prefix(str_[i:], words + [v])

        ret = list(' '.join(i) for i in get_prefix(s, []))
        ret.sort()
        # print('-------------', ret)
        return ret


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        if not s or not wordDict:
            return []

        dict_ = set(wordDict)
        lens = list(set(len(i) for i in wordDict))
        middle_result = [([], s)]
        result = []

        while middle_result:
            words, str_ = middle_result.pop()
            n = len(str_)
            for i in lens:
                if i > n:
                    continue
                v = str_[:i]
                if v in dict_:
                    if i == n:
                        result.append(words + [v])
                    else:
                        middle_result.append((words + [v], str_[i:]))

        ret = list(' '.join(i) for i in result)
        ret.sort()
        # print('-------------', ret)
        return ret


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        if not s or not wordDict:
            return []

        mem = {}
        dict_ = set(wordDict)
        lens = list(set(len(i) for i in wordDict))
        lens.sort()
        middle_result = [([], s)]
        result = []

        while middle_result:
            words, str_ = middle_result.pop()
            n = len(str_)
            for i in lens:
                if i > n:
                    continue
                v = str_[:i]
                if v in dict_:
                    if i == n:
                        result.append(words + [v])
                    else:
                        middle_result.append((words + [v], str_[i:]))

        ret = list(' '.join(i) for i in result)
        ret.sort()
        # print('-------------', ret)
        return ret


def test():
    assert Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == list(sorted([
"cats and dog",
"cat sand dog"
]))
    assert Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]) == list(sorted([
"pine apple pen apple",
"pineapple pen apple",
"pine applepen apple"
]))
    assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []
    import time
    curr = time.time()
    Solution().wordBreak('a'*1000, ['aa', 'aaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaa'])
    print(time.time() - curr)


if __name__ == '__main__':
    test()
