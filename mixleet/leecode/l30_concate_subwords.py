# coding; utf-8
"""
https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
"""
from collections import Counter


def process(s, words):
    if not words:
        return []

    word_len = len(words[0])
    if len(s) < word_len:
        return []

    word_to_index = {word: i for i, word in enumerate(words, 1)}
    word_to_counter = Counter(word_to_index[i] for i in words)
    string_part_index = []

    for i in range(len(s) - word_len+1):
        index = word_to_index.get(s[i: i+word_len], 0)
        string_part_index.append(index)

    ret = []
    for start in range(word_len):
        string_sp = string_part_index[start::word_len]
        for i in range(len(string_sp) - len(words)+1):
            counter = Counter(string_sp[i:i + len(words)])
            print(start,
                  string_part_index,
                  string_sp,
                  string_part_index[start::word_len],
                  i,
                  string_sp[i:i + len(words)],
                  counter, word_to_counter)
            if counter != word_to_counter:
                continue
            else:
                ret.append(start+i*word_len)

    print(ret)
    return ret


def test():
    """
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
    :return:
    """
    assert process("barfoothefoobarman", ["foo","bar"]) == [0, 9]
    assert process("barfoothefoobar", ["foo", "bar"]) == [0, 9]
    assert process("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []
    assert process("abc", ["word", "good", "best", "word"]) == []
    assert process("words", ["word", "good", "best", "word"]) == []
    assert process("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]) == [8]


if __name__ == '__main__':
    """
    python -m mixleet.201908.l30_concate_subwords test
    """
    from fire import Fire
    Fire()
