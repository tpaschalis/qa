# 11. Container With Most Water

Medium 

Given n non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

### Examples

Example 1
```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

### Testcases
```
[1,8,6,2,5,4,8,3,7]
[2,2]
[2,0,2]
```

### Benchmarks and Remarks

```
 Runtime: 68 ms, faster than 46.91% of Python3 online submissions for Container With Most Water.
 Memory Usage: 14.2 MB, less than 99.09% of Python3 online submissions for Container With Most Water.
```

Brute force solution is O(n²), as we pass through every possible pair.

A one-pass O(n) solution is to begin with the leftmost and rightmost columns. Since the total volume of 'water'/area is bounded by the lower value in the leftmost-rightmost pair, we move that index towards the center. Keep doing that until the left and right barriers meet each other, and you're done!
