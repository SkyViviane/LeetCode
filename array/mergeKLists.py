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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    self.nodes = []
    head = point = ListNode(-1)
    for l in lists:
    	while l:
    		self.nodes.append(l.val)
    		l = l.next
    for x in sorted(self.nodes):
    	point.next = ListNode(x)
    	point = point.next
    return head.next
