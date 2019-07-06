# 7. Reverse Integer

Easy

Given a 32-bit signed integer, reverse digits of an integer.

### Examples

Example 1:
```
Input: 123
Output: 321
```

Example 2:
```
Input: -123
Output: -321
```

Example 3:
```
Input: 120
Output: 21
```

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

### Testcases
```
# input
-2147483412
123
-123
0
1534236469

# output
-2143847412
321
-321
0
0
```

### Benchmarks and Remarks

```
 Runtime: 32 ms, faster than 94.77% of Python3 online submissions for Reverse Integer.
 Memory Usage: 13.2 MB, less than 78.51% of Python3 online submissions for Reverse Integer.
```

I could deal with bits and manual operations, but the `.bit_length()` method was so tempting to use.

Remember to reverse the number *after* reversing it.
