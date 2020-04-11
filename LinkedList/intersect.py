"""
判断两个相交链表
"""
#第一种方法
class Node:
    def __init__(self, val = None, next_ = None):
        self.val = val
        self.next = next_
        
def intersect(head1, head2):
    l1 = l11 = head1
    l2 = l22 = head2
    len1 = 1
    len2 = 1
    while l11.next != None:
        len1 += 1
        l11 = l11.next
    while l22.next != None:
        len2 += 1
        l22 = l22.next
    if len1 > len2:
        for i in range((len1 - len2)):
            l1 = l1.next
    elif len1 < len2:
        for i in range((len2 - len1)):
            l2 = l2.next
    while l1 and l2:
        if l1.val == l2.val and id(l1.val) == id(l2.val):
            return l1.val
        else:
            l1 = l1.next
            l2 = l2.next
                
head1 = Node(3)
head1.next = Node(4)
head1.next.next= Node(7)
head1.next.next.next = Node(2)
head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(2)
print(intersect(head1, head2))

#利用字典的第二种方法
class Node:
    def __init__(self, val = None, next_ = None):
        self.val = val
        self.next = next_
        
def intersect(head1, head2):
    dicts = {}
    l1 = head1
    l2 = head2
    while l1 != None:
        dicts[id(l1.val)] = l1.val
        l1 = l1.next
    while l2 != None:
        key = id(l2.val)
        if key in dicts.keys():
            return l2.val
        else:
            l2 = l2.next      
                
head1 = Node(3)
head1.next = Node(4)
head1.next.next= Node(7)
head1.next.next.next = Node(2)
head2 = Node(8)
head2.next = Node(7)
head2.next.next = Node(2)
print(intersect(head1, head2))
    
