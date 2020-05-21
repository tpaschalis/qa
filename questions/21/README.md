# 21. Merge Two Sorted Lists

Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

### Examples

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

### Testcases
```
[1,2,4]
[1,3,4]
[]
[0]
[]
[]
```

### Benchmarks and Remarks

```
 Runtime: 40 ms, faster than 88.25% of Python3 online submissions for Merge Two Sorted Lists.
 Memory Usage: 13.8 MB, less than 5.01% of Python3 online submissions for Merge Two Sorted Lists.
```

Tried three solutions. An easy and concise recursive one, a simple iterative one, and an iterative solution that modifies the list in place.
