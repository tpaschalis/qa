# 19. Remove Nth Node From End of List

Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

### Examples

Example:

Given linked list: `1->2->3->4->5`, and `n = 2`.

After removing the second node from the end, the linked list becomes `1->2->3->5`.


### Benchmarks and Remarks

```
 Runtime: 32 ms, faster than 96.18% of Python3 online submissions for Remove Nth Node From End of List.
 Memory Usage: 13.1 MB, less than 67.48% of Python3 online submissions for Remove Nth Node From End of List.
 Runtime: 36 ms, faster than 83.52% of Python3 online submissions for Remove Nth Node From End of List.
 Memory Usage: 13.1 MB, less than 67.48% of Python3 online submissions for Remove Nth Node From End of List.
```

I need to get used to this technique of creating a dummy, with a null element, where its *dummy.next* is the head of the input linked list.

I tried acting directly on the input like `s = f = head`, but I was hitting weird edge cases, which needed special attention.

I did it with both the two-pass method, as well as the one-pass, two-pointer method. Obviously preferring the second

