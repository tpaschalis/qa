# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        h = res = ListNode(0)
        
        while l1 or l2 or carry != 0:

            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = s//10 
            res.next = ListNode(s%10)
            res = res.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None            
        
        return h.next
