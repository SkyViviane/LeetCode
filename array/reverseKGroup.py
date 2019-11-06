"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = end = dummy
        while end.next is not None:
            for i in range(k):
                if end is not None:
                    end = end.next
            if end is None:
                break
            start = pre.next
            next = end.next
            end.next = None
            pre.next = self.reverse(start)
            start.next = next
            pre = end = start
        return dummy.next

    def reverse(self, head):
        cur = head
        pre = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
