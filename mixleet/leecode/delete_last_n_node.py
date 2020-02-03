# coding: utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return '%s->%s' % (self.val, str(self.next))
        return '%s' % self.val


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        n_list = [curr]
        n_node = 1
        while curr.next:
            n_list.append(curr.next)
            curr = curr.next
            n_node += 1
            # if len(n_list) > n+1:
            #     del n_list[0]

        if n_node == n:
            return head.next

        deleted = n_list[-n-1]
        deleted.next = deleted.next.next
        return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


def do_test():

    def create_list(nums=[1, 2, 3, 4, 5]):
        node_last = None
        for i in reversed(nums):
            node_new = ListNode(i)
            node_new.next = node_last
            node_last = node_new

        return node_last

    assert str(Solution().removeNthFromEnd(create_list(), 2)) == '1->2->3->5'
    assert str(Solution().removeNthFromEnd(create_list(), 5)) == '2->3->4->5'
    assert str(Solution().removeNthFromEnd(create_list([1]), 1)) == 'None'


if __name__ == '__main__':
    do_test()