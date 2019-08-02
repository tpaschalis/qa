# 35. Search Insert Position

Easy

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

### Examples

Example 1:
```
Input: [1,3,5,6], 5
Output: 2
```

Example 2:
```
Input: [1,3,5,6], 2
Output: 1
```

Example 3:
```
Input: [1,3,5,6], 7
Output: 4
```

Example 4:
```
Input: [1,3,5,6], 0
Output: 0
```

### Testcases
```
[1,3,5,6]
5
[1,3,5,6]
0
[1,3,5,6]
7
[1]
1
```

### Benchmarks and Remarks

```
 Runtime: 52 ms, faster than 97.26% of Python3 online submissions for Search Insert Position.
 Memory Usage: 14.4 MB, less than 5.18% of Python3 online submissions for Search Insert Position.
```

O(logn). Slight modification, so that binary keeps working if original sorted list has duplicate values

