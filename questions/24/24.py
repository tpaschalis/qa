# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode("#")
        dummy.next = head
        
        prev, current = dummy, head
        while current != None and current.next != None :
	    # Pointers to next and next-to-next positions
            s1, s2 = current.next, current.next.next
            
	    # Swap the pairs
            prev.next = s1
            s1.next = current
            
	    # Move the next step of the swapping calculation to current.next.next
            current.next = s2
            prev = current
            current = s2
            
        return dummy.next
