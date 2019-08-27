# coding: utf-8
"""
https://soulmachine.gitbooks.io/algorithm-essentials/content/cpp/bfs/word-ladder-ii.html
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example, Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
[
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

def get_one_change(word, dict_, visted):
    ret = []
    for word_ in dict_:
        if word_ in visted:
            continue
        common = sum(i==j for i, j in zip(word_, word))
        if common == len(word) - 1:
            ret.append(word_)
    return ret


def get_ladder(start, end, dict_):
    visited = set()

    def _ladder(words, paths):
        for i in words:
            visited.add(i)

        ret = []
        for word, path in zip(words, paths):
            if word == end:
                ret.append(path)
                continue
        if ret:
            return ret

        next_words = []
        next_paths = []
        for word, path in zip(words, paths):
            starts = get_one_change(word, dict_, visited)
            for next_ in starts:
                next_words.append(next_)
                next_paths.append(path + [next_])

        if next_words:
            return _ladder(next_words, next_paths)

        return []

    return _ladder([start], [[start]])


def test():
    start = "hit"
    end = "cog"
    dict_ = ["hit", "hot", "dot", "dog", "lot", "log", "cog"]
    return_ = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]
    print(get_ladder(start, end, dict_))
    assert get_ladder(start, end, dict_) == return_


if __name__ == '__main__':
    """
    python -m mixleet.201908.WordLadderII test
    """
    from fire import Fire
    Fire()

