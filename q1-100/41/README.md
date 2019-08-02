# 41. First Missing Positive

Hard

Given an unsorted integer array, find the smallest missing positive integer.

### Examples

Example 1:
```
Input: [1,2,0]
Output: 3
```

Example 2:
```
Input: [3,4,-1,1]
Output: 2
```

Example 3:
```
Input: [7,8,9,11,12]
Output: 1
```

Note:

Your algorithm should run in O(n) time and uses constant extra space.


### Testcases
```
[2,2]
[1,2,0]
[3,4,-1,1]
[]
```

### Benchmarks and Remarks

```
 Runtime: 40 ms, faster than 82.73% of Python3 online submissions for First Missing Positive.
 Memory Usage: 13.9 MB, less than 5.25% of Python3 online submissions for First Missing Positive.
```

The complexity is O(2N) or O(3N), which is equal to O(N). Wanting to keep the space constant, there are two main options; swapping the nums[i] to nums[nums[i]] and then seeing which one is missing in the second iteration, or use nums[i] to store the frequency of each number in a quasi-hashmap
