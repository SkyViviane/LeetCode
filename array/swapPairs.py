'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        fnode = ListNode(-1)
        fnode.next = head
        cur1 = fnode
        cur2 = cur1.next
        cur3 = cur2.next
        while True:
            cur2.next = cur3.next
            cur3.next = cur2
            cur1.next = cur3
            cur1 = cur2
            if cur1.next is None or cur1.next.next is None:
                return fnode.next
            cur2 = cur1.next
            cur3 = cur2.next
