# 2. Add Two Numbers

Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


### Examples

Example:
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

### Testcases
```
[2,4,3]
[5,6,4]
[1,8]
[0]
[5]
[5]
```

### Benchmarks and Remarks

```
# Run it some more times, because I thought it was just a lucky break.
# But actually the thing does go really fast!

 Runtime: 60 ms, faster than 99.90% of Python3 online submissions for Add Two Numbers.
 Memory Usage: 13.3 MB, less than 45.44% of Python3 online submissions for Add Two Numbers

 Runtime: 72 ms, faster than 90.97% of Python3 online submissions for Add Two Numbers.
 Memory Usage: 13.2 MB, less than 77.02% of Python3 online submissions for Add Two Numbers

 Runtime: 64 ms, faster than 99.27% of Python3 online submissions for Add Two Numbers.
 Memory Usage: 13.1 MB, less than 93.20% of Python3 online submissions for Add Two Numbers.

 Runtime: 72 ms, faster than 90.97% of Python3 online submissions for Add Two Numbers.
 Memory Usage: 13.2 MB, less than 74.37% of Python3 online submissions for Add Two Numbers.
```


Not much experience with linked lists, so this had me struggle for a little time.

Eventually once I got the handle of how things work, it was a breeze. 

Small things, to not exit the loop if we have a carry, handling lists of non-equal length (I didn't know they would be in the input), and the `h = res = ListNode(0)` chained definition, so we can keep the "head" or the "start" of the resulting `ListNode` to return were nice touches.

