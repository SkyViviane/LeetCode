"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        fnode = ListNode(-1)
        pre = fnode
        while l1 and l2:
            if l1.val >= l2.val:
                pre.next = l2
                l2 = l2.next
            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next
        pre.next = l1 if l1 is not None else l2
        return fnode.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


so = Solution()
l1 = [4, 5, 6]
l2 = [3, 4, 5]
print(so.mergeTwoLists(l1, l2))
