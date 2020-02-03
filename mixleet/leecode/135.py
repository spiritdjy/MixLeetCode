# coding: utf-8
"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？
示例 1:
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:
输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
"""

class Solution:
    def candy(self, ratings: list) -> int:
        ret = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] == ratings[i-1]:
                ret[i] = 1
            elif ratings[i] < ratings[i-1]:
                if ret[i-1] > 1:
                    ret[i] = 1
                else:
                    curr = 1
                    while i >= 1:
                        if ratings[i-1] > ratings[i]:
                            if ret[i-1] < curr + 1:
                                ret[i-1] = curr + 1
                            else:
                                break
                            i -= 1
                            curr += 1
                        else:
                            break
            elif ratings[i] > ratings[i-1]:
                ret[i] = ret[i-1] + 1

        return sum(ret)

    def candy(self, ratings: list) -> int:
        sum_ = 1
        inc_ = 0
        curr = 1
        max_ = 1
        for i in range(1, len(ratings)):
            print(f'Rateing: {ratings[:i+1]}, sum:{sum_}, inc:{inc_}, curr:{curr}, max:{max_}')
            if ratings[i] == ratings[i-1]:
                sum_ += 1
                inc_ = 0
                curr = 1
                max_ = 1
            elif ratings[i] < ratings[i-1]:
                inc_ += 1
                if curr > 1:
                    curr = 1
                    sum_ += curr
                else:
                    if max_ >= 1 + inc_:
                        sum_ += inc_ - 1
                    else:
                        max_ = 1 + inc_
                        sum_ += inc_
                    curr = 1
                    sum_ += curr
            elif ratings[i] > ratings[i-1]:
                curr += 1
                inc_ = 0
                sum_ += curr
                max_ = curr
            print(f'--Rateing: {ratings[:i+1]}, sum:{sum_}, inc:{inc_}, curr:{curr}, max:{max_}')

        return sum_



def test():
    import time
    assert Solution().candy([1,0,2]) == 5
    assert Solution().candy([1,2,2]) == 4
    assert Solution().candy([1,2,3]) == 6
    assert Solution().candy([1, 2, 3, 3, 2, 1]) == 12
    assert Solution().candy([4, 3, 3, 2, 1]) == 9
    assert Solution().candy([4, 4, 4, 4, 1]) == 6
    assert Solution().candy([4, 4, 4, 4, 4]) == 5
    assert Solution().candy([1,3,2,2,1]) == 7
    assert Solution().candy([1,2,3,1,0]) == 9
    assert Solution().candy([1, 2, 3, 4, 5, 3, 2, 1]) == 21
    assert Solution().candy([1, 2, 3, 2, 1, 0, -1]) == 18
    curr = time.time()
    # Solution().candy(list(i for i in range(12000, 0, -1)))
    print(time.time() - curr)


if __name__ == '__main__':
    test()