# coding: utf-8
"""
https://soulmachine.gitbooks.io/algorithm-essentials/content/cpp/simulation/zigzag-conversion.html
1        2n-1            => 1, 2n-1, 4n-3   ... +2n-2
2   n+2  2n              => 2, 2n-2, 2n         +2n-4, 2
3 n+1
n        3n-2            => k, 2n+2-2k,         +2n-2k, 2k-2

1 2 3    n
对于每一层垂直元素的坐标 (i,j)= (j+1 )*n +i；对于每两层垂直元素之间的插入元素（斜对角元素），(i,j)= (j+1)*n -i
"""

def cover(str_, n):
    ret = ''
    for i in range(n):
        first, second = 2*n - 2 - i*2, i*2
        index = i
        ret += str_[index] if index < len(str_) else ''
        while True:
            if first:
                index = index + first
                if index >= len(str_):
                    break
                ret += str_[index]

            if second:
                index = index + second
                if index >= len(str_):
                    break
                ret += str_[index]

    return ret


def test():
    assert cover('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'


if __name__ == '__main__':
    test()

