# 54. Spiral Matrix

Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

### Examples
```
Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
```
```
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

### Testcases
```
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
```

### Benchmarks and Remarks

```
 Runtime: 32 ms, faster than 92.83% of Python3 online submissions for Spiral Matrix.
 Memory Usage: 13.8 MB, less than 5.25% of Python3 online submissions for Spiral Matrix.
 Runtime: 32 ms, faster than 92.83% of Python3 online submissions for Spiral Matrix.
 Memory Usage: 13.9 MB, less than 5.25% of Python3 online submissions for Spiral Matrix.
```

I included both a Pythonic, fun solution that is O(n^2), as well as the straightforward O(n) approach.

Whenever you hit a boundary, or a revisited position, you turn clockwise as per `(dr, dc)`. This way, you're facing at `di`. Then calculate the next step you're currently about to take, and either go in the same direction, or turn clockwise.

