# 4. Median of Two Sorted Arrays

Hard

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.


## Examples
Example 1:
```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

Example 2:
```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

### Testcases
```
[1, 2]
[3, 4]
```

### Benchmarks and Remarks

First approach was using Python's built-in tools. It was accepted, and was quite fast.
```
 Runtime: 52 ms, faster than 92.64% of Python3 online submissions for Median of Two Sorted Arrays.
 Memory Usage: 13.5 MB, less than 20.16% of Python3 online submissions for Median of Two Sorted Arrays.
```


But let's look at the math behind it, and find something even clever-er!!   
https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
