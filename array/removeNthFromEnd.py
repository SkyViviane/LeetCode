'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        fnode = ListNode(-1)
        fnode.next = head
        cur1 = fnode
        cur2 = fnode
        for i in range(1, n + 2):
            cur2 = cur2.next
        while cur2 is not None:
            cur1 = cur1.next
            cur2 = cur2.next
        cur1.next = cur1.next.next
        return fnode.next
