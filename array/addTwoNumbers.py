'''
给出两个非空的链表用来表示两个非负的整数。
其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# class ListNode:
#    def __init__(self, data):
#        self.val = data
#        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        l3 = temp
        a = 0
        while l1 is not None or l2 is not None or a != 0:
            if l1 is not None:
                a += l1.val
                l1 = l1.next
            if l2 is not None:
                a += l2.val
                l2 = l2.next
            temp.next = ListNode(a % 10)
            temp = temp.next
            a = a // 10
        return l3.next

