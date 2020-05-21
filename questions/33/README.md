# 33. Search in Rotated Sorted Array

Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

### Examples

Example 1:
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

X. Title of Problem

<difficultyLvl>

Problem Definition
Problem Definition
Problem Definition
Problem Definition

### Examples

### Testcases
```
[4,5,6,7,0,1,2]
0
[4,5,6,7,0,1,2]
6
```

### Benchmarks and Remarks

```
 Runtime: 48 ms, faster than 79.82% of Python3 online submissions for Search in Rotated Sorted Array.
 Memory Usage: 14.1 MB, less than 5.19% of Python3 online submissions for Search in Rotated Sorted Array.
 Runtime: 52 ms, faster than 51.07% of Python3 online submissions for Search in Rotated Sorted Array.
 Memory Usage: 14.2 MB, less than 5.19% of Python3 online submissions for Search in Rotated Sorted Array.
```

A modified Binary Search to achieve the O(logn) that was required by the problem definition.

When the array is pivoted like that, one half will always be correctly sorted.

If the target is either in the "correctly" sorted half, we continue the binary search as usual.    
In the case that it's in the "pivoted" half, we make the next iteration go through this pivoted half instead.
