# 34. Find First and Last Position of Element in Sorted Array

Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

### Examples

Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```


### Testcases
```
[5,7,7,8,8,10]
8
[1,2,2,3,3,4,5,5,5,6,6,6,7,7,8,9,10,11]
5
```

### Benchmarks and Remarks

```
 Runtime: 96 ms, faster than 76.59% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
 Memory Usage: 14.7 MB, less than 5.38% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
```

Binary Search satisfies our O(logn) solution. Python built-in functions to bisect takes the same time. Another silly idea is to reverse the array and find the occurence from the end.
