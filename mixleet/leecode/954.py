class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        if not A:
            return [-1, -1]
        count_one = A.count(1)
        if count_one % 3 != 0:
            return [-1, -1]
        if count_one == 0:
            return [0, len(A) - 1]

        one_n = count_one // 3
        tail_1_index = ''.join(str(_) for _ in A).rfind('1')
        tail_0_count = len(A) - 1 - tail_1_index
        len_ = len(A)

        def find_end(i):
            c = 0
            while i < len_ and c < one_n:
                if A[i] == 1:
                    c += 1
                i += 1

            c = 0
            while i < len_ and c < tail_0_count:
                if A[i] == 0:
                    c += 1
                i += 1

            return i - 1

        i = find_end(0)
        j = find_end(i + 1)

        if int('0b0' + ''.join(str(_) for _ in A[:i + 1]), 2) == int('0b0' + ''.join(str(_) for _ in A[i + 1:j + 1]),
                                                                     2) and \
                int('0b0' + ''.join(str(_) for _ in A[:i + 1]), 2) == int('0b0' + ''.join(str(_) for _ in A[j + 1:]),
                                                                          2):
            return [i, j + 1]
        return [-1, -1]