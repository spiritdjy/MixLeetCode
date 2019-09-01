class Solution:

    chars = 'abcdefghijklmnopqrstuvwxyz'

    def isMatch(self, s: str, p: str) -> bool:
        while '**' in p:
            p = p.replace('**', '*')
        return self._isMatch(s, p)

    def get_max_sub_str(self, p: str):
        ret = ['']
        for i, c in enumerate(p):
            if c in '*?':
                ret.append('')
            else:
                ret[-1] += c
        ret.sort(key=lambda x:len(x))
        return ret[-1]

    def _isMatch(self, s: str, p: str) -> bool:

        if not p and not s:
            return True
        if s and not p:
            return False
        if not s and p:
            if p != '*':
                return False
            return True

        count_wen = p.count('?')
        count_star = p.count('*')
        count_normal = len(p) - count_wen - count_star

        if count_normal == 0:
            if count_star and len(s) >= count_wen:
                return True
            elif len(s) == count_wen:
                    return True
            return False

        if len(s) < count_wen + count_normal:
            return False

        if p[-1] not in '*?':
            if s[-1] != p[-1]:
                return False
        if p[0] not in '*?':
            if p[0] != s[0]:
                return False

        if p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        if p[-1] == '?':
            return self.isMatch(s[:-1], p[:-1])

        sub_ = self.get_max_sub_str(p)
        if sub_:
            start_index = p.find(sub_)
            end_index = start_index + len(sub_)
            # print(sub_, start_index, end_index)

        else:
            index = 0
            start_index = None
            end_index = len(p)
            while index < len(p):
                if p[index] in '*?':
                    if start_index is not None:
                        end_index = index
                        break
                else:
                    if start_index is None:
                        start_index = index
                index += 1
            sub_ = p[start_index: end_index]

        index = -1
        while True:
            index = s.find(sub_, index + 1)
            if index >= 0:
                # print(index, start_index, end_index, s[:index], p[:start_index], sub_, s[index+len(sub_):], p[end_index:])
                r = self.isMatch(s[:index], p[:start_index]) and self.isMatch(s[index+len(sub_):], p[end_index:])
                if r:
                    return True
            else:
                break
        # print(s, p, False)
        return False


def do_test():
#     assert Solution().isMatch("aa", "aa") == True
#     assert Solution().isMatch("aa", "a") == False
#     assert Solution().isMatch("aa", "*a") == True
#     assert Solution().isMatch("aa", "?a") == True
#     assert Solution().isMatch("aa", "?*a") == True
#     assert Solution().isMatch("aa", "*?a") == True
#     assert Solution().isMatch("aa", "*?aa") == False
#     assert Solution().isMatch("aa", "?aa") == False
#     assert Solution().isMatch("aa", "*") == True
#     assert Solution().isMatch("cb", "*a") == False
#     assert Solution().isMatch("adceb", "*a*b") == True
#     assert Solution().isMatch("acdcb", "a*c?b") == False
#     assert Solution().isMatch("", "*") == True
#     assert Solution().isMatch("a", "*") == True
#     assert Solution().isMatch("abcccd", "*") == True
#     assert Solution().isMatch("", "?") == False
#     assert Solution().isMatch("aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba",
# "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*") == True
#     assert Solution().isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
# "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a") == False
    assert Solution().isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
"**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb") == True


if __name__ == '__main__':
    do_test()