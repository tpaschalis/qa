## Recursive Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = ListNode("#")

        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


## Iteratively
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = s = ListNode("#")

        # while l1 and l2
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                s.next = ListNode(l1.val)
                l1 = l1.next
            else:
                s.next = ListNode(l2.val)
                l2 = l2.next
            s = s.next

        # One of the two lists has all its elements processed
        # s.next = l1 or l2

        if l1 != None:
            s.next = l1
        elif l2 != None:
            s.next = l2

        return res.next



## Iteratively and in-place
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = s = ListNode("#")

        s.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                skip = s.next
                s.next = l2
                tmp = l2.next
                l2.next = skip
                l2 = tmp
            s = s.next
        s.next = l1 or l2
        return res.next

