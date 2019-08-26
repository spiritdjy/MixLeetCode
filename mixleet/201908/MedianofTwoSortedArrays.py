# coding: utf-8
"""
Median of Two Sorted Arrays, log(m+n)
"""

def find_kth(list_a, list_b, k):
    print('->', list_a, list_b, k)
    if not list_a:
        return list_b[k-1]
    if not list_b:
        return list_a[k-1]

    len_a = len(list_a)
    len_b = len(list_b)

    if k == 1:
        return min(list_a[0], list_b[0])
    if k == len_a + len_b:
        return max(list_a[-1], list_b[-1])

    if len_a < len_b:
        index_a = min(len_a, k//2) - 1
        index_b = k - index_a - 2
    else:
        index_b = min(len_b, k // 2) - 1
        index_a = k - index_b - 2

    if list_a[index_a] == list_b[index_b]:
        return list_b[index_b]
    elif list_a[index_a] < list_b[index_b]:
        return find_kth(list_a[index_a+1:], list_b[:index_b+1], k-index_a-1)
    else:
        return find_kth(list_a[:index_a + 1], list_b[index_b+1:], k-index_b-1)


def test():
    import random
    for i in range(50):
        list_a = [random.randint(1, 400) for _ in range(random.randint(10,30))]
        list_b = [random.randint(1, 400) for _ in range(random.randint(10,30))]
        k = (len(list_a) + len(list_b)) // 2
        list_a.sort()
        list_b.sort()
        all_ = list_a + list_b
        all_.sort()
        print(list_a, list_b, all_[k-1], find_kth(list_a, list_b, k))
        assert all_[k-1] == find_kth(list_a, list_b, k)


if __name__ == '__main__':
    test()
