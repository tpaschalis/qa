# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode("#")
        dummy.next = head
        # slow, fast
        s = f = dummy
        
        for i in range(n):
            f = f.next
        
	# Leapfrom the link we need to remove    
        while f.next != None:
            f = f.next
            s = s.next
        curr = s.next
        s.next = curr.next
        
        if f == None:
            return None
        
        return dummy.next
