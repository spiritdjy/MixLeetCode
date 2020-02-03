class Solution:
    def generateParenthesis(self, n: int) -> str:
        if n <= 0:
            return []

        ret = []

        def generate(str, left, right):
            if left == 0 and right == 0:
                ret.append(str)
                return

            if left:
                generate(str + '(', left - 1, right + 1)

            if right:
                generate(str + ')', left, right - 1)

        generate('', n, 0)

        return ret

    def generateParenthesis(self, n: int) -> str:
        if n <= 0:
            return []

        mapper = {
            0: [],
            1: ['()'],
            2: ['()()', '(())']
        }

        for i in range(3, n+1):
            ret = []
            for j in range(i):
                for left in (mapper[j] or ['']):
                    for right in (mapper[i - 1 - j] or ['']):
                        ret.extend('(' + left + ')' + right)

            mapper[i] = ret

        return mapper[n]

Solution().generateParenthesis(3)
