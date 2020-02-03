# coding: utf-8
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + '->' + str(self.next)


class ListLink:

    def __init__(self, list_):
        if list_:
            nodes = [ListNode(i) for i in list_]
            self.root = nodes[0]
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]
        else:
            self.root = None

    def __str__(self):
        if not self.root:
            print('LIST:None')
        else:
            strs = []
            node = self.root
            while node:
                strs.append(str(node.val))
                node = node.next
            print(f'LIST:{"->".join(strs)}')


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        ret = []
        while True:
            lists = [i for i in lists if i]
            if not lists:
                break
            values = [i.val for i in lists]
            min_ = min(values)
            index = values.index(min_)
            ret.append(lists[index])
            lists[index] = lists[index].next

        for i in range(len(ret)-1):
            ret[i].next = ret[i+1]

        return ret[0] if ret else None


def test():
    assert Solution().mergeKLists([ListLink([1,3]).root, ListLink([2, 4]).root, ListLink([3, 5]).root]).__str__() == '1->2->3->4->5->None'